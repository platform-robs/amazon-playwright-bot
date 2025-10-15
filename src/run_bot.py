import asyncio
from .tests import AmazonBot

async def main():
    email = "tucorreo@gmail.com"
    password = "TuPassword123"
    headless = False  # True = headless, False = se ve el navegador

    bot = AmazonBot(email=email, password=password, headless=headless)
    await bot.run_test()

if __name__ == "__main__":
    asyncio.run(main())
