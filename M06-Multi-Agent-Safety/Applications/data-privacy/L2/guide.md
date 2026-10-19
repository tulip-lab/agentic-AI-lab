# L2：比较隐私参数、误差与重复发布

## 1. Overview and Learning Goals

完成后，你应能读懂 ε 与统计误差的受控比较，计算多次发布的预算上界，并判断原始记录访问风险是否被单独控制。

## 2. Setup and Background

先完成[L1](../L1/guide.md)。本地 Python 3.9+ 即可，无需安装依赖。所有实验只用固定的合成 A 组，不能替换为真实学习记录。

## 3. Core Concepts

`compare` 用固定随机种子重复抽样，便于比较 ε 为 0.25、0.5、1.0 时的平均绝对误差；它公开精确合成计数，因此**不是差分隐私发布**。`release` 使用系统随机源给出带噪结果，且不在输出中写出精确计数。对同一人可能有影响的连续发布，演示预算按各次 ε 相加；本实验仅在单次命令内检查预算，重新运行不会继承历史支出；此处没有选定现实场景的“安全 ε”。

## 4. Guided Implementation

```sh
python3 run_lab.py compare
python3 run_lab.py release --epsilon 0.5 --queries 2 --budget 1 --out /tmp/flip-privacy-l2-a.json
python3 run_lab.py release --epsilon 0.6 --queries 2 --budget 1 --out /tmp/flip-privacy-l2-rejected.json
```

第一条查看误差随 ε 的变化，并注明这是可复现模拟。第二条读取带噪值和已使用预算；新运行必须使用新文件名。第三条应拒绝，因为 0.6 × 2 超过设定预算 1。不要把一次带噪值与精确计数的差距，当作实际机制的可靠误差估计。

## 5. Testing and Analysis

正常：0.5 × 2 恰好用完预算。边缘：一次小组计数的噪声可能很大，甚至给出负数；不要擅自把它解释为真实人数。失败：ε 为 0、非有限数、次数为 0、超预算或输出文件已存在，程序均应停止。比较时一次只改变 ε 或查询次数，并记录另一项是否固定。

## 6. Student Tasks

| 任务 | 目的 | 提交证据 |
| --- | --- | --- |
| 1. 比较三种 ε | 认识隐私与效用取舍 | 模拟表格及其“非发布”标记 |
| 2. 计算两种预算方案 | 理解重复发布 | ε、次数、总预算与接受/拒绝结果 |
| 3. 复核原始记录边界 | 避免误用机制 | 说明差分隐私不能补救的泄密情形 |

## 7. Submission and Reflection

提交命令、模拟表、一次接受与一次拒绝记录，并说明为什么模拟中的精确计数不应与真实数据发布在一起。检查输出路径没有覆盖旧结果。若结果与预期不同，先核对参数单位和预算乘法；不要以修改代码绕过拒绝。反思：增加查询次数会怎样改变可用预算？

#### Further Readings

[NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final)；[L3 OpenDP 进阶](../L3/guide.md)。
