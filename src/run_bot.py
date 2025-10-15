# run_bot.py
import asyncio
from src.tests import AmazonBot
from src.config import AMAZON_URL, HEADLESS_DEFAULT, SCREENSHOT_FOLDER

if __name__ == "__main__":
    email = "platform.robs@gmail.com"
    password = "Testing002!"
    headless = True

    bot = AmazonBot(email=email, password=password, headless=headless)
    asyncio.run(bot.run_test())
