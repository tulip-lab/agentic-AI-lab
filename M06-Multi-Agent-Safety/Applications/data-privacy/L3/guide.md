# L3：用 OpenDP 对照预算管理

## 1. Overview and Learning Goals

完成后，你应能明确隐私单位、固定查询与总预算，运行 OpenDP 的 Context 计数发布，并用正常与失败输入说明边界。适合有 Python 基础的本科生或研究生；教师可只阅读输出。

## 2. Setup and Background

先完成[L2](../L2/guide.md)。可在独立虚拟环境中安装 `opendp`，以当前[官方安装与 Context 文档](https://docs.opendp.org/en/stable/getting-started/typical-workflow.html)核对版本。此进阶脚本仅使用六条合成记录；固定小组名单和向量长度在本教学情境中是公开设定，不能直接移植到真实数据。

## 3. Core Concepts

本例调用 OpenDP 当前需要启用 `contrib` 功能；这表明相关构造尚不能作为已完成全面审查的生产发布依据。OpenDP 的 Context 先给定隐私单位和总 ε，再分配查询预算；超出时拒绝继续查询。脚本每次运行新建 Context，不跨命令累计预算；真实发布需要持久化的统一预算管理。这里每条虚构记录对应一个人，每个值限定在 0–1，查询求 A 组三人的二元标志之和。实验中的人、组与数据结构都明确为合成且固定；一旦真实数据的成员身份、贡献次数或分组键也需保护，必须重新设计隐私单位和查询，而不能沿用本脚本的保证。

## 4. Guided Implementation

```sh
python3 -m pip install opendp
python3 run_opendp.py --epsilon 1 --queries 2 --out /tmp/flip-opendp-l3.json
python3 -m unittest discover -p 'test*.py'
```

脚本每次查询分配 ε/2，输出只含带噪值、预算和库版本，不输出真实计数。第二次调用使用新的输出路径。比较标准库教学实现与 OpenDP 的预算管理：两者都能给出随机结果，但后者提供可检查的组合与查询接口。不要给“两个结果哪个更接近真值”赋予单次运行的效能结论。

## 5. Testing and Analysis

正常：两次发布获得两个带噪值。边缘：小数据集的噪声可明显改变结果；不同运行结果应变化。失败：非正或非有限 ε、次数超出实验范围、已存在的输出路径或缺少库时应停止，并说明原因。另检查把差分隐私用于统计发布，不会改变原始记录访问控制的要求。

## 6. Student Tasks

| 任务 | 目的 | 提交证据 |
| --- | --- | --- |
| 1. 运行 OpenDP 对照 | 认识库管理的查询预算 | 命令、版本、两次带噪值 |
| 2. 比较一种参数变更 | 观察取舍 | 固定其他条件的对照记录 |
| 3. 写边界说明 | 防止错误迁移 | 隐私单位、公开假设、原始数据防护 |

## 7. Submission and Reflection

提交运行结果、参数说明、一次失败记录与边界说明。检查结果没有精确合成计数或真实个人资料；若安装失败，记录环境与错误，不要上传密钥或私有数据。思考：若一人可贡献多条记录，为什么“每行即一个人”的假设会失效？

#### Further Readings

[OpenDP Typical Workflow](https://docs.opendp.org/en/stable/getting-started/typical-workflow.html)；[NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final)。
