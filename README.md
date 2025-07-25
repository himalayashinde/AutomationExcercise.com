# AutomationExcercise.com

A Python automation suite for the Automation Exercise website.

## Project Overview

This project automates the end-to-end shopping flow of an e-commerce site using Selenium and PyTest, with HTML reporting.

### Features

- **User Authentication:** Automates login and registration flows.
- **Product Search:** Searches for products and validates results.
- **Cart Management:** Adds products to the cart and verifies cart contents.
- **Checkout Process:** Simulates checkout with a mock payment gateway.
- **Order Confirmation:** Verifies order placement and confirmation.

### Highlights

- Uses **Selenium** for browser automation.
- Organized using the **Page Object Model (POM)**.
- Generates **HTML reports** for test results.
- Integrates with **Jenkins** for CI/CD.
- Utilizes **JSON-based test data** for flexibility.

### Bonus (Planned)

- API testing with **Postman** or **Rest Assured** (via Python) may be added in the future if required.

## Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd AutomationExcercise.com
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- To run all tests and generate an HTML report:
  ```bash
  pytest --html=reports/report.html
  ```
- To run a specific test:
  ```bash
  pytest tests/test_sample.py
  ```

## Contributing

- Fork the repository and create a feature branch.
- Add/modify tests in the `tests/` directory.
- Run tests locally before submitting a pull request.

## Troubleshooting

- Ensure ChromeDriver/GeckoDriver is installed and in your PATH.
- Use a virtual environment to avoid dependency conflicts.
