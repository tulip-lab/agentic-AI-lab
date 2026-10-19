![FLIP](../../../Assets/images/flip-banner.png)

# S03：从课程资料到可审核教学资源

FLIP: Foundations and Engineering of Agentic AI · M05 知识与状态智能体应用

Prepared by :tulip: **[TULIP Lab](https://www.tulip.academy), Australia**

用原创合成的 Data Privacy 案例，体验“课程资料 → 任务规范 → 学习目标与活动 → 讲义/课件/练习 → 证据与质量检查”。

- [L1：直接使用与教师审核](L1/guide.md)
- [L2：修改任务、模型候选与受控比较](L2/guide.md)
- [L3：实现可核查的检索与资源生成流程](L3/guide.md)
- [Flowise：课程资源候选的人工审核关口](flowise/README.md)
- [案例资料](../../../Data/case-packs/data-privacy-ai-security/v3/README.md)
- [输出契约](plan.schema.json)

案例把推断型隐私泄露、原始记录数据泄密、差分隐私统计发布分别作为证据页。差分隐私不替代原始数据的访问控制；L1 识别边界，L2 比较发布方案，L3 检查检索与来源覆盖。

想让参加者亲自比较重叠统计、越权导出与差分隐私预算，可接续 [M06 Data Privacy L1–L3 实验](../../../M06-Multi-Agent-Safety/Applications/data-privacy/README.md)。

## 可运行基线

需要 Python 3.9+，不安装第三方包、不使用账号，也不调用模型。以下命令在本目录运行，输出使用一个全新的本地目录：

```sh
python3 run_demo.py --out /tmp/flip-s03-demo
python3 -m unittest -v test_demo.py
```

默认输入是明确标注的手写教学 fixture，用于演示可复现流程，不能作为真实模型效果证据。生成的 generation-prompt.md 可连同 plan.schema.json 用于自己有权访问的模型；将 JSON 保存后，用 `--candidate <候选.json> --out <新目录>` 导入同一检查链。模型调用由教师自行选择和核查，不会由脚本自动外发资料。

输出含 lesson-plan.md、slides.md、tutorial.md、review.md、trace.json 和 quality-report.json。本样板按显式来源编号选择证据，事实页采用逐字引用，使来源检查可观察；活动和目标属于教学建议，必须教师审核。脚本不自动验证一般语义正确性。

## 行为与安全

正常输入生成完整资源；缺失证据、未批准来源、伪造引用、目标遗漏或危险课件标记会停止，避免写出半成品。输出目录非空时拒绝覆盖。语料中的不可信文本不能提升工具权限；示例不发布课件、不评分、不发送信息。

内容许可 CC BY 4.0，代码 MIT，具体范围见仓库 LICENSING.md。

## 边界案例与进阶实现

同一实验可从 [L1](L1/guide.md)、[L2](L2/guide.md) 进入 [L3](L3/guide.md)。L3 提供可复现的词面检索、外部候选导入与 trace；默认候选来自确定性模板。对证据缺失、已标注冲突、越权资料与伪造引文，观察程序停止与人工核查的分工。

[边界场景](../../../Data/case-packs/data-privacy-ai-security/v3/boundary-scenarios.json)中的两个保存期片段属于虚构的相互矛盾资料，不是机构政策。只识别显式标注的冲突不能代替语义审核。
