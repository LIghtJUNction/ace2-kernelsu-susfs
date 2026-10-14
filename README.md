# Ace 2: upstream KernelSU + SUSFS

Personal maintenance fork of [Numbersf/Action-Build](https://github.com/Numbersf/Action-Build/tree/KernelSU). Original authorship and license are retained in README.upstream.md and LICENSE.

Target: OnePlus Ace 2 (PHK110), stock ColorOS 16, android12-5.10.236. This is not for Ace 2 Pro or Ace 2V.

The maintained branch uses tiann/KernelSU v3.3.1 and SUSFS, with source revisions in sources.lock.json. KPM/KPN, extra schedulers, networking tweaks, ZRAM changes and APK/module auto-installation are disabled. Critical-partition write protection remains enabled.

Run the manual **Build Ace 2 - upstream KernelSU and SUSFS** workflow on branch `ace2-kernelsu-susfs`. A successful build must include build-evidence with the actual configuration, source manifest and SHA256 hashes. Build success is not a device boot test. No flashing is automated.

Before any future flash, inspect the installer and package, preserve the current boot backup and verify matching kernel/Android/device identity. Do not bypass device checks. The installer is limited to PHK110 and Android 16.

The baseline device was PHK110_16.0.2.400(CN01), kernel 5.10.236-android12-9. Backups are private and are not included in this repository.
