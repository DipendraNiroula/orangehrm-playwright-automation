# OrangeHRM Automation Testing with Playwright & Python

An automated test suite built with **Playwright** and **Python** to test the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) HR management web application. The project applies real-world QA practices including the **Page Object Model (POM)**, **data-driven testing** using CSV and JSON, and **Playwright tracing** for debugging.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| Playwright | Browser automation framework |
| Pytest | Test runner |
| pytest-html | HTML test reports |
| CSV / JSON | External data sources for data-driven testing |
| Playwright Tracing | Screenshot & snapshot debugging |

---

## 📁 Project Structure

```
orangehrm-playwright-automation/
│
├── pages/
│   ├── orangehrm_login_page.py   # POM - Login page
│   ├── orange_home.py            # POM - Home page (Performance, Directory)
│   ├── test2_login_orm.py        # POM - Login page (extended)
│   └── test2_home_orm.py         # POM - Home page (Recruitment, Leave, My Info, etc.)
│
├── tests/
│   ├── test_log_orange.py        # Login + navigation using POM
│   ├── test2_log_orm.py          # Extended navigation using POM
│   ├── test2_orm.py              # Navigation flow without POM
│   ├── test_rec1.py              # Recruitment & logout flow   
│   └── test_datadrivendemo.py    # Data-driven login tests (CSV & JSON)
│
├── test_data/
│   ├── data.csv                  # Login credentials (CSV format)
│   └── data.json                 # Login credentials (JSON format)
│
├── conftest.py                   # Pytest fixtures with tracing enabled
├── first_test.py                 # Initial Playwright smoke test
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Project dependencies
├── trace.zip                     # Playwright trace output
└── README.md
```

---

## ✅ Features

### 🏗️ Page Object Model (POM)
Separate page classes keep test code clean and maintainable:

- **`LoginPage`** — handles username, password input and login button
- **`HomePage`** — handles navigation to Dashboard, Recruitment, Vacancies, Leave, My Info, Job, Salary, Maintenance, Performance, and Directory

### 📊 Data-Driven Testing
Login tests run across multiple credential sets using:
- **CSV** (`data.csv`) via Python's `csv.DictReader`
- **JSON** (`data.json`) via `json.load`
- Powered by `@pytest.mark.parametrize`

### 🔍 Playwright Tracing
`conftest.py` captures full trace per test session including screenshots, DOM snapshots, and source — saved to `trace.zip` for post-run debugging.

### 📄 HTML Reports
Auto-generated test reports via `pytest-html`, saved to `reports/report.html`.

---

## 🧪 Test Coverage

| Test File | What It Tests |
|-----------|--------------|
| `test_log_orange.py` | Login with POM + navigate to Directory & Performance |
| `test2_log_orm.py` | Login with POM + navigate to Recruitment, Vacancies, Leave, My Info, Job, Salary, Dashboard, Maintenance |
| `test2_orm.py` | Same navigation flow without POM (raw Playwright) |
| `test_rec1.py` | Login, sidebar navigation, logout, verify login page restored |
| `test_log_orange_copy.py` | Recorded login + Admin/Performance/Directory navigation + logout |
| `test_datadrivendemo.py` | Data-driven login with multiple credentials from JSON/CSV |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/DipendraNiroula/orangehrm-playwright-automation.git
cd orangehrm-playwright-automation

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_log_orange.py

# Run data-driven tests only
pytest tests/test_datadrivendemo.py
```

### Viewing the HTML Report

```bash
# Report is auto-generated at:
reports/report.html
```

### Viewing Playwright Trace

```bash
playwright show-trace trace.zip
```

---

## ⚙️ Configuration

`pytest.ini`:

```ini
[pytest]
addopts = --headed --browser chromium --html=reports/report.html --self-contained-html
testpaths = tests --slowmo=200
```

Tests run in **headed Chromium** with **200ms slow motion** for visibility, and generate a self-contained HTML report.

---

## 📌 Notes

- All tests run against the public OrangeHRM demo: `https://opensource-demo.orangehrmlive.com/`
- Tracing is enabled per session in `conftest.py` and saved to `trace.zip`
- `test_data/` folder must exist with `data.csv` and `data.json` for data-driven tests to run

---

## 👤 Author

**Dipendra Niroula**  
QA Intern | Playwright · Python · Postman · JMeter  
[LinkedIn](https://www.linkedin.com/in/) · [GitHub](https://github.com/DipendraNiroula)