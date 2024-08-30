1. Product Listing Page Bug
Title: Inventory product list with items is displayed with invalid image
Severity: Critical
Priority: High
Description: The inventory page is listing product items with invalid image when tested on both chrome and firefox for valid credentials.
Steps to Reproduce:
Navigate to the login page.
Enter valid username = 'problem_user', 'visual_user' and password.
Click on the "Login" button.
Expected Result: User should be displayed with product image.
Actual Result: The image displayed against product item is invalid.

2. Product Listing Page Bug
Title: Add/Remove cart item button is not working from Inventory page
Severity: Medium
Priority: Medium
Description: Add items to the cart button and remove button are inconsistent and not working properly for product items when clicked.
Steps to Reproduce:
Navigate to Inventory page using valid user as 'error_user'
Click add to cart button.
Click remove button.
Expected Result: Add/Remove operation should work for product items in inventory.
Actual Result: Add to Cart/Remove buttons are not responding when clicked.

3. Filter Options Bug
Title: Filter by price sort items is broken
Severity: Medium
Priority: High
Description: The price filter sorts displays broken error when selecting from the dropdown to sort.
Steps to Reproduce:
Go to the product listing page using valid user as 'error_user'.
Select a price filter from dropdown.
Expected Result: Products should be displayed within the selected price range.
Actual Result: Error("Sorting is broken! This error has been reported to Backtrace.") is displayed.

4. UI Display Bug
Title: Checkout button is displayed incorrectly
Severity: Low
Priority: Low
Description: The checkout button is displayed incorrectly on screens.
Steps to Reproduce:
Access the site using valid user as 'visual_user'.
Navigate to the checkout page.
Expected Result: Button should be properly positioned.
Actual Result: Button is misplaced on the UI.
