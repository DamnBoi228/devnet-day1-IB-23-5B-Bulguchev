# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Bulguchev Dima
- Group: IB-23-5B
- Token: D1-IB-23-5b-04-5F1C
- Repo: https://github.com/DamnBoi228/devnet-day1-IB-23-5B-Bulguchev

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: Yes
- artifacts/day4/docker/sampleapp_token_proof.txt: Yes
- artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
- artifacts/day4/docker/ sampleapp_build_log.txt:Yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt:No
- artifacts/day4/jenkins/buildapp_console.txt:No
- artifacts/day4/jenkins/testapp_console.txt:No
- artifacts/day4/jenkins/pipeline_script.groovy: No
- artifacts/day4/jenkins/pipeline_console.txt:No
- artifacts/day4/jenkins/jenkins_url.txt:No

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt:Yes
- artifacts/day4/ansible/ansible_hello.txt:Yes
- artifacts/day4/ansible/ansible_playbook_install.txt: Yes
- artifacts/day4/ansible/ports_conf_after.txt:Yes
- artifacts/day4/ansible/curl_apache_8081.txt:Yes

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt:Yes
- artifacts/day4/security/login_v1.txt:Yes
- artifacts/day4/security/signup_v2.txt:Yes
- artifacts/day4/security/login_v2.txt:Yes
- artifacts/day4/security/db_tables.txt:Yes
- artifacts/day4/security/db_user_hash_sample.txt:Yes

## 3) Commands output
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-20T14:25:04.476963+00:00",
  "student": {
    "token": "D1-IB-23-5b-04-5F1C",
    "token_hash8": "b167a8af",
    "name": "Bulguchev",
    "group": "IB235B"
  },
  "checks": {
    "docker_token_in_page": false,
    "docker_tokenproof": false,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": false,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "26bd24cb008243a68cf645c072a049b4580ec87b60c3ef7d8f4f96de8e9a8c33",
    "docker_ps": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "docker_build_log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "docker_token_proof": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "jenkins_docker_ps": "b46330ae850f844cee9eddedefa65380a5d5d035a5e1f33231ae44c36f2c303b",
    "buildapp_console": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "testapp_console": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "pipeline_script": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "pipeline_console": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "jenkins_url": "185f195598830dbc315eb3a6741f97eace245e9d9d2a7225c5da77b87f27f3fc",
    "ansible_ping": "005e9245df2c530d64aee6bfec751dfc3ced4b06361f597e7fde4163bc44fd69",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "780a930fdc01318e3b45c474d7947b8716a2433723aa3db9c981cff178781583",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "signup_v1": "160934e5410a09ae8dd40d9b6a30ea3756117baff90c2f6019001abf1d8a00dc",
    "login_v1": "ca4a8106e4f4e2e44db1811ff469acfcda6d7bade5199678ee4ef28b39e54712",
    "signup_v2": "11e017aa8ec99930fcf69f014e79c312ffd5c36e8357fad8ecd8a30cd5af73be",
    "login_v2": "a64859c97b01971cc99e033f06924e17c92f3f19bcd5f7b92d70b33bcb3b583d",
    "db_tables": "a6b72f95fe1f1775bb24bb8c5d5b49e05152f31acab0b426a684c0c28d51ce6f",
    "db_user_hash_sample": "8c68d04d8bddadf80ae05ddda4c0fa7d42b9626fb1e63beb0d62b36505bbe3d6"
  },
  "validation_passed": false,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}

...F                                           [100%]
====================== FAILURES ======================
______ test_day4_summary_and_required_evidence _______

    def test_day4_summary_and_required_evidence():
        env = os.environ.copy()
        assert env.get("STUDENT_TOKEN")
        assert env.get("STUDENT_NAME")
        assert env.get("STUDENT_GROUP")
    
        r = subprocess.run(["python", "src/day4_summary_builder.py"], cwd=str(ROOT), env=env, capture_output=True, text=True)
        assert r.returncode in (0, 2), r.stderr
    
        assert (ART / "summary.json").exists()
        summary = jload(ART / "summary.json")
        schema = jload(SCHEMA)
        jsonschema.validate(instance=summary, schema=schema)
    
        # сильные проверки
>       assert summary["checks"]["docker_token_in_page"] is True
E       assert False is True

tests/test_day4_labs.py:27: AssertionError
============== short test summary info ===============
FAILED tests/test_day4_labs.py::test_day4_summary_and_required_evidence - assert False is True
1 failed, 3 passed in 0.95s
## 4) Short reflection (5–8 lines)
- What was the hardest part today and why?
- One security mistake you avoided (or made and fixed):

## 5) Problems & fixes (at least 1)
- Problem:
- Fix:
- Proof:
...