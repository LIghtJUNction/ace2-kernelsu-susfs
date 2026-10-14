# Ace 2 maintenance rules

- This fork targets OnePlus Ace 2 PHK110, stock ColorOS 16, android12-5.10.236. Ace 2 Pro and Ace 2V are different targets.
- Use upstream tiann/KernelSU only. Do not substitute KernelSU-Next, SukiSU, MKSU or BakaSU.
- Read sources.lock.json before changing sources. Keep source changes deliberate, record every upstream commit and preserve the original license/attribution.
- Keep the baseline small: SUSFS and critical-partition write protection; no KPM/KPN, scheduler or networking additions without a separate request.
- Validate workflow defaults against scripts/validate_ace2.py, parse YAML, and check shell syntax locally before pushing build changes.
- A successful artifact must pass scripts/verify_ace2_build.py, including the embedded Image config check. Do not weaken verification to make a failed build green.
- Keep build provenance, actual kernel config and SHA256 receipts alongside each delivered image. Distinguish built, inspected and device-tested states.
- Building is not authorization to flash. Do not write phone partitions, reboot or install modules without authorization for that action. Never touch ABL/efisp as part of this kernel build.
- Preserve private device backups locally; never add device property dumps, partition images, credentials or keyboxes to the repository.
