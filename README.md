# Playwright Test Automation

Ecommerce website tests written with playwright.

## Contains:
- Playwright (Python) + pytest test suite
- Page Object Model (POM) implementation under `pages/`
- Tests for Login, Cart, Checkout, Search (using SauceDemo)
- `conftest.py` with reusable fixtures and CLI options
- GitHub Actions CI workflow
- Clear README with run instructions

## Setup (local)
1. Create & activate a virtualenv (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # mac / linux
   .venv\Scripts\activate    # windows
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers (required)
   ```bash
   playwright install
   ```

## Run tests
- Headless (default):
  ```bash
  pytest -q
  ```
- With browser visible (headed):
  ```bash
  pytest -q --headed
  ```
- Select browser (chromium, firefox, webkit):
  ```bash
  pytest -q --browser=firefox
  ```

## Project structure
```
playwright-portfolio/
├── pages/                # Page Objects (POM)
├── tests/                # pytest tests using Playwright
├── .github/workflows/ci.yml  # CI workflow using Playwright
├── conftest.py           # fixtures & CLI options
├── requirements.txt
└── README.md
```
