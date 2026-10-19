![FLIP](../../../Assets/images/flip-banner.png)

# Data Privacy：从隐私泄露到差分隐私发布

FLIP: Foundations and Engineering of Agentic AI · M06 安全实践案例

Prepared by :tulip: **[TULIP Lab](https://www.tulip.academy), Australia**

本实验延续[共享 Data Privacy v3 案例](../../../Data/case-packs/data-privacy-ai-security/v3/README.md)，只使用六条原创合成记录。学习重点是区分三件事：重叠统计导致的**隐私泄露**、原始记录被越权导出的**数据泄密**、以及限制统计发布中个体影响的**差分隐私**。本地程序不会导出原始记录，也不接入真实课程系统。

| 路线 | 入口 | 成果 |
| --- | --- | --- |
| L1 阅读与判断 | [L1 指引](L1/guide.md) | 风险分类与发布前核查表 |
| L2 受控比较 | [L2 指引](L2/guide.md) | ε、误差、重复发布比较记录 |
| L3 工程进阶 | [L3 指引](L3/guide.md) | 预算边界、OpenDP 对照与失败记录 |

## 运行方式

Python 3.9+ 可直接运行 L1/L2 的命令；不需要账号或第三方库。建议在本目录执行：

```sh
python3 run_lab.py risk
python3 run_lab.py compare
python3 run_lab.py release --epsilon 0.5 --queries 2 --budget 1 --out /tmp/flip-privacy-release.json
python3 -m unittest discover -p 'test*.py'
```

`risk` 展示两项重叠的**精确**统计如何推断虚构成员的二元标志，以及配置错误时原始记录可能被外部读取的风险；不执行导出。`compare` 使用固定随机种子作可复现的误差模拟，**不是可发布的差分隐私结果**。`release` 使用系统随机源输出带噪统计和预算记录，不输出精确值；这仍是教学实现，不能直接用于真实数据发布。L3 另提供基于 OpenDP 预算管理接口的进阶对照；其 Context 调用需启用 `contrib`，仍只用于合成教学。

`--epsilon` 是单次查询预算，`--budget` 是本次程序设置的总预算。这里采用“一条合成记录对应一个人”的教学假设，固定查询的计数敏感度为 1。单次命令内的多次发布按 ε 顺序组合相加；不同命令之间**不保存预算状态**，不能用此程序管理真实发布。较小 ε 通常带来更强的保护和更大的误差；实际参数选择需要情境评估，不能从这个六人样例直接得出安全阈值。

安全边界：无真实学生、客户或研究数据；无密钥、联网或自动发布。即使统计发布采用差分隐私，原始数据的访问控制和泄密事件处理仍是独立问题。技术背景参见 [NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final)；进阶库用法参见 [OpenDP Context 文档](https://docs.opendp.org/en/stable/api/user-guide/context/index.html)。
