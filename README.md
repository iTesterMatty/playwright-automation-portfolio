# 🎭 Playwright E2E Test Automation Framework

[![Playwright End-to-End Tests](https://github.com/iTesterMatty/playwright-automation-portfolio/actions/workflows/playwright.yml/badge.svg)](https://github.com/iTesterMatty/playwright-automation-portfolio/actions)

A production-ready Web UI automation framework built with **Python**, **Playwright**, and **Pytest**. This repository demonstrates professional test automation architecture, showcasing scalable design patterns, decoupled configurations, and a cloud-integrated Continuous Integration pipeline.

---

## 🏗️ Architecture & Core Features

* **Page Object Model (POM):** Enhances code maintainability and readability by cleanly separating structural UI web locators from functional test logic.
* **Decoupled Configuration:** Manages execution preferences natively via `pytest.ini` and isolates high-priority application credentials using `python-dotenv`.
* **Robust Visual Reporting Engine:** Configured custom hooks via `tests/conftest.py` to intercept execution lifecycles, capturing raw page screenshots on runtime failure and embedding them directly as Base64 strings inside self-contained visual HTML dashboards.
* **Continuous Integration (CI/CD):** Integrated automated **GitHub Actions** cloud workflow pipeline (`playwright.yml`) to orchestrate dependency builds, install headless cross-browser runners, inject vault-encrypted repository secrets, and execute the full regression suite automatically on every code push.

### 🔐 Configuration & Secrets Management

To mirror production-grade security standards, this framework completely decouples environment configuration from the core execution logic:
* **Local Isolation:** Sensitive runtime attributes are managed via local `.env` files. The real `.env` file is strictly decoupled from version control via `.gitignore` to prevent credential leaks.
* **Template Provisioning:** A `.env.example` template is provided to safely demonstrate required keys (`SAUCE_USER`, `SAUCE_PASSWORD`, `BASE_URL`) for local execution readiness.
* **CI/CD Vault Integration:** In the automated cloud pipeline, runtime variables are injected dynamically at execution time utilizing encrypted **GitHub Repository Secrets**. No hardcoded keys ever exist within the codebase.

---

## 🛠️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.12** | Core Programming Language |
| **Playwright** | Next-Generation Web Browser Automation Backend Engine |
| **Pytest** | Technical Testing Framework & Suite Runner |
| **Pytest-HTML** | Interactive Visual Dashboard Test Execution Reporting Plugin |
| **GitHub Actions** | Cloud Integration Execution Pipeline Tool Engine |

---

## 📂 Repository Structure

```text
playwright-automation-portfolio/
├── .github/
│   └── workflows/
│       └── playwright.yml    # GitHub Actions CI/CD pipeline blueprint
├── pages/                    # Page Object Model (POM) layer
│   ├── __init__.py           # Package initialization marker
│   ├── cart_page.py          # Cart actions & element locators
│   ├── checkout_page.py      # Checkout workflow actions & locators
│   ├── inventory_page.py     # Product grid actions & locators
│   └── login_page.py         # Authentication actions & locators
├── tests/                    # Execution test suite layer
│   ├── __init__.py           # Package initialization marker
│   ├── conftest.py          # Global reporting hooks & asset generation
│   └── test_saucedemo.py     # Functional end-to-end automation test cases
├── .env.example              # Sample environment variables configuration template
├── .gitignore                # Restricts reports/ and local environments from version control
├── pytest.ini                # Central framework configurations and default execution flags
└── requirements.txt          # Python dependency mapping
```

## ⚙️ Local Installation & Execution

1. **Clone the repository:**
```bash
git clone https://github.com/iTesterMatty/playwright-automation-portfolio.git
cd playwright-automation-portfolio
```

2. **Setup your virtual environment:**
```bash
pyrhon3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install --with-deps
```

4. **Environment setup:**<br>
Create a `.env` file in the project root directory and declare your target runtime application variables.
Since **Sauce Demo** uses a public sandbox layout, you can safely leverage the public training credentials below:
```plaintext
SAUCE_USER=standard_user
SAUCE_PASSWORD=secret_sauce
BASE_URL=https://www.saucedemo.com/
```

5. **Run the test suite:**
```bash
# Run all tests sequentially
python3 -m pytest tests/

# Run tests in headed UI mode with slow-motion delay
python3 -m pytest --headed --slowmo 1000 tests/
```