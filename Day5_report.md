# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Dima Bulguchev
- Group: IB-23-5B
- Token: D1-IB-23-5b-04-5F1C
- Repo: https://github.com/DamnBoi228/devnet-day1-IB-23-5B-Bulguchev

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang
  - artifacts/day5/yang/pyang_version.txt
  - artifacts/day5/yang/pyang_tree.txt
- Screenshot (optional): pyang tree output

## 3) Webex (8.6.7)
- Room title contains token_hash8: Yes
- Message text contains token_hash8: Yes
- Evidence files:
  - me.json / rooms_list.json / room_create.json / message_post.json / messages_list.json

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
  - external_access_check.json / network_devices.json / hosts.json
  - postman_collection.json / postman_environment.json
  - pt_internal_output.txt

## 5) Commands output (paste exact)
{
    "schema_version": "5.0",
    "student": {
        "name": "Bulguchev",
        "group": "IB235B",
        "token_hash8": "b167a8af"
    },
    "checks": {
        "yang_interfaces_in_tree": true,
        "webex_room_title_has_token_hash8": true,
        "pt_empty_ticket_check": true,
        "pt_network_devices_ok": true,
        "pt_hosts_ok": true,
        "docker_token_in_page": true
    }
}
pytest -q
......................                         [100%]
22 passed in 0.65s
## 6) Problems & fixes (at least 1)
- Problem:
- Fix:
- Proof:
...