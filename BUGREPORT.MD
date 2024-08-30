# Bug Reports

## 1. Product Listing Page Bug
- **Title**: Inventory product list with items is displayed with invalid image
- **Severity**: Critical
- **Priority**: High
- **Description**: The inventory page is listing product items with invalid images when tested on both Chrome and Firefox for valid credentials.
- **Steps to Reproduce**:
  1. Navigate to the login page.
  2. Enter valid username as 'problem_user', 'visual_user' and password.
  3. Click on the "Login" button.
- **Expected Result**: User should be displayed with product images.
- **Actual Result**: The image displayed against product items is invalid.

---

## 2. Product Listing Page Bug
- **Title**: Add/Remove cart item button is not working from Inventory page
- **Severity**: Medium
- **Priority**: Medium
- **Description**: Add to cart button and remove button are inconsistent and not working properly for product items when clicked.
- **Steps to Reproduce**:
  1. Navigate to Inventory page using valid user as 'error_user'.
  2. Click add to cart button.
  3. Click remove button.
- **Expected Result**: Add/Remove operations should work for product items in inventory.
- **Actual Result**: Add to Cart/Remove buttons are not responding when clicked.

---

## 3. Filter Options Bug
- **Title**: Filter by price sort items is broken
- **Severity**: Medium
- **Priority**: High
- **Description**: The price filter sort displays a broken error when selecting from the dropdown to sort.
- **Steps to Reproduce**:
  1. Go to the product listing page using valid user as 'error_user'.
  2. Select a price filter from the dropdown.
- **Expected Result**: Products should be displayed within the selected price range.
- **Actual Result**: Error("Sorting is broken! This error has been reported to Backtrace.") is displayed.

---

## 4. UI Display Bug
- **Title**: Checkout button is displayed incorrectly
- **Severity**: Low
- **Priority**: Low
- **Description**: The checkout button is displayed incorrectly on screens.
- **Steps to Reproduce**:
  1. Access the site using a valid user as 'visual_user'.
  2. Navigate to the checkout page.
- **Expected Result**: Button should be properly positioned.
- **Actual Result**: Button is misplaced on the UI.
