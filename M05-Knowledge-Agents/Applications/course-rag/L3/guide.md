# L3：实现可核查的检索与资源生成流程

## 1. Overview and Learning Goals

完成后，你能解释检索排名如何影响候选内容，实现检索—生成—检查的接口，并用正常与失败记录说明系统边界。适合完成 L2、能够运行 Python 的本科生和研究生；建议作为课后项目。

## 2. Setup and Background

使用 Python 3.9 以上版本，无需密钥和额外依赖。在本实验根目录运行命令，输出目录换成尚未使用的目录。先阅读 [L2](../L2/guide.md) 与 [输出契约](../plan.schema.json)。只用案例中的原创合成资料。

## 3. Core Concepts

英文按单词、中文按相邻双字切分，以词频余弦相似度排序，只从 approved_teaching 来源中取 top-k。词面相似度不能判断真实性或适用性；例如两个矛盾的保存期片段都可能相关。

生成边界接受两种候选：确定性模板将选中资料组织成学习目标、活动和逐字引文；外部模型按照同一契约另行生成候选。模板不代表模型效果。所有候选都经过来源、已标注冲突、引文和目标覆盖检查，再由教师审核。

## 4. Guided Implementation

```sh
python3 run_l3.py --query '隐私泄露 数据泄密 差分隐私' --top-k 3 --out /tmp/flip-l3-normal
python3 run_l3.py --query '保存期' --top-k 2 --out /tmp/flip-l3-conflict
python3 -m unittest discover -p 'test*.py'
```

第一条尝试检索三类概念；检查 trace 中的实际排名及是否遗漏概念。第一条产生教学资源、task.json 与 trace；task.json 记录这次实际检索选中的来源，可交给 [Flowise 人工关口](../flowise/README.md)；第二条应停止且不创建输出，因为 RETENTION-A/B 的保存期存在手工标注的冲突。

若使用模型，先读取正常运行的 generation-prompt.md 和 plan.schema.json，另存 JSON 候选，然后以相同 query/top-k 加 `--candidate <候选.json>` 导入。来源集合必须匹配该次检索，不能把旧候选直接当作新检索结果。记录模型与日期，不提交密钥。

## 5. Testing and Analysis

比较 top-k=1 与 top-k=3：哪些来源和教学活动改变？再用无命中查询 `zzxyq987654` 和保存期冲突查询观察停止行为。尝试加入未选择的引文，检查拒绝原因。

消融比较可把“按任务明确选来源”的原 run_demo.py 作为基线，与 run_l3.py 的自动词面检索比较。二者使用同一输出检查。记录来源覆盖、人工修改次数和停止原因；不要用检查通过率推断教学效果。程序不自动检测未标注的语义矛盾。

## 6. Student Tasks

| 任务 | 目的 | 提交证据 |
| --- | --- | --- |
| 实现或修改检索排序 | 理解 context acquisition | 排序方法、一次受控变更、前后排名 |
| 对比两种候选来源 | 区分流程与模型能力 | 手写模板/真实模型标识、引用与目标覆盖报告 |
| 构造边界输入 | 验证停止行为 | 无命中、来源冲突、伪造引文三种记录 |
| 提出适切性修订 | 连接技术与教学 | 人工修改理由与未解决问题 |

## 7. Submission and Reflection

提交 query、task、candidate、trace、检查结果及人工复核。不要交真实学生数据。解释一个词面相关但教学上不适用的来源，说明如何改进检索与人工确认；研究生可增加多个查询的消融比较，但须报告样本量与局限。

#### Further Readings

[检索实现](../retrieval.py)、[L3 运行器](../run_l3.py)、[边界案例](../../../../Data/case-packs/data-privacy-ai-security/v3/boundary-scenarios.json)。
