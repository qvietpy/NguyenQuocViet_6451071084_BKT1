# NguyenQuocViet_6451071084_BKT1

## Mục tiêu

Project kiểm thử tự động E2E Web UI cho chức năng đăng nhập, áp dụng Page Object Model với Selenium WebDriver 4, pytest và báo cáo Excel tự động.

## Website kiểm thử

https://vanphongdientu.utc.edu.vn/Login

## Technologies

- Python 3.11
- Selenium WebDriver 4
- pytest
- openpyxl
- Chrome

## Project Structure

```text
e2e/
  base/
    base_test.py
  pages/
    base_page.py
    login_page.py
  tests/
    test_login_e2e.py
reports/
screenshots/
conftest.py
pytest.ini
requirements.txt
README.md
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Credentials

Không commit thông tin đăng nhập thật. Test đăng nhập thành công đọc biến môi trường:

```cmd
set VALID_USERNAME=your_username
set VALID_PASSWORD=your_password
```

```powershell
$env:VALID_USERNAME="your_username"
$env:VALID_PASSWORD="your_password"
```

Nếu thiếu hoặc sai credentials, testcase TC40 được phép fail theo kết quả thực tế.

## Run tests

Chạy toàn bộ:

```powershell
python -m pytest -v
```

Chạy một test:

```powershell
python -m pytest e2e/tests/test_login_e2e.py::test_tc01_login_page_loads -v
```

Chạy headless:

```powershell
$env:HEADLESS="1"
python -m pytest -v
```

## Reports

Report Excel tự sinh sau mỗi pytest session:

```text
reports/latest_test_report.xlsx
reports/test_report_YYYYMMDD_HHMMSS.xlsx
```

## Screenshots

Screenshot khi test fail được lưu trong:

```text
screenshots/
```

## Git commit strategy

Mục tiêu lịch sử Git: framework commit trước, sau đó mỗi testcase có một commit riêng dạng:

```text
test(TC01): verify login page loads
```
