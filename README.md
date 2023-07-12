# playwright-py
Small POC to assess the capabilities of Playwright with pytest

## Installation
Depending on your system configuration, you might need to run the below commands as superuser
1. `pip install -r requirements.txt` <br>
2. `playwright install`

## Running tests
`pytest -n 3` <br><br>
Where `-n 3` is the number of tests to execute in parallel. <br>
The tests run in headless mode by default. Use `--headed` to run in headed mode
