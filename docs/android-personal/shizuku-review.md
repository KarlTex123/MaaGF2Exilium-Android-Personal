# Shizuku 代码检查

本次只检查固定外壳提交 `4384ba1dd4f921ebf37a9617d3e070eb61b6048a` 的代码，没有切换手机后端、启停 Shizuku 或申请新的权限。当前个人包按 Root 路径维护。Root 的实机结果不能证明普通 ADB 启动的 Shizuku 具有同样能力。

下列路径均相对于 `Android/MaaFwApp/app/src/main/`。

## 已接入的流程

- `java/com/aliothmoon/maafw/privileged/ShizukuManager.kt` 检查 Binder 和授权，处理服务上线/死亡，并能区分 UID 0 的 Root Shizuku。
- `privileged/ShizukuProcessServiceConnector.kt`（同一 Java 包下）使用 `ShizukuSpawner` 启动与 Root 相同的 `RemoteServiceImpl`，继续复用截图、控制器和 Python agent 路径。
- `privileged/ShizukuSpawner.kt` 通过 `IShizukuService.newProcess` 创建进程；授权通过并不等于整个游戏任务已验证。

## 静态检查发现的边界

1. `privileged/ProcessServiceConnectorBackend.kt` 在 Android 14 及以上请求 `--keep-root`；代码注释将其与输入注入权限关联。`native/launcher.c` 不能把普通 shell UID 提升成 Root。普通 ADB Shizuku 与 Root 启动的 Shizuku 需要分开验证。
2. `remote/AgentInstaller.kt` 使用共享运行时目录，并在标记中记录 UID。切换 UID 后会尝试删除并重新解包，但没有看到针对 Root 所有目录的权限恢复处理。由 Root 切换到普通 shell Shizuku 时可能遇到目录删除或写入失败。这是代码推断，没有在设备上复现。
3. `ShizukuSpawner.kt` 直接使用服务 AIDL 的进程接口；后续升级 Shizuku 时应复查兼容性，不能仅凭现有入口宣称一直可用。

结论：Shizuku 后端在代码中已接入，但本包仅完成代码检查，未通过 Shizuku 实机验收，不作为当前发行包的支持承诺。自用继续选择已经验证的 Root 后端即可。
