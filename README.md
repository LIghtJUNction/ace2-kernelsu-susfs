# Ace 2: upstream KernelSU + SUSFS

Personal maintenance fork of [Numbersf/Action-Build](https://github.com/Numbersf/Action-Build/tree/KernelSU). Original authorship and license are retained in README.upstream.md and LICENSE.

Target: OnePlus Ace 2 (PHK110), stock ColorOS 16, android12-5.10.236. This is not for Ace 2 Pro or Ace 2V.

The maintained branch uses tiann/KernelSU v3.3.1 and SUSFS, with source revisions in sources.lock.json. KPM/KPN, extra schedulers, networking tweaks, ZRAM changes and APK/module auto-installation are disabled. Critical-partition write protection remains enabled.

Run the manual **Build Ace 2 - upstream KernelSU and SUSFS** workflow on branch `ace2-kernelsu-susfs`. A successful build must include build-evidence with the actual configuration, source manifest and SHA256 hashes. Build success is not a device boot test. No flashing is automated.

Before any future flash, inspect the installer and package, preserve the current boot backup and verify matching kernel/Android/device identity. Do not bypass device checks. The installer is limited to PHK110 and Android 16.

The baseline device was PHK110_16.0.2.400(CN01), kernel 5.10.236-android12-9. Backups are private and are not included in this repository.

## 维护与构建

维护分支为 `ace2-kernelsu-susfs`，仅使用原版 `tiann/KernelSU`，不使用 Next。

1. 在 `sources.lock.json` 查看锁定的版本；一加项目的提交同时记录在 `manifests/oneplus_ace2_b.xml`。
2. 在 Actions 手动运行 `Build Ace 2 - upstream KernelSU and SUSFS`。默认参数是本项目的基础构建；参数检查会拒绝其他机型、漂移的 KSU/SUSFS 提交以及额外功能。
3. 构建成功后取得两个产物：AnyKernel3 包和 `ace2-build-evidence`。后者包含实际配置、镜像内嵌配置、源码清单、哈希与构建状态。
4. 更新系统后先核对源码、内核分支和兼容性，不能只看版本号，也不要跳过设备检查。

构建流程不会刷写手机。首次产物在真机启动、Root 和 SUSFS 功能验证之前，只能称为构建通过。
