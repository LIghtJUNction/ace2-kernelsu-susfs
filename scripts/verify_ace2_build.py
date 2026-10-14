import hashlib, json, os, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parents[1]
lock = json.loads((ROOT / "sources.lock.json").read_text())
platform = ROOT / "kernel_workspace/kernel_platform"
common = platform / "common"
package = ROOT / "AnyKernel3"
evidence = ROOT / "build-evidence"
evidence.mkdir(exist_ok=True)
config_paths = [common / "out/.config"]
config_paths += sorted((platform / "out").glob("**/.config")) if (platform / "out").exists() else []
config_path = next((p for p in config_paths if p.is_file()), None)
assert config_path, "Missing actual build config"
config = config_path.read_text()
required = ("CONFIG_KSU=y", "CONFIG_KSU_SUSFS=y", "CONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y", "CONFIG_IKCONFIG=y")
for setting in required:
    assert setting in config.splitlines(), f"Missing built setting: {setting}"
assert "CONFIG_KPM=y" not in config.splitlines(), "Unexpected KPM enabled"
for tree in (common, platform / "KernelSU"):
    assert not list(tree.rglob("*.rej")), f"Unresolved patch rejects in {tree}"
ksu_sha = subprocess.check_output(["git", "-C", str(platform / "KernelSU"), "rev-parse", "HEAD"], text=True).strip()
assert ksu_sha == lock["kernelsu"], "KernelSU pin mismatch"
assert "github.com/tiann/KernelSU" in subprocess.check_output(["git", "-C", str(platform / "KernelSU"), "remote", "get-url", "origin"], text=True)
image = package / "Image"
assert image.stat().st_size > 10000000, "Kernel Image missing or implausibly small"
embedded = subprocess.check_output(["bash", str(common / "scripts/extract-ikconfig"), str(image)])
assert embedded.decode().strip() == config.strip(), "Image embedded config differs from build config"
installer = package / "anykernel.sh"
text = installer.read_text()
anchor = ". tools/ak3-core.sh"
assert anchor in text
text = text.replace(anchor, """# Maintained fork: reject other devices before any partition write.
[ "$(getprop ro.product.model)" = "PHK110" ] || { echo "PHK110 only"; exit 1; }
[ "$(getprop ro.build.version.sdk)" = "36" ] || { echo "Android 16 only"; exit 1; }
""" + anchor, 1)
text = text.replace("kernel.string=OnePlus Kernel by Numbersf", "kernel.string=Ace 2 upstream KernelSU + SUSFS (Numbersf fork)")
installer.write_text(text)
subprocess.run(["bash", "-n", str(installer)], check=True)
(evidence / "kernel.config").write_text(config)
(evidence / "embedded.config").write_bytes(embedded)
(evidence / "sources.lock.json").write_text(json.dumps(lock, indent=2) + "\n")
receipt = {"device": "PHK110", "android": 16, "kernelsu": ksu_sha, "workflow_commit": os.environ.get("GITHUB_SHA"), "run_id": os.environ.get("GITHUB_RUN_ID"), "status": "built_and_config_verified_not_device_tested", "files": {}}
for f in sorted(package.rglob("*")):
    if f.is_file(): receipt["files"][str(f.relative_to(package))] = {"bytes": f.stat().st_size, "sha256": hashlib.sha256(f.read_bytes()).hexdigest()}
(evidence / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print("KernelSU identity, SUSFS config, embedded config and installer checks passed")
