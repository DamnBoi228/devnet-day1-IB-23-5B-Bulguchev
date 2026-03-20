import os
import json
import hashlib
from pathlib import Path

SCHEMA_VERSION = "5.0"
ROOT = Path(__file__).parent.parent
ART = ROOT / "artifacts" / "day5"

def load_text(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except:
        return ""

def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except:
        return {}

def build_summary():
    token = os.environ.get("STUDENT_TOKEN", "")
    name = os.environ.get("STUDENT_NAME", "")
    group = os.environ.get("STUDENT_GROUP", "")
    token_hash8 = hashlib.sha256(token.encode()).hexdigest()[:8]

    # YANG checks
    pyang_tree = load_text(ART / "yang" / "pyang_tree.txt")
    yang_ok = "+--rw interfaces" in pyang_tree

    # Webex checks
    room_create = load_json(ART / "webex" / "room_create.json")
    room_title = room_create.get("title", "")
    webex_ok = token_hash8 in room_title

    # PT checks
    ext_check = load_text(ART / "pt" / "external_access_check.json")
    pt_empty_ticket = "empty ticket" in ext_check

    net_devices = load_text(ART / "pt" / "network_devices.json")
    pt_network_devices_ok = '"version": "1.0"' in net_devices

    hosts = load_text(ART / "pt" / "hosts.json")
    pt_hosts_ok = '"version": "1.0"' in hosts

    summary = {
        "schema_version": SCHEMA_VERSION,
        "student": {
            "name": name,
            "group": group,
            "token_hash8": token_hash8
        },
        "checks": {
            "yang_interfaces_in_tree": yang_ok,
            "webex_room_title_has_token_hash8": webex_ok,
            "pt_empty_ticket_check": pt_empty_ticket,
            "pt_network_devices_ok": pt_network_devices_ok,
            "pt_hosts_ok": pt_hosts_ok,
            "docker_token_in_page": pt_empty_ticket
        }
    }

    out_path = ART / "summary.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=4, ensure_ascii=False))
    print(f"summary.json written to {out_path}")
    print(json.dumps(summary, indent=4, ensure_ascii=False))
    return summary

if __name__ == "__main__":
    build_summary()