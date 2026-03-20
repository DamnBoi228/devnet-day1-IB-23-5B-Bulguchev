import os
import json
import hashlib
import subprocess
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).parent.parent
ART = ROOT / "artifacts" / "day5"
SCHEMA = ROOT / "schemas" / "day5_summary.schema.json"

def jload(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def file_nonempty(path):
    p = Path(path)
    return p.exists() and p.stat().st_size > 0

# ── обязательные артефакты ──────────────────────────────────────────

REQUIRED_FILES = [
    ART / "yang" / "ietf-interfaces.yang",
    ART / "yang" / "pyang_version.txt",
    ART / "yang" / "pyang_tree.txt",
    ART / "webex" / "me.json",
    ART / "webex" / "rooms_list.json",
    ART / "webex" / "room_create.json",
    ART / "webex" / "message_post.json",
    ART / "webex" / "messages_list.json",
    ART / "pt" / "external_access_check.json",
    ART / "pt" / "serviceTicket.txt",
    ART / "pt" / "network_devices.json",
    ART / "pt" / "hosts.json",
]

@pytest.mark.parametrize("fpath", REQUIRED_FILES)
def test_artifact_exists_and_nonempty(fpath):
    assert Path(fpath).exists(), f"Missing: {fpath}"
    assert Path(fpath).stat().st_size > 0, f"Empty: {fpath}"

# ── summary builder ─────────────────────────────────────────────────

def test_day5_summary_and_schema():
    env = os.environ.copy()
    assert env.get("STUDENT_TOKEN"), "STUDENT_TOKEN not set"
    assert env.get("STUDENT_NAME"), "STUDENT_NAME not set"
    assert env.get("STUDENT_GROUP"), "STUDENT_GROUP not set"

    r = subprocess.run(
        ["python", "src/day5_summary_builder.py"],
        cwd=str(ROOT), env=env,
        capture_output=True, text=True
    )
    assert r.returncode in (0, 2), f"Builder failed:\n{r.stderr}"

    summary_path = ART / "summary.json"
    assert summary_path.exists(), "summary.json not created"

    summary = jload(summary_path)
    schema = jload(SCHEMA)
    jsonschema.validate(instance=summary, schema=schema)

    # token_hash8 корректен
    token = env["STUDENT_TOKEN"]
    expected_hash8 = hashlib.sha256(token.encode()).hexdigest()[:8]
    assert summary["student"]["token_hash8"] == expected_hash8, \
        f"token_hash8 mismatch: {summary['student']['token_hash8']} != {expected_hash8}"

# ── признаки из G.1 ─────────────────────────────────────────────────

def test_yang_interfaces_in_tree():
    pyang_tree = (ART / "yang" / "pyang_tree.txt").read_text(encoding="utf-8")
    assert "+--rw interfaces" in pyang_tree, "pyang_tree.txt missing '+--rw interfaces'"

def test_webex_room_title_has_token_hash8():
    token = os.environ.get("STUDENT_TOKEN", "")
    token_hash8 = hashlib.sha256(token.encode()).hexdigest()[:8]
    room = jload(ART / "webex" / "room_create.json")
    title = room.get("title", "")
    assert token_hash8 in title, \
        f"room_create.json title '{title}' does not contain token_hash8 '{token_hash8}'"

def test_pt_empty_ticket_check():
    content = (ART / "pt" / "external_access_check.json").read_text(encoding="utf-8")
    assert "empty ticket" in content, \
        "external_access_check.json missing 'empty ticket'"

def test_pt_network_devices_ok():
    content = (ART / "pt" / "network_devices.json").read_text(encoding="utf-8")
    assert '"version": "1.0"' in content or "'version': '1.0'" in content, \
        "network_devices.json missing version 1.0"

def test_pt_hosts_ok():
    content = (ART / "pt" / "hosts.json").read_text(encoding="utf-8")
    assert '"version": "1.0"' in content or "'version': '1.0'" in content, \
        "hosts.json missing version 1.0"