# Flowise：课程资源候选的人工审核关口

此可选扩展把已通过离线结构与引文检查的合成候选接入 Flowise Agentflow V2，展示真正的暂停、拒绝、继续与恢复。流程只有 Start、Human Input 和两个 Direct Reply；没有模型、外部工具、凭据、发布或评分节点。Proceed 表示通过**本地流程演示**，不代表教师正式采用课件。

## 准备与导入

1. 先完成上级 [课程资源实验](../README.md) 的正常运行，阅读其 review.md，并保留教师待核查项目。
2. 在本目录生成与当前候选绑定的导入文件：

   ```sh
   python3 build_flow.py --plan ../fixture-plan.json --out /tmp/flip-course-gate.json
   ```

   使用 L3 的检索结果时，同时指定该次运行保存的任务：`--plan <L3 输出>/plan.json --task <L3 输出>/task.json`，并使用新输出文件。程序会核对案例哈希、来源和逐字引文，再把候选摘要哈希与所选来源写入人工审核提示。
3. 在本地 `flowiseai/flowise:3.1.3` 镜像的 Agentflows 界面导入 JSON。Flowise 需按课程的 M03 环境指南启动，绑定本机并使用独立账户；不要在公开仓库保存账户、API key 或运行记录。
4. 在界面用合成问题启动，确认 Human Input 暂停；分别在新会话中选择 Reject 和 Proceed，检查两条 Direct Reply 分支。也可用下面的脚本对已导入的 flow ID 作端到端核验：

   ```sh
   python3 pilot.py --base-url http://127.0.0.1:3000 --flow-id <导入后ID> --out /tmp/flip-flowise-pilot.json
   ```

   如果该 flow 设置了 API key，把它仅放在本地环境变量 `FLOWISE_API_KEY`；脚本只读取，不写入文件。报告包含 chat ID 和审核路径，仅用于本地实验。

## 学习者任务与边界

先独立判断一个事实与一个教学适切性问题，再比较 Flowise 的 Reject/Proceed 控制流程。将来源冲突的候选交给上级 Python 检查，观察其在进入 Flowise 前停止；不要靠人工关口补救未通过契约的引文。说明自动检查与教师审核分别处理了什么。

本适配器验证平台的流程控制，不评价模型生成质量。没有本地 Flowise 时，可使用 L1/L2/L3 离线材料完成课程任务。
