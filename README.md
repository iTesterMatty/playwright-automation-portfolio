# Playwright & Pytest Automation Portfolio

A professional-grade test automation framework built to demonstrate scalable, robust web application testing using Python, Playwright, and the Pytest framework. 

This project transitions from isolated sandboxes to realistic e-commerce simulation environments, utilizing advanced selector strategies, locator chaining, and asynchronous execution principles.

## 🚀 Key Framework Features
* **User-Centric Locators:** Prioritizes accessibility-focused targeting (`get_by_role`, `get_by_placeholder`) over fragile CSS selectors.
* **Strictness & Isolation Scoping:** Implements strict locator chaining to eliminate multi-element collisions and flaky test execution.
* **Modern Project Architecture:** Clean separation of concerns with isolated test structures and robust execution dependencies.

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3
* **Test Runner:** Pytest
* **Automation Engine:** Playwright (Python Integration)
* **Environment:** Containerized Linux (Fedora / Ubuntu Development Stack)

## 📁 Repository Structure
```text
playwright_learning/
├── tests/
│   ├── test_todo.py          # Multi-step lifecycle, hover, and filter test cases
│   └── test_saucedemo.py     # E-commerce login and dynamic cart validation
├── .gitignore                # Optimized version control exclusions
├── requirements.txt          # Python project dependencies
└── README.md                 # Project portfolio documentation
```

## ⚙️ Local Installation & Execution

1. **Clone the repository:**
```bash
git clone (https://github.com/iTesterMatty/playwright-automation-portfolio.git)
cd playwright-automation-portfolio
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install
```

3. **Run the test suite:**
```bash
# Run all tests sequentially
python3 -m pytest tests/
# Run tests in headed UI mode with slow-motion delay
python3 -m pytest tests/ --headed --slowmo 1000
```

