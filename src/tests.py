import asyncio
import os
from playwright.async_api import async_playwright
from config import AMAZON_URL, EMAIL, PASSWORD, HEADLESS
from logger import setup_logger
from locators import AmazonLocators


class AmazonBot:
    def __init__(self):
        self.logger = setup_logger()
        self.screenshot_folder = "screenshots"
        os.makedirs(self.screenshot_folder, exist_ok=True)

    async def run_test(self):
        self.logger.info("Starting Amazon Bot...")

        async with async_playwright() as p:
            # Persistent context to maintain session
            browser = await p.chromium.launch_persistent_context(
                user_data_dir="./user_data",
                headless=HEADLESS,
                args=["--start-maximized"]
            )
            page = await browser.new_page()

            self.logger.info("Navigating to Amazon homepage...")
            await page.goto(AMAZON_URL, wait_until="domcontentloaded")
            await asyncio.sleep(2)

            try:
                logged_in = await self.is_logged_in(page)
                if not logged_in:
                    await self.login(page)
                else:
                    self.logger.info("Session detected,"
                                     "login is not necessary.")

                await self.navigate_to_tvs(page)
                await self.apply_filter(page)

            except Exception as e:
                self.logger.error(f"Test failed: {e}")
                await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                        "error_general.png"))
            finally:
                self.logger.info("Test completed.")
                await browser.close()

    # -------------------------------------------------------------------------
    # Is_logged_in

    async def is_logged_in(self, page) -> bool:
        try:
            await page.wait_for_selector(AmazonLocators.LOGIN_LINK, timeout=10000)
            login_text = await page.inner_text(AmazonLocators.LOGIN_LINK)

            # If the text does not contain "Identifícate" or "Sign in", user is logged in
            if "identifícate" not in login_text and "Sign in" not in login_text:
                self.logger.info(f"User is logged in: {login_text}")
                return True

            self.logger.info("There is no active session.")
            return False
        except Exception as e:
            self.logger.warning(f"Could not determine login status: {e}")
            return False

    # -------------------------------------------------------------------------
    # Login

    async def login(self, page):
        try:
            self.logger.info("Logining to Amazon account...")
            await page.wait_for_selector(AmazonLocators.LOGIN_LINK, timeout=15000)
            await page.click(AmazonLocators.LOGIN_LINK)

            self.logger.info("Filling in credentials...")
            await asyncio.sleep(2)

            self.logger.info("Waiting for email input...")
            await page.wait_for_selector(AmazonLocators.EMAIL_INPUT, timeout=10000)

            self.logger.info("Filling email...")
            await page.fill(AmazonLocators.EMAIL_INPUT, EMAIL)

            self.logger.info("Clicking continue...")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "00_login_page.png"))
            await asyncio.sleep(2)
            await page.click(AmazonLocators.CONTINUE_BUTTON)

            self.logger.info("Waiting for password input...")
            await asyncio.sleep(2)
            await page.wait_for_selector(AmazonLocators.PASSWORD_INPUT, timeout=10000)

            self.logger.info("Filling password...")
            await page.fill(AmazonLocators.PASSWORD_INPUT, PASSWORD)

            self.logger.info("Clicking sign in...")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "01_filled_credentials.png"))
            await asyncio.sleep(2)
            await page.click(AmazonLocators.SIGN_IN_BUTTON)

            self.logger.info("Login successful.")
        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                    "error_login.png"))
            raise

    # -------------------------------------------------------------------------
    # Navigate to TVs

    async def navigate_to_tvs(self, page):
        self.logger.info("Navigating to TV section...")

        self.logger.info("Opening hamburger menu...")
        await page.wait_for_selector(AmazonLocators.HAMBURGER_MENU, timeout=15000)
        await page.click(AmazonLocators.HAMBURGER_MENU)
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
        await page.click(AmazonLocators.TV_VIDEO_CATEGORY)
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
        await page.click(AmazonLocators.FIFTY_SIX_INCH_FILTER,
                         force=True)  # Added force=True
        self.logger.info("Clicked '56 pulgadas o más' filter.")
        await page.screenshot(path=os.path.join(self.screenshot_folder,
                                                "07_filtered_tvs.png"))

        self.logger.info("Navigated to TV section successfully.")

    # -------------------------------------------------------------------------
    # Apply filter
  
    async def apply_filter(self, page):
           self.logger.info("Applying 56 pulgadas o más...")
        try:
            await page.wait_for_selector("div[data-csa-c-content-id*='size']", timeout=10000)
            filter_element = page.locator('a:has-text("56")')
            await filter_element.first.scroll_into_view_if_needed()
            await filter_element.first.click()
            await page.wait_for_load_state("networkidle")
            await page.screenshot(path=os.path.join(self.screenshot_folder, "03_filter_applied.png"))
            self.logger.info("Filter applyed successfuly.")
        except Exception as e:
            self.logger.error(f" Error applying filter: {e}")
            await page.screenshot(path=os.path.join(self.screenshot_folder, "error_filter.png"))

if __name__ == "__main__":
    test = AmazonBot()
    asyncio.run(test.run_test())
