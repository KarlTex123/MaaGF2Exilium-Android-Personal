# MaaGF2Exilium Android Personal

《少女前线2：追放》安卓手机独立运行的个人维护版，基于 [DarkLingYun/MaaGF2Exilium](https://github.com/DarkLingYun/MaaGF2Exilium) 和 [Aliothmoon/MaaFwApp](https://github.com/Aliothmoon/MaaFwApp)。当前基线为 `speedfix5`。

本仓库保留原项目历史及许可证；原版说明见 [README.upstream.md](README.upstream.md)。本地修改以源码提交和安卓外壳补丁保存，可以在干净检出后重新应用。

## 当前范围

- 已在一加 Ace 5 Pro、Android 17、Root 后端、1280×720 后台虚拟屏上验证过部分流程。运行任务由手机本机控制，不依赖电脑 ADB 持续连接。
- 邮件导航、首次巡录介绍、升级弹窗和部分领奖收尾适配。
- Android 使用 PP-OCRv6 tiny 模型及局部识别区域，减少全屏识别和重复等待。
- 扫荡按钮最多命中4次；识别异常时提示停止本项并返回主页，避免反复打开补充体力界面。
- 后台授权保留应用自身授权，取消调用关闭全局“幽灵进程”清理机制的操作。

## 已知限制

- 体力补充弹窗的精准识别在真实运行中仍有漏检；实测通过的是有限重试后退出保护。
- 部分主页按钮适配依赖当前3D场景和布局；其他背景、设备、语言及游戏版本需要另行验证。
- 当前实兵演习脚本只领取奖励，战斗需要在游戏中另行处理。
- 茶歇需要先收藏可制作饮品；当期边界等入口不存在时会提示跳过。
- 完整日常、完整周常、熄屏运行及重启自启动尚未全部验收。历史基线的启动与邮件曾通过物理拔USB测试；`speedfix5` 的启动与体力保护通过有线测试，不能等同于全日常通过。

## 使用与构建

测试安装包见 [Releases](https://github.com/KarlTex123/MaaGF2Exilium-Android-Personal/releases)。`personal-speedfix5-r1` 在原 speedfix5 的任务逻辑上移除安卓用不到的 Windows 启动程序，避免依赖包夹带本机构建路径。该版本使用本地 debug 签名，非官方发行包；完整日常、周常仍待验收。

当前按 Root 方式维护。Shizuku 只完成[代码检查](docs/android-personal/shizuku-review.md)，没有实机验证。未配置手机自动更新或自动发布。手动 Android 构建入口保留，云端临时 debug 签名不能保证覆盖个人手机现有安装；长期更新需要沿用原签名，密钥在代码库之外单独保存。

构建方法、验证范围和上传内容说明见 [安卓维护说明](docs/android-personal/maintenance.md)。本仓库没有上传个人手机配置、账号信息、设备日志、调试截图、签名密钥或本地工具链。

## 许可与来源

主项目许可见 [LICENSE](LICENSE)，安卓外壳许可见 [MaaFwApp LICENSE](https://github.com/Aliothmoon/MaaFwApp/blob/4384ba1dd4f921ebf37a9617d3e070eb61b6048a/LICENSE)，其他依赖沿用各自许可。原项目文档、署名和公开历史保留；个人维护者新增提交使用 GitHub noreply 邮箱。
