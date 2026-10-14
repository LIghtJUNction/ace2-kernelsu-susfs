import json, os, pathlib, xml.etree.ElementTree as ET
ROOT = pathlib.Path(__file__).resolve().parents[1]
lock = json.loads((ROOT / "sources.lock.json").read_text())
manifest = ET.parse(ROOT / "manifests/oneplus_ace2_b.xml")
for project in manifest.findall("project"):
    name = project.get("name")
    if name in lock["kernel_projects"]:
        assert project.get("revision") == lock["kernel_projects"][name], name
        assert project.get("upstream").endswith("sm8475_b_16.0.0_ace_2"), name
if os.environ.get("GITHUB_EVENT_PATH"):
    inputs = json.loads(pathlib.Path(os.environ["GITHUB_EVENT_PATH"]).read_text())["inputs"]
    expected = {"FILE": "oneplus_ace2_b", "KPM": "N/A", "SUSFS_META": lock["susfs"],
                "KSU_META": "main/v3.3.1/" + lock["kernelsu"], "SUSFS_CI": "N/A",
                "ZRAM": "0/lz4kd/8589934592", "RESUBLEVEL": ""}
    for key, value in expected.items():
        assert str(inputs.get(key, "")) == value, f"Unsupported input {key}"
    for key in ("LZ4_UPDATE", "NETFILTER", "CCM", "UNICODE_BYPASS", "SCHED_HMBIRD", "DROID_SPACES", "RE_KERNEL", "SUSFS_DEV"):
        assert str(inputs.get(key, "false")).lower() == "false", f"Extra feature {key} disabled in baseline"
    assert str(inputs["LSM_BBG"]).lower() == "true", "Keep critical partition protection"
print("Ace 2 source pins and baseline inputs verified")
