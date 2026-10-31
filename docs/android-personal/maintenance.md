# 安卓个人维护版

## 来源与保存位置

- 主项目基线：`DarkLingYun/MaaGF2Exilium`，提交 `8bf0d192cabda42785bb5b9153d7dc90f31afc92`。
- 安卓外壳：子模块 `Aliothmoon/MaaFwApp`，提交 `4384ba1dd4f921ebf37a9617d3e070eb61b6048a`。
- 公共资源：子模块 `MaaXYZ/MaaCommonAssets`，提交 `dabcd4681ac990dc4361de26416d986abd80e4aa`。
- 已验证 MaaFramework：`v5.14.3`；Python agent core：`3.13.15-maafw5.14.3`。
- 个人基线：`speedfix5`。建仓整理现有修改，没有合入后来的上游功能，也没有重新安装手机应用。

`Android/mobile-overrides.json` 保存安卓识别区域和流程；`Android/prepare.py` 将其应用到暂存资源并选择 tiny OCR。`Android/patches/` 保存安卓外壳的权限修改，使用 `Android/apply_patches.py` 检查并应用；重复执行不会重复修改。子模块指针保留原公开版本，避免主仓库指针与本机修改不一致而漏掉补丁。更新外壳后如补丁不能应用，应人工检查，脚本不会丢弃修改。

## 从干净检出构建

准备 Git、Python 3.13、uv 0.12.16、JDK 25、Android SDK 37、Build Tools 36.0.0、NDK 29.0.13113456、CMake 3.22.1。Gradle 使用外壳自带的 wrapper。

```sh
git clone --recurse-submodules https://github.com/KarlTex123/MaaGF2Exilium-Android-Personal.git
cd MaaGF2Exilium-Android-Personal
python Android/apply_patches.py
python Android/prepare.py --version personal-speedfix5 --repository KarlTex123/MaaGF2Exilium-Android-Personal
python Android/build_runtime.py --abis arm64-v8a --framework-tag v5.14.3
```

在 `Android/MaaFwApp/local.properties` 设置当前电脑的 `sdk.dir` 路径，并填写：

```properties
pi.profile=../profile.yaml
build.debugAbi=arm64-v8a
build.releaseAbi=arm64-v8a
build.ndkVersion=29.0.13113456
```

进入 `Android/MaaFwApp` 运行 `./gradlew :app:assembleDebug`；Windows 使用 `gradlew.bat :app:assembleDebug`。产物位于外壳的 `app/build/outputs/apk/debug/`。运行时构建会联网下载官方框架和匹配的 agent core；升级框架时需同时验证内核版本。

仓库保留手动 Android 构建入口。首次上传没有配置签名 Secrets 或自动发布，云端生成的临时 debug 签名不能保证覆盖个人手机现有版本。

## 更新与回退

个人远程地址通常命名为 `origin`，原项目命名为 `upstream`。查看上游变化，在单独分支合并需要的更新；检查覆盖项、外壳补丁、构建及实机行为后，再合入 `main` 并标记个人版本。首次上传只推送维护分支与个人标签，不把上游标签当成本维护版发布。

覆盖安装依赖原签名，源码和 APK 不能代替密钥备份。安装前备份手机配置，并确认包内资源重新解包。最少检查启动、主页、邮件、体力不足退出；如修改战斗或周常，另测对应流程。

## 验证边界

- 历史 mailfix5：用户物理拔USB运行启动与邮件，重连日志完成。
- speedfix4：启动、邮件/边界恢复/班组补给及收尾奖励子集有线完成；完整日常复测在体力环节取消。
- speedfix5：启动与补给有线完成。精准体力弹窗识别在原图回放通过，真实运行仍漏检；四次上限保护实际生效并返回主页。完成表示结束扫荡尝试，不表示补充了体力或领到了奖励。
- 完整周常、熄屏运行、自启动和多设备兼容性没有全面验证。

## 上传内容与脱敏

新增内容仅含源码、通用流水线数据、小图标、补丁及脱敏说明。两张新增PNG仅含导航/邮件图标，已人工查看，没有账号区域。

不上传设备序列号、账号/UID、个人联系方式、配置UUID、原始手机日志/截图、ADB路径、本机用户名和绝对路径、APK、密钥、令牌、SDK及缓存。原始部署记录和个人配置备份保留在本机工作区，不属于本仓库。

原项目已有公开作者信息、许可证及提交历史保留。新增维护提交使用 GitHub noreply 邮箱，避免把维护者私人邮箱写入提交元数据。
