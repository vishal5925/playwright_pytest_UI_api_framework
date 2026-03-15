# playwright_pytest_UI_api_framework
complete framework to support playwright ui &amp; api automation using pytest  

# Playwright + Pytest Automation Framework (UI + API)

## Overview

This project is a scalable **test automation framework** built using **Playwright and Pytest** for testing both **Web UI and REST APIs**.
The framework follows industry best practices including **Page Object Model (POM)**, **data-driven testing**, **parallel execution**, and **CI/CD integration**.

The framework is designed to be easily integrated with **CI/CD pipelines** and can run across multiple environments.

---

# Key Features

* UI Automation using Playwright
* API Automation using Requests library
* Page Object Model (POM) design pattern
* Parallel test execution
* Pytest fixtures for reusable setup
* HTML / Allure reporting
* Environment configuration support
* CI/CD ready (Jenkins / GoCD / GitHub Actions)
* Cross-browser testing support
* Logging and reporting integration

---

# Tech Stack

* Python
* Playwright
* Pytest
* Requests (API testing)
* Allure Reporting
* Git
* CI/CD Integration

---

# Project Structure

```
project-root
│
├── tests
│   ├── ui
│   │   └── test_login.py
│   │
│   └── api
│       └── test_user_api.py
│
├── pages
│   └── login_page.py
│
├── api
│   └── user_api.py
│
├── utils
│   ├── config_reader.py
│   └── logger.py
│
├── testdata
│   └── test_data.json
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/playwright-automation-framework.git
```

Navigate to project directory

```
cd playwright-automation-framework
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Install Playwright browsers

```
playwright install
```

---

# Running Tests

Run all tests

```
pytest
```

Run UI tests

```
pytest tests/ui
```

Run API tests

```
pytest tests/api
```

Run tests in parallel

```
pytest -n 4
```

Run tests with verbose logs

```
pytest -v
```

---

# Test Reports

Generate Allure results

```
pytest --alluredir=allure-results
```

Generate report

```
allure serve allure-results
```

Reports include

* Test execution summary
* Passed / Failed test details
* Logs and screenshots
* Execution time

---

# Framework Design

The framework follows **Page Object Model (POM)** which separates test logic from page interactions.

Benefits

* Improved code maintainability
* Reusable page methods
* Reduced test duplication

Example

```
login_page.enter_username()
login_page.enter_password()
login_page.click_login()
```

---

# API Automation

API tests are implemented using the **Requests library**.

Features

* Reusable API client
* JSON response validation
* Schema validation support
* API response time validation

Example

```
response = requests.get("/users")
assert response.status_code == 200
```

---

# Logging

The framework includes logging support to capture:

* Test execution steps
* Errors
* API responses
* Debug information

Logs are stored in the **logs** folder.

---

# CI/CD Integration

This framework can be integrated with:

* Jenkins
* GoCD
* GitHub Actions
* GitLab CI

Typical pipeline steps

1. Checkout code
2. Install dependencies
3. Install browsers
4. Run pytest
5. Publish reports

---

# Best Practices Followed

* Page Object Model
* Reusable fixtures
* Data-driven testing
* Clean test architecture
* Separation of UI and API layers
* Environment-based configuration

---

# Future Enhancements

* Docker integration
* Cloud execution (BrowserStack / Sauce Labs)
* AI-based self-healing locators
* Test analytics dashboard

---

# Author

QA Automation Framework designed for scalable **UI and API automation testing** using modern tools and best practices.
