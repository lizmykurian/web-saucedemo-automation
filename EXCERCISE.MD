# Activity 1:

TEST STRATEGY

# Introduction

This test strategy outlines the approach, tools, and processes that will be used to ensure the quality of the SauceDemo e-commerce application. The application includes various features such as login, product search, filtering, product listing, product details, cart, and checkout. The primary objective is to validate that these features function correctly and meet the requirements

# Objectives

The testing will be performed on Saucelab Demo ecommerce website to:
    -   Ensure that the login functionality is secure and user authentication works as expected.
    -   Validate that filtering options correctly refine product listings.
    -   Confirm that the product listing page displays the correct items with accurate details.
    -   Check that the product details page provides all necessary information and allows adding items to the cart.
    -   Ensure that the cart functions correctly, including adding, updating, and removing items.
    -   Validate that the checkout process is smooth and processes orders correctly.

# Scope

	-   Login
	-   Filtering
	-   Product Listing Page
	-   Product Details Page
    -   Cart
    -   Checkout


# Testing Types

The following testing types will be performed during the testing of the Saucelab Demo ecommerce web application:

## Functional Testing
    -   Login/Logout: Verify succesfull login and logout of users.
    -   Product Filtering: Ensure products can be filtered correctly.
    -   Product Listing Page: Check the inventory for proper listing of products.
    -   Product Details Page: Confirm the product details page works as expected.
    -   Cart: Test adding, removing, and updating items in the cart.
    -   Checkout: Validate the entire checkout process, including payment and order confirmation.
## Integration Testing
    -   Test the interactions between the login module and the user account module.
    -   Validate the integration between the product catalog, shopping cart, and checkout process.
    -   Ensure that third-party services are correctly integrated.
## End to End Testing
    -   Test end to end real user scenarios, such as logging in, searching for a product, adding it to the cart, proceeding to checkout, and completing the order.
    -   Verify the complete user journey, ensuring all components work together smoothly.
## Regression Testing
    -   Ensure existing functionalities are not affected with any new change. 
## User Acceptance Testing
    -   Test involving real users to ensure application meets user expectations and is ready for production deployment.
## Non-Functional Testing
    -   Assess the application’s load time, response time, and scalability.
    -   Test for security vulnerabilities.
## Compatibility Testing
    -   Verify that the application performs consistently across different browsers and platforms.

# Test Approach

The testing will be conducted using both manual and automated testing approaches.

    -   Manual Testing: Exploratory testing and user acceptance testing (UAT) will be carried out to discover potential issues that automated tests might miss.
    -   Automated Testing: Regression tests, smoke tests, and functional tests will be automated using Selenium with the pytest framework.

##	Test Planning:
    -	Define test objectives, scope, and resources.
    -	Prepare test cases based on functional requirements and user stories.
    -	Develop a test schedule and assign responsibilities.
##	Test Execution:
    -	Perform manual and automated tests as per the test cases.
    -	Use automation tools like Selenium for repetitive tasks and regression tests.
##	Defect Management:
    -	Log defects in a tracking system (e.g., JIRA).
    -	Categorize and prioritize defects based on severity and impact.
    -	Work with developers to resolve defects and retest as necessary.
##	Reporting:
    -	Prepare test reports summarizing test results, defects, and coverage.
    -	Communicate findings and recommendations to stakeholders.

# Tools and Resources

    -   Programming Language: Python
    -   Testing Framework: pytest 
    -   Automation Tool: Selenium WebDriver
    -   Assertion Library: pytest 
    -   Reporting Tool: pytest-html for HTML reports, Allure for more advanced reporting
    -   Test Management: TestRail
    -   Defect Tracking: JIRA or Clickup
    -   Continuous Integration (CI): Jenkins, GitHub Actions, or GitLab CI
    -   Version Control: Git

# Test Plan

## Test Cases

### Test Case Login

### Test Case 1: Successful Login

Objective: Verify that a user can successfully log in with valid credentials.
Preconditions: User is on the login page.
Steps:
1. Enter a valid username.
2. Enter a valid password.
3. Click the "Login" button.
Expected Result: User is redirected to the product listing page.

### Test Case 2: Login with Invalid Credentials

Objective: Verify that login fails with invalid credentials.
Preconditions: User is on the login page.
Steps:
1. Enter an invalid username or password.
2. Click the "Login" button.
Expected Result: User sees an error message indicating invalid credentials.

