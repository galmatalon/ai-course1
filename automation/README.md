# 🎭 Playwright Automation Testing Framework

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/galmatalon/final-project-61?style=flat-square&logo=github&color=blue)](https://github.com/galmatalon/final-project-61)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square&logo=python)](https://python.org)
[![Pytest](https://img.shields.io/badge/pytest-latest-green?style=flat-square&logo=pytest)](https://pytest.org)
[![Playwright](https://img.shields.io/badge/Playwright-latest-brightgreen?style=flat-square&logo=playwright)](https://playwright.dev)
[![Allure Reports](https://img.shields.io/badge/Allure-Reports-orange?style=flat-square&logo=allure-testops)](https://qameta.io/allure/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-success?style=flat-square)](https://github.com/galmatalon/final-project-61)

**A professional-grade end-to-end automation testing framework built with Playwright and Python.**

[View Project](#) • [GitHub Repository](https://github.com/galmatalon/final-project-61) • [LinkedIn Profile](https://www.linkedin.com/in/gal-matalon/) • [Automation Academy](https://automation.co.il/)

</div>

---

## 📖 Overview

This is a **robust, scalable, and maintainable** test automation framework designed to perform comprehensive end-to-end testing of web applications. Built using **Playwright**, **pytest**, and **Allure Reports**, the framework follows industry best practices including the **Page Object Model (POM)** design pattern, providing clean code architecture and excellent maintainability.

The framework is specifically configured to test **SauceDemo** - a popular e-commerce demo application widely used for QA automation training and validation.

### ✨ Key Highlights

- ✅ **Cross-browser Testing**: Automated tests run seamlessly across Chrome, Firefox, and Safari
- ✅ **Page Object Model (POM)**: Clean separation of test logic and page interactions
- ✅ **Comprehensive Reporting**: Beautiful Allure reports with screenshots and detailed logs
- ✅ **CI/CD Ready**: GitHub Actions integration for automated test execution
- ✅ **Easy Configuration**: Simple INI-based configuration management
- ✅ **Professional Documentation**: This README serves as a complete guide

---

## 🎯 Project Purpose

This project demonstrates **professional-grade test automation practices**:

1. **Quality Assurance**: Validate web application functionality through automated test scenarios
2. **Regression Testing**: Ensure new changes don't break existing functionality
3. **Performance Monitoring**: Track test execution times and identify performance bottlenecks
4. **Learning & Development**: Educational resource for QA automation best practices
5. **CI/CD Integration**: Seamless integration with GitHub Actions for continuous testing

The framework tests real-world scenarios including:
- User authentication
- Product browsing and filtering
- Shopping cart operations
- Checkout processes
- Error handling and validation

---

## 🛠 Technologies & Tools

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.9+ | Programming language |
| **Playwright** | Latest | Cross-browser automation engine |
| **pytest** | Latest | Test framework and runner |
| **pytest-playwright** | Latest | pytest plugin for Playwright |
| **Allure-pytest** | Latest | Test reporting and analytics |
| **GitHub Actions** | Native | CI/CD pipeline automation |

### Dependencies Breakdown

```
playwright      # Browser automation library
pytest          # Testing framework
pytest-playwright  # Playwright + pytest integration
allure-pytest   # Reporting and visualization
```

---

## 📥 Installation & Setup

### Prerequisites

- **Python 3.9 or higher** installed on your system
- **pip** package manager
- **Git** for cloning the repository

### Step 1: Clone the Repository

```bash
git clone https://github.com/galmatalon/final-project-61.git
cd final-project-61
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `playwright` - Browser automation
- `pytest` - Test framework
- `pytest-playwright` - pytest integration
- `allure-pytest` - Report generation

### Step 4: Install Playwright Browsers

```bash
playwright install
```

This downloads the browser binaries needed for automated testing.

### Step 5: Verify Installation

```bash
pytest --version
playwright --version
```

---

## 🚀 Running Tests

### Run All Tests

```bash
pytest
```

**Output**: Tests run in headed mode with 500ms slowdown for better visibility.

### Run Specific Test File

```bash
pytest tests/test_login.py -v
```

### Run Tests with Different Options

```bash
# Show detailed output
pytest -v

# Run with less verbosity
pytest -q

# Run with print statements visible
pytest -s

# Stop after first failure
pytest -x
```

### Run Tests in Specific Browser

```bash
# Chrome (default)
pytest --browser chromium

# Firefox
pytest --browser firefox

# Safari
pytest --browser webkit
```

---

## 📁 Project Structure

```
final-project-61/
├── .github/
│   └── workflows/          # CI/CD pipeline configurations
├── pages/                  # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py       # Base page class with common methods
│   ├── login_page.py      # Login page interactions
│   ├── inventory_page.py  # Product inventory page
│   └── cart_page.py       # Shopping cart page
├── tests/                 # Test cases
│   ├── __init__.py
│   ├── test_login.py      # Login scenario tests
│   ├── test_inventory.py  # Product browsing tests
│   ├── test_cart.py       # Cart operations tests
│   └── conftest.py        # pytest fixtures and configuration
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── config_reader.py   # Configuration management
│   ├── logger.py          # Logging utility
│   └── helpers.py         # Helper functions
├── config.ini             # Application configuration (test URL, credentials)
├── pytest.ini             # pytest configuration
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

### 🗂 Directory Explanation

| Directory | Purpose |
|-----------|---------|
| **pages/** | Page Object Model implementations - each page has its own class |
| **tests/** | Test scripts organized by feature/page |
| **utils/** | Reusable utilities: configuration, logging, helpers |
| **.github/workflows/** | GitHub Actions CI/CD pipeline definitions |

---

## ✅ What Gets Tested

### 1. **Authentication Tests** (`test_login.py`)
- ✓ Valid login with correct credentials
- ✓ Invalid login error handling
- ✓ Required field validation
- ✓ Session management

### 2. **Product Inventory Tests** (`test_inventory.py`)
- ✓ Product list displays correctly
- ✓ Product filtering and sorting
- ✓ Product details accuracy
- ✓ Price display validation
- ✓ Product availability status

### 3. **Shopping Cart Tests** (`test_cart.py`)
- ✓ Add products to cart
- ✓ Remove products from cart
- ✓ Cart quantity updates
- ✓ Cart total calculation
- ✓ Checkout process completion

### 4. **Integration Tests**
- ✓ Complete user journey from login to checkout
- ✓ Multi-step workflows
- ✓ Cross-feature interactions

---

## 📊 Test Reports & Allure Integration

### Generate Allure Report

```bash
# Run tests and generate Allure results
pytest --alluredir=./allure-results

# Serve Allure report locally
allure serve ./allure-results
```

This opens a beautiful interactive report in your browser showing:
- Test execution timeline
- Pass/fail statistics
- Detailed test logs
- Screenshots on failure
- Execution history

### Allure Report Features

- 📈 **Test Statistics**: Pass rate, execution time, trends
- 📸 **Screenshots**: Automatic capture on test failure
- 📝 **Detailed Logs**: Step-by-step test execution details
- 📊 **Graphs & Charts**: Visual representation of results
- 🔗 **Traceability**: Link tests to requirements

---

## 🔗 GitHub Actions & CI/CD Reports

### Continuous Integration Setup

Tests automatically run on:
- Push to main branch
- Pull request creation
- Scheduled daily runs

### View Test Results

1. Go to **Actions** tab in GitHub repository
2. Select the latest workflow run
3. Download test results and Allure reports
4. View detailed execution logs

### CI/CD Pipeline Status

[![GitHub Actions](https://github.com/galmatalon/final-project-61/actions/workflows/tests.yml/badge.svg)](https://github.com/galmatalon/final-project-61/actions)

---

## 🏗 Project Architecture

### Page Object Model (POM)

The framework uses POM design pattern for maintainability:

```python
# pages/login_page.py
class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "input#user-name"
    PASSWORD_INPUT = "input#password"
    LOGIN_BUTTON = "input#login-button"
    
    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
```

### Test Organization

Tests are organized by feature with clear naming:

```python
# tests/test_login.py
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    # Assert successful login
```

### Configuration Management

```ini
# config.ini
[general]
url=https://www.saucedemo.com/
user=gal
password=11111
```

---

## 📋 Configuration Guide

### `config.ini` File

Edit `config.ini` to configure test environment:

```ini
[general]
url=https://www.saucedemo.com/  # Test application URL
user=gal                        # Test user username
password=11111                  # Test user password
```

### `pytest.ini` File

Test execution options:

```ini
[pytest]
addopts = --headed --slowmo 500
```

- `--headed` - Run browser in visible mode (not headless)
- `--slowmo 500` - Add 500ms delay between steps for visibility

### Modify for Your Needs

```bash
# Run tests headless
pytest --headless

# Run tests without slowmo
pytest -o addopts="" 

# Run tests with increased timeout
pytest --timeout=60
```

---

## 🎓 Learning Resources

### Getting Started with Playwright
- [Playwright Official Documentation](https://playwright.dev/python/)
- [Playwright API Reference](https://playwright.dev/python/docs/api/class-playwright)

### pytest Best Practices
- [pytest Documentation](https://docs.pytest.org/)
- [pytest Fixtures Guide](https://docs.pytest.org/en/stable/how-to.html#fixtures)

### Test Automation Concepts
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Test Automation Best Practices](https://automation.co.il/)

---

## 💡 Usage Examples

### Basic Test Example

```python
def test_login_success(page):
    # Navigate to app
    page.goto("https://www.saucedemo.com/")
    
    # Fill login form
    page.fill("input#user-name", "standard_user")
    page.fill("input#password", "secret_sauce")
    
    # Click login
    page.click("input#login-button")
    
    # Assert successful login
    assert "inventory" in page.url
```

### Using Page Objects

```python
def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    # Login
    login_page.login("standard_user", "secret_sauce")
    
    # Add product to cart
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    
    # Assert cart count
    assert inventory_page.get_cart_count() == 1
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'playwright'`
```bash
# Solution: Install playwright
pip install playwright
playwright install
```

**Issue**: Tests run in headless mode when you want to see the browser
```bash
# Check pytest.ini for --headed flag
# Or run with: pytest --headed
```

**Issue**: Allure reports not generating
```bash
# Install allure
pip install allure-pytest

# Generate with correct flag
pytest --alluredir=./allure-results
```

**Issue**: Tests timing out
```bash
# Increase timeout in conftest.py
context = browser.new_context(timeout=60000)
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep tests independent and isolated
- Update README for new features

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| Average Test Execution Time | < 30 seconds per test |
| Browser Load Time | ~2-3 seconds |
| Test Suite Completion | ~2-3 minutes (all tests) |
| Report Generation | ~5-10 seconds |
| CI/CD Pipeline Duration | ~5-10 minutes |

---

## 📞 Support & Contact

### Need Help?

- 🔗 **LinkedIn**: [Gal Matalon](https://www.linkedin.com/in/gal-matalon/)
- 🎓 **Automation Academy**: [automation.co.il](https://automation.co.il/)
- 🐙 **GitHub Issues**: [Report Issues](https://github.com/galmatalon/final-project-61/issues)

### About the Author

This project was created as a demonstration of professional-grade test automation practices and QA excellence. It represents real-world automation scenarios and best practices applicable to any web application testing.

---

## ⭐ Show Your Support

If you found this project helpful:

1. ⭐ **Star this repository** on GitHub
2. 📢 **Share it** with your network
3. 💬 **Provide feedback** and suggestions
4. 🔗 **Connect on LinkedIn** to discuss QA automation

Your support helps maintain and improve this project! 🙌

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Playwright Team** for the excellent browser automation library
- **pytest Community** for the amazing testing framework
- **Allure Framework** for beautiful test reporting
- **SauceDemo** for providing a great test application
- **GitHub Actions** for seamless CI/CD integration

---

<div align="center">

### Made with ❤️ for QA Automation Excellence

**[Visit GitHub](https://github.com/galmatalon/final-project-61)** • **[Connect on LinkedIn](https://www.linkedin.com/in/gal-matalon/)** • **[Learn Automation](https://automation.co.il/)**

Last Updated: September 2026 | Built with Playwright & pytest

</div>
