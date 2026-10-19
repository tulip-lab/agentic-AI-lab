# L1：直接使用与审核

目标是把资料、教学设计与采用决定区分开。无需安装或编程，可阅读案例和手写示例；如有 Python，运行上级 README 的基线命令。

## 1. Overview and Learning Goals

从 task.json 识别受众和主题，解释三项目标与课堂活动如何关联，核对一条事实来源，并指出需人工判断的地方。

## 2. Setup and Background

阅读 [案例](../../../../Data/case-packs/data-privacy-ai-security/v3/README.md)、task.json 和上级 fixture-plan.json。这里的默认示例由作者编写，不代表模型实际回答。

## 3. Core Concepts

课程知识是证据，目标与活动是教学设计建议。程序检查引用和结构，教师判断事实适切性与教学价值。检索文本不是工具授权。

## 4. Guided Implementation

按上级 README 运行基线或阅读 fixture，依次核对：目标 O1/O2/O3、所选来源、活动对齐和人工审核项。把一个事实回溯到 corpus.json 中的同编号文字，再阅读 quality-report 中仍需人审的部分。

核对三类风险：小分组或重叠统计造成推断泄露、原始记录被越权取得造成数据泄密、差分隐私用于控制统计发布的个体影响。明确差分隐私不能补救原始数据泄密。

## 5. Testing and Analysis

比较三种输入：正常资料、请求不存在的来源、请求不可信讨论区内容。后两者应停止，不补造规则。运行测试时可检查 test_demo.py 中的对应拒绝行为。

## 6. Student Tasks

选择自己的一门课程，写出受众、一个可观察目标、一项活动和一个审核问题；只使用公开或合成资料。说明哪个判断依赖证据，哪个是教学建议。

## 7. Submission and Reflection

保留目标—活动对应、来源核对及采用/修改理由。若不运行代码，提交阅读核对即可；不得把阅读 fixture 记为真实模型实验。

#### Further Readings

[实践说明](../README.md)；[课程知识案例](../../../../Data/case-packs/data-privacy-ai-security/v3/README.md)。
