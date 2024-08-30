# SauceDemo Automation Testing

This project contains automated tests for the SauceDemo e-commerce website using Python, Selenium WebDriver, and pytest. The tests include scenarios for valid login, invalid login, and login with empty fields.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Viewing Reports](#viewing-reports)
- [Project Structure](#project-structure)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8+
- pip (Python package manager)
- Google Chrome and/or Mozilla Firefox (depending on the browsers you want to test)
- Allure CLI (if you wish to generate and view Allure reports)

## Installation

1. **Clone the Repository**:

   https://github.com/lizmykurian/web-saucedemo-automation.git
   cd web-saucedemo-automation

2. **Install Dependencies**:

Install the required Python packages:

   pip install -r requirements.txt

## Running the Tests

1. **Set Up Environment Variables**:

You can configure the browsers and other settings in a .env file:

BASE_URL=https://www.saucedemo.com/
BROWSERS=chrome,firefox
USERNAME=standard_user
PASSWORD=secret_sauce

2. **Run the Tests**:

Run the tests using pytest:

    pytest --html=report.html --self-contained-html --alluredir=allure-results
 
## Viewing Reports

1. **HTML Report**:

Open the report.html file in your web browser to view the test results.

2. **Allure Report**:

To view the Allure report, run the following command:

    allure serve allure-results

## Project Structure

saucedemo-automation/
│
├── common/
│   └── browser_manager.py  # Manages browser configuration and driver setup
│
├── pages/
|   |── cart_page.py        # Page Object for the cart page
|   |── check_out_page.py   # Page Object for the checkout page
|   |── inventory_page.py   # Page Object for the inventory page
│   ├── login_page.py       # Page Object for the login page
│   |── product_details_page.py # Page Object for the product details page
|   |── product_listing_page.py # Page Object for the product listing page
│
├── tests/
|   |── test_cart.py        # Test cases for cart functionality
|   |── test_checkout.py    # Test cases for checkout functionality
|   |── test_inventory.py   # Test cases for inventory functionality
│   ├── test_login.py       # Test cases for login functionality
│   |── test_product_details.py # Test cases for product details functionality
|   |── test_product_list.py # Test cases for product list functionality
│
├── requirements.txt        # List of dependencies
├── .env                    # Environment configuration
├── test_data.json          # Test data file
├── BUGREPORT.md            # Bug report file
├── EXCERCISE.md            # Excercise file outlining test strategy and plan 
└── README.md               # Instructions on how to set up and run the project

## Notes

1. **Cross-Browser Testing**: 
The tests are configured to run on multiple browsers (Chrome, Firefox) as specified in the .env file.
2. **Test Data**: 
The login credentials and other test data are stored in the test_data.json file.
3. **Error Handling**: 
The test cases include scenarios for valid, invalid, and empty credentials with appropriate assertions.
