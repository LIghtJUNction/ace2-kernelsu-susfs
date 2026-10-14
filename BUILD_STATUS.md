# Verified build: PHK110 Android 16

- Build: https://github.com/LIghtJUNction/ace2-kernelsu-susfs/actions/runs/38602223532
- Built source commit: `8736021c1a9b03fa1451d0632d9b96f74ae93fc0`.
- Upstream KernelSU v3.3.1 commit: `0c0fdb960178fa12d80d6cbcfdcb6ad8be6a865d`.
- Actual driver version reported by KernelSU Kbuild: `32680`.
- Kernel: `5.10.236-android12-ace2-ksu-susfs`; SUSFS: `v2.3.0`.
- Workflow completed successfully. Embedded image config matches actual build config; KSU, SUSFS and bootconfig spoofing are enabled. No KPM.
- Both downloaded artifact archives match GitHub SHA256 digests; all 13 package files match the build receipt.
- Kernel artifact ZIP SHA256: `9b94dd8cafb92c4401a975fe22724a504573610b6b9f77d930af946373520c72`.
- Image SHA256: `e6f93ce39a79873c1061663d663aacb799b112197e5ad89fd7dea571416cfd5e`.
- Status: built and inspected; NOT flashed or device-tested.

The original artifact name contains `KernelSU_30050` because packaging counted a shallow Git history before Kbuild restored full history. The actual compiled driver is `32680`. Future packaging now restores history first; this naming fix does not change the existing kernel image.