### Test Case 3: Login with Empty Fields

Objective: Verify that login fails when username or password fields are left empty.
Preconditions: User is on the login page.
Steps:
1. Leave the username and/or password field empty.
2. Click the "Login" button.
Expected Result: User sees an error message indicating that fields cannot be empty.


### Test Case Filtering
### Test Case 1: 
Objective: Verify that inventory page loads.
Preconditions: User is on the login Page.
Steps:
1. Enter a valid username.
2. Enter a valid password.
3. Click the "Login" button.
4. Land in Inventory Page
Expected Result: User is displayed with product listing.

### Test Case 2: 
Objective: Verify that user is able to filter for price low-to-high.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click filter drop down
3. Select low-to-high from dropdown
Expected Result: User is displayed with product listing sorted from price low-to-high.

### Test Case 3: 
Objective: Verify that user is able to filter for price high-to-low.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click filter drop down
3. Select low-to-high from dropdown
Expected Result: User is displayed with product listing sorted from price high-to-low.

### Test Case Product Listing Page

### Test Case 1: 
Objective: Verify that user is able to add to cart from product list.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click add to cart to add item
Expected Result: User is able to add item to cart.

### Test Case 2: 
Objective: Verify that user is able to add to cart from product list.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click add to cart to add item
3. Click remove from cart to remove item
Expected Result: User is able to remove item from cart.

### Test Case Product Details Page

### Test Case 1: 
Objective: Verify that product details page loads.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click a product
Expected Result: User is redirected to product details page.

### Test Case 2: 
Objective: Verify that user is able to add to cart from product details page.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click a product
3. Land in product details page
4. Click add to cart to add item
Expected Result: User is able to add item to cart.

### Test Case 3: 
Objective: Verify that user is able to add to cart from product details page.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click a product
3. Land in product details page
4. Click add to cart to add item
5. Click remove from cart to remove item
Expected Result: User is able to remove item from cart.

### Test Case Cart
### Test Case 1: 
Objective: Verify that user is able to see the cart items.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click on cart
3. Land in cart page
Expected Result: User is able to view items in cart.

### Test Case 2: 
Objective: Verify that user is able to checkout cart items.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click a product
3. Land in cart page
4. Click checkout button
Expected Result: User is able to land in checkout page.

### Test Case Checkout

### Test Case 1: 
Objective: Verify that user is able to proceed to the checkout overview.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click a product
3. Land in cart page
4. Click checkout button
5. Land in checkout information page
6. Fill in details
7. Click continue
Expected Result: User is able to land in the checkout overview page.

### Test Case 2: 
Objective: Verify that user is able to complete the checkout.
Preconditions: User is on the Inventory Page.
Steps:
1. Navigate to the inventory page
2. Click a product
3. Land in cart page
4. Click checkout button
5. Land in checkout information page
6. Fill in details
7. Click continue
8. Click finish
Expected Result: User is able to finish the checkout process.


## Test Data

Valid Username: standard_user
Valid Password: secret_sauce

Invalid Username: invalid_user
Invalid Password: invalid_sauce

## Automation Plan

    -  Create a Page Object Model (POM) for the each page to encapsulate the elements and actions.
    -  Automate the test cases using Selenium and pytest.
    -  Store test data in separate configuration files.
    -  Use pytest fixtures for setup and teardown activities, such as opening and closing the browser.
    -  Implement logging to capture detailed test execution results.

## Reporting

    -  Generate HTML test reports using pytest-html.

## CI/CD Integration

    -  Configure Github Actions to trigger test runs after each code commit.

## Risk and Mitigation
    -  Risk: Flaky tests due to unstable web elements.
       Mitigation: Use explicit waits to handle timing issues.
    -  Risk: Changes in the application UI may break tests.
       Mitigation: Regularly update the test scripts and maintain good communication with the development team.

## Continuous Improvement
    -	Gather feedback from test cycles
    -	Analyze test results and defect trends to improve testing processes.
    -	Update test cases and strategies based on new features or changes in requirements.       

## Exit Criteria
    -  All critical and high-priority test cases are executed.
    -  No critical or high-priority defects remain open.
    -  Test coverage for automated regression tests is at least 80%.

# Conclusion
This test strategy provides a comprehensive approach to testing the SauceDemo e-commerce application. By combining manual and automated testing, we aim to ensure a high level of quality and user satisfaction.