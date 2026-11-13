# Runs the test suite and opens the Allure report in the browser.
# Any arguments are passed to pytest, e.g.: .\run_tests.ps1 tests\test_login.py
Set-Location $PSScriptRoot
& .\.venv\Scripts\python.exe -m pytest @args
allure serve allure-results
