# Ace 2: upstream KernelSU + SUSFS

Personal maintenance fork of [Numbersf/Action-Build](https://github.com/Numbersf/Action-Build/tree/KernelSU). Original authorship and license are retained in README.upstream.md and LICENSE.

Target: OnePlus Ace 2 (PHK110), stock ColorOS 16, android12-5.10.236. This is not for Ace 2 Pro or Ace 2V.

The maintained branch uses tiann/KernelSU v3.3.1 and SUSFS, with source revisions in sources.lock.json. KPM/KPN, extra schedulers, networking tweaks, ZRAM changes and APK/module auto-installation are disabled. Critical-partition write protection remains enabled.

Run the manual **Build Ace 2 - upstream KernelSU and SUSFS** workflow on branch `ace2-kernelsu-susfs`. A successful build must include build-evidence with the actual configuration, source manifest and SHA256 hashes. Build success is not a device boot test. No flashing is automated.

Before any future flash, inspect the installer and package, preserve the current boot backup and verify matching kernel/Android/device identity. Do not bypass device checks. The installer is limited to PHK110 and Android 16.

The baseline device was PHK110_16.0.2.400(CN01), kernel 5.10.236-android12-9. Backups are private and are not included in this repository.

## 为什么 GitHub 显示落后上游几百个提交？

上游 `Numbersf/Action-Build` 的默认分支是 `SukiSU-Ultra`，本仓库的维护分支 `ace2-kernelsu-susfs` 则基于上游 `KernelSU` 分支。GitHub 仓库首页的 fork 对比默认使用上游默认分支，因此可能显示落后几百个提交。

`SukiSU-Ultra` 和 `KernelSU` 已经分叉。这个数字表示提交历史的差异，不能据此判断本仓库漏掉了原版 KernelSU 分支的更新，也不代表内核或 KernelSU 驱动的版本落后。

请使用[与上游 KernelSU 分支的正确对比](https://github.com/Numbersf/Action-Build/compare/KernelSU...LIghtJUNction:ace2-kernelsu-susfs)查看同步状态。本仓库建立时已基于该分支的最新提交；此后是否需要同步，以这个对比页面为准。内核、KernelSU 和 SUSFS 实际采用的源码版本则以 `sources.lock.json` 为准。

不要直接用默认的 **Sync fork** 将 `SukiSU-Ultra` 合入维护分支。维护本仓库时，应检查上游 `KernelSU` 分支，选择需要的更新，并保留本仓库的 Ace 2 配置与验证步骤。

## 维护与构建

维护分支为 `ace2-kernelsu-susfs`，仅使用原版 `tiann/KernelSU`，不使用 Next。

1. 在 `sources.lock.json` 查看锁定的版本；一加项目的提交同时记录在 `manifests/oneplus_ace2_b.xml`。
2. 在 Actions 手动运行 `Build Ace 2 - upstream KernelSU and SUSFS`。默认参数是本项目的基础构建；参数检查会拒绝其他机型、漂移的 KSU/SUSFS 提交以及额外功能。
3. 构建成功后取得两个产物：AnyKernel3 包和 `ace2-build-evidence`。后者包含实际配置、镜像内嵌配置、源码清单、哈希与构建状态。
4. 更新系统后先核对源码、内核分支和兼容性，不能只看版本号，也不要跳过设备检查。

构建流程不会刷写手机。首次产物在真机启动、Root 和 SUSFS 功能验证之前，只能称为构建通过。
