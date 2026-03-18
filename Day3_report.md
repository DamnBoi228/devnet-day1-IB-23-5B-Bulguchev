# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Bulguchev Dima
- Group: IB-23-5B
- Token: D1-IB-23-5b-04-5F1C
- Repo: https://github.com/DamnBoi228/devnet-day1-IB-23-5B-Bulguchev

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots: [list]
- Postman screenshots: [list]
- Python run screenshot: [list]

## 3) Artifacts checklist
- artifacts/day3/books_before.json: Yes
- artifacts/day3/books_sorted_isbn.json: Yes
- artifacts/day3/mybook_post.json: Yes
- artifacts/day3/books_by_me.json: Yes
- artifacts/day3/add100_report.json: Yes
- artifacts/day3/postman_collection.json: Yes
- artifacts/day3/postman_environment.json: Yes
- artifacts/day3/curl_get_books.txt: Yes/
- artifacts/day3/curl_get_books_isbn.txt: Yes
- artifacts/day3/curl_get_books_sorted.txt: Yes
- artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
python src/day3_library_lab.py --count 100
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-18T15:44:33.629720+00:00",
  "student": {
    "token": "D1-IB-23-5b-04-5F1C",
    "token_hash8": "b167a8af",
    "name": "Bulguchev",
    "group": "IB235B"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "537ae377e146dd5e4e566ac49ca9561c99a83f9f8fb54015cd160619a16f01a0",
    "books_sorted_isbn": "f925fd1050e36611a71faae521c9a591f3b0b678c21f39a5a702db1d052968b0",
    "mybook_post": "7161ed693e1a7530f6080de2f96f7eb3cea8cdb950e9eba289d400fe32f36f7d",
    "books_by_me": "1d150b0c0ef7038afc7c35af2df2a120fa3b337c8cf0c6f36fb38250fb4b9d24",
    "add100_report": "d368559ec3b13471f8b96001863714de78ba239adf50259aad9fff18d9311cc5",
    "postman_collection": "",
    "postman_environment": "",
    "curl_get_books": "de64bae22fde03848fbeb14e2a6c661cf7e9eed12f29b574d596224bf5bf6bf9",
    "curl_get_books_isbn": "ee1093008a5d89a75d9aaf8a2c8a7987c8841bce0c4028d02d32e78f083fb227",
    "curl_get_books_sorted": ""
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}

### 4.2 Tests
```text
pytest -q
```

## 5) Problems & fixes (at least 1)
- Problem:
- Fix:
- Proof:
...