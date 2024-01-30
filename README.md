# Selenium Page Object Model with Python

## Test Automation Project
This repository provides a sample Page Object Model (POM) framework for automated web testing using Selenium with Python 3.12 and pytest. The Page Object Model is a design pattern that helps organize and manage web elements in a more modular and maintainable way.

## Prerequisites
Make sure you have the following installed on your machine:

Python 3.12
pip (Python package installer)

## Setup
1. Clone the repository:
```
git clone https://github.com/your-username/selenium-pom-framework.git
```
2.  Activate virtual environmenton Unix or MacOS run:
```
source .venv/bin/activate
```
3. Run Tests
```
pytest /tests/test_base_page.py
```

## Project Structure
Here you can find a short description of main directories and it's content
- [pages](pages) - there are sets of method for each test step (notice: some repeated methods were moved to [functions.py](utils/functions.py))
- [tests](tests) - there are sets of tests for main functionalities of website

```
selenium-pom-framework/
|-- tests/
|   |-- test_sample.py
|-- pages/
|   |-- base_page.py
|   |-- login_page.py
|   |-- home_page.py
|-- locators/
|   |-- login_page_locators.py
|   |-- home_page_locators.py
|-- utils/
|   |-- webdriver_factory.py
|   |-- config_reader.py
|-- conftest.py
|-- pytest.ini
|-- README.md
```