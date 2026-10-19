# L2：自定义与受控比较

## 1. Overview and Learning Goals

修改课程上下文或教学设计，比较结果并诊断失败。保持一次只改变一项条件。

## 2. Setup and Background

先完成 [L1](../L1/guide.md)。复制 case 中 task.json 到自己的工作目录，复制上级 fixture-plan.json 作为候选。输出使用新目录，不覆盖指导示例。

## 3. Core Concepts

task 规定资料范围，candidate 规定学习目标、逐字事实引文、活动及反思。事实必须来自选择的来源，目标和活动仍是建议。模型可帮助起草候选，但其文本不能成为指令或权限。

## 4. Guided Implementation

先运行基线，再只改变 audience 或 activity，并用 `--task <任务.json> --candidate <候选.json> --out <新目录>` 检查。若添加 DP-ACCESS 或 DP-CONSENT 到 source_ids，同步补充 candidate 中的对应事实引文；若不补，检查应报告证据覆盖不足。

要体验 AI 生成，先取得基线的 generation-prompt.md，再把它和 plan.schema.json 提供给自己可用的模型，保存输出 JSON 并通过同一命令导入。记录模型、日期、任务版本、修改和结果。不要上传自己的私有资料或密钥；不必为完成离线学习购买服务。

还可只改变统计发布频次，比较候选是否提醒累计隐私损失与误差；这属于概念审核，不声称完成差分隐私实现。

## 5. Testing and Analysis

至少记录正常变更、缺失来源、伪造引文三种结果。程序停止也是有效证据。外部模型若返回 Markdown 代码块，应保存为纯 JSON 后再检查，不能用执行任意代码的方式“解析”。

## 6. Student Tasks

完成一组受控比较，提交变更前后 task/candidate、质量报告和人工修改记录。进一步尝试让活动漏掉一项目标，观察拒绝原因；之后自己修正。

## 7. Submission and Reflection

解释变更是否改善了教学目标、活动适切性和证据质量。成本、延迟、模型信息仅对真实模型运行报告；离线 fixture 标为手写基线。检查通过不自动意味着可以发布或评分。

#### Further Readings

[输出契约](../plan.schema.json)；[实践说明](../README.md)。
