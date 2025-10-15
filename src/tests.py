"""
This module contains the AmazonBot class that automates interactions
"""

import asyncio
import os
from playwright.async_api import async_playwright
from .config import AMAZON_URL, HEADLESS_DEFAULT, SCREENSHOT_FOLDER
from .logger import setup_logger
from .locators import AmazonLocators

class AmazonBot:
    """
    A bot that automates the process of logging into Amazon,
    navigating to the TV section, applying a filter, selecting a product,
    adding it to the cart, and proceeding to checkout.

    Credentials are now provided at runtime via API.

    Attributes:
        logger (logging.Logger): Logger for logging messages.
        screenshot_folder (str): Folder to save screenshots.

    Methods:
        run_test(): Main method to run the test sequence.
        is_logged_in(page): Checks if the user is logged in.
        login(page): Logs into the Amazon account.
        navigate_to_tvs(page): Navigates to the TV section.
        select_product(page): Selects a product from the list.
        add_to_cart(page): Adds the selected product to the cart.
        proceed_to_checkout(page): Proceeds to the checkout page.
    """

    def __init__(self, email: str, password: str, headless: bool = HEADLESS_DEFAULT):
        self.email = email
        self.password = password
        self.headless = headless
        self.logger = setup_logger()
        self.screenshot_folder = SCREENSHOT_FOLDER
        os.makedirs(self.screenshot_folder, exist_ok=True)

    async def run_test(self):
        self.logger.info("Starting Amazon Bot...")

        async with async_playwright() as p:
            # Usamos launch() para evitar problemas de Windows + FastAPI
            browser = await p.chromium.launch(
                headless=self.headless,
                args=["--start-maximized", "--no-sandbox"]
            )
            page = await browser.new_page()

            try:
                await page.goto(AMAZON_URL, wait_until="domcontentloaded")
                await asyncio.sleep(2)

                if not await self.is_logged_in(page):
                    await self.login(page)
                else:
                    self.logger.info("Session detected, login not necessary.")

                await self.navigate_to_tvs(page)
                await self.select_product(page)
                await self.add_to_cart(page)
                await self.proceed_to_checkout(page)

            except Exception as e:
                self.logger.error(f"Bot failed: {e}")
                await page.screenshot(path=os.path.join(self.screenshot_folder, "error_general.png"))
            finally:
                await browser.close()
                self.logger.info("Bot finished.")

    # ------------------- Login -------------------

    async def login(self, page):
        """Login to Amazon account using credentials provided via API."""
        try:
            self.logger.info("Logging into Amazon account...")
            await page.wait_for_selector(AmazonLocators.LOGIN_LINK, timeout=15000)
            await page.click(AmazonLocators.LOGIN_LINK)

            self.logger.info("Waiting for email input...")
            await page.wait_for_selector(AmazonLocators.EMAIL_INPUT, timeout=10000)
            await page.fill(AmazonLocators.EMAIL_INPUT, self.email)

            await page.screenshot(path=os.path.join(self.screenshot_folder, "00_login_page.png"))
            await page.click(AmazonLocators.CONTINUE_BUTTON)
            await asyncio.sleep(2)

            self.logger.info("Waiting for password input...")
            await page.wait_for_selector(AmazonLocators.PASSWORD_INPUT, timeout=10000)
            await page.fill(AmazonLocators.PASSWORD_INPUT, self.password)
            await page.screenshot(path=os.path.join(self.screenshot_folder, "01_credentials.png"))
            await page.click(AmazonLocators.SIGN_IN_BUTTON)

            self.logger.info("Login successful.")
        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            await page.screenshot(path=os.path.join(self.screenshot_folder, "error_login.png"))
            raise

    # -------------------------------------------------------------------------
    # Is_logged_in

    async def is_logged_in(self, page) -> bool:
        """
        Verifies if the user is logged in

        :return: True if logged in, False otherwise
        :rtype: bool
        """

        try:
            await page.wait_for_selector(AmazonLocators.LOGIN_LINK,
                                         timeout=10000)
            login_text = await page.inner_text(AmazonLocators.LOGIN_LINK)

            # If the text does not contain "Identifícate" or "Sign in",
            # user is logged in
            if "identifícate" not in login_text and "Sign in" not in login_text:
                self.logger.info(f"User is logged in: {login_text}")
                return True

            self.logger.info("There is no active session.")
            return False
        except Exception as e:
            self.logger.warning(f"Could not determine login status: {e}")
            return False

    # -------------------------------------------------------------------------
    # Navigate to TVs

    async def navigate_to_tvs(self, page):
        """
        Navigates to the TV section on Amazon

        :return: None
        :rtype: None
        """

        self.logger.info("Home page, navigating to TV section...")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "02_home_logged_in.png"))

        self.logger.info("Opening hamburger menu...")
        # force click in HAMBURGER_MENU for overlay issues
        await asyncio.sleep(5)
        await page.click(AmazonLocators.HAMBURGER_MENU, force=True)
        await asyncio.sleep(2)
        self.logger.info("Hamburger menu opened.")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "03_hamburger_menu.png"))

        self.logger.info("Selecting Electronics...")
        await page.wait_for_selector(AmazonLocators.ELECTRONICS_CATEGORY)
        await page.click(AmazonLocators.ELECTRONICS_CATEGORY)
        await asyncio.sleep(2)
        self.logger.info("Electronics category selected.")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "04_electronics_category.png"))

        self.logger.info("Selecting TV & Video...")
        await page.wait_for_selector(AmazonLocators.TV_VIDEO_CATEGORY)
        # force click in case of overlay issues
        await page.click(AmazonLocators.TV_VIDEO_CATEGORY, force=True)
        await asyncio.sleep(2)
        self.logger.info("TV & Video category selected.")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "05_tv_video_category.png"))

        self.logger.info("Selecting TVs...")
        await page.wait_for_selector(AmazonLocators.TVS_CATEGORY)
        await page.click(AmazonLocators.TVS_CATEGORY)
        self.logger.info("TVs category selected.")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "06_tvs_category.png"))

        self.logger.info("Filtering by size: 56 pulgadas o más...")
        await page.wait_for_selector(AmazonLocators.FIFTY_SIX_INCH_FILTER)
        await page.click(AmazonLocators.FIFTY_SIX_INCH_FILTER, force=True)
        self.logger.info("Clicked '56 pulgadas o más' filter.")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "07_filtered_tvs.png"))

        self.logger.info("Navigated to TV section successfully.")

    # -------------------------------------------------------------------------
    # Select first product

    async def select_product(self, page):
        """
        Selects the first product from the list of TVs.

        :param page:
        :return:
        """
        try:
            self.logger.info("Starting product selection...")
            await page.wait_for_selector(AmazonLocators.PRODUCT_ITEM,
                                         timeout=15000)
            await asyncio.sleep(2)
            await page.click(AmazonLocators.PRODUCT_ITEM, force=True)
            self.logger.info("Clicked on product item container.")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "08_product_list.png"))
            self.logger.info("Product selection completed.")
        except Exception as e:
            self.logger.error(f"Failed to select product: {e}")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "select_prod_error.png"))
            raise

    # -------------------------------------------------------------------------
    # Add to cart

    async def add_to_cart(self, page):
        """
        Adds the selected product to the cart.

        :param page:
        :return:
        """

        self.logger.info("Adding product to cart...")
        try:
            await page.wait_for_selector(AmazonLocators.ADD_TO_CART_BUTTON,
                                         timeout=10000)
            await asyncio.sleep(2)
            await page.click(AmazonLocators.ADD_TO_CART_BUTTON, force=True)

            # Assurant popup
            try:
                assurant_btn = await page.wait_for_selector(
                    AmazonLocators.ASSURANT_BUTTON, timeout=3000
                )
                await asyncio.sleep(2)
                await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                        "09_Assurant_popup.png"))
                if assurant_btn:
                    self.logger.info("Assurant coverage popup appeared, skipping...")
                    await page.click(AmazonLocators.ASSURANT_BUTTON)
                    await asyncio.sleep(1)
            except:
                # Si no aparece, continuar normalmente
                self.logger.info("No Assurant popup detected.")
                await page.wait_for_load_state("networkidle")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "10_added_to_cart.png"))
            self.logger.info("Product added to cart successfully.")
        except Exception as e:
            self.logger.error(f"Error adding product to cart: {e}")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "error_add_to_cart.png"))

    # -------------------------------------------------------------------------
    # Proceed to checkout

    async def proceed_to_checkout(self, page):
        """
        Proceeds to the checkout page.

        :param page:
        :return:
        """

        self.logger.info("Proceeding to checkout...")
        try:
            await page.wait_for_selector(AmazonLocators.CART_BUTTON)
            await asyncio.sleep(2)
            await page.click(AmazonLocators.CART_BUTTON)
            self.logger.info("Cart page loaded.")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "11_cart_page.png"))

            self.logger.info("Clicking proceed to checkout...")
            await page.wait_for_selector(
                AmazonLocators.PROCEED_TO_CHECKOUT_BUTTON, timeout=15000)
            await asyncio.sleep(2)
            await page.click(AmazonLocators.PROCEED_TO_CHECKOUT_BUTTON, force=True )
            self.logger.info("Clicked proceed to checkout button.")
            await page.wait_for_load_state("networkidle")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "12_checkout.png"))
            self.logger.info("Proceeded to checkout successfully.")
        except Exception as e:
            self.logger.error(f"Error proceeding to checkout: {e}")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "error_checkout.png"))

#
# if __name__ == "__main__":
#     test = AmazonBot()
#     asyncio.run(test.run_test())
