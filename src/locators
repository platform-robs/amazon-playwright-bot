"""
Locators for Playwright Amazon bot.

This file stores all the CSS and text-based selectors used by the bot to
interact with Amazon pages. Keeping them in one place makes it easy to
update or fix locators when Amazon changes its layout.

Sections:
----------
1. Login page locators
   - Elements used for signing in (email, password, continue buttons, etc.)

2. Navigation locators
   - Menu and category elements (hamburger menu, electronics, TVs, etc.)

3. Product page locators
   - Product list items and “Add to Cart” button.

4. Cart page locators
   - Elements for accessing the cart and proceeding to checkout.

Tip:
----
If something breaks, Amazon probably changed a selector.
You can inspect the page (right-click → Inspect) and update the locator here.
"""


class AmazonLocators:
    # Login page locators
    LOGIN_LINK = "#nav-link-accountList"
    EMAIL_INPUT = "input#ap_email_login"
    CONTINUE_BUTTON = "input.a-button-input[aria-labelledby='continue-announce']"
    PASSWORD_INPUT = "input#ap_password"
    SIGN_IN_BUTTON = "input#signInSubmit"
    SKIP_PHONE_VERIFICATION_LINK = "a#ap-account-fixup-phone-skip-link"

    # Navigation locators
    HAMBURGER_MENU = 'a#nav-hamburger-menu'
    ELECTRONICS_CATEGORY = 'a.hmenu-item[data-menu-id="11"]'
    TV_VIDEO_CATEGORY = 'a.hmenu-item:has-text("Televisión y Video")'
    TVS_CATEGORY = 'img[alt="Televisiones"]'
    FIFTY_SIX_INCH_FILTER = 'img[alt="56\\" y Más"]'

    # Product page locators
    PRODUCT_ITEM = "a.a-link-normal.s-no-outline"
    ADD_TO_CART_BUTTON = "#add-to-cart-button"

    # Cart page locators
    CART_BUTTON = "#nav-cart"
    PROCEED_TO_CHECKOUT_BUTTON = "#sc-buy-box-ptc-button"
