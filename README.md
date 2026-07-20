# FlClash 免费节点仓库

本仓库用于保存每天更新的 Clash / FlClash 免费节点配置。

## 固定订阅地址

FlClash 中长期使用下面这个链接：

```text
https://raw.githubusercontent.com/50lovelace/flclash-nodes/main/flclash.yaml

只要仓库名称、分支名称和文件名称不变，这个订阅地址就不需要修改。

每日更新方法
打开本仓库的 Actions
点击“更新 FlClash 节点”
点击 Run workflow
粘贴当天新的 Clash 订阅链接
再点击绿色的 Run workflow
等待运行状态变成绿色对勾
回到 FlClash 点击更新配置

系统会自动：

下载当天的 Clash 配置
检查配置内容
覆盖 flclash.yaml
记录更新时间
提交到仓库
文件说明
flclash.yaml：FlClash 实际读取的配置文件
update-info.txt：记录最近一次更新时间和来源链接
.github/workflows/update-nodes.yml：自动更新程序
注意事项
本仓库仅用于保存公开分享的免费节点。
不要上传私人付费机场订阅、订阅令牌或个人节点。
免费节点可能不稳定，也可能随时失效。
不建议通过免费节点处理网银、支付、重要邮箱或敏感资料。
本仓库不保证节点的可用性、安全性和速度。
