"""
Main config file for the Amazon bot.

This file defines global settings that control how the bot behaves,
including login credentials, base URL, and browser options.

Variables:
-----------
AMAZON_URL : str
    The main Amazon site the bot will work on.

EMAIL : str
    Your Amazon account email. Used for login.

PASSWORD : str
    The password for the account above.

HEADLESS : bool
    Browser mode:
        - True  -> runs in headless mode (no browser window shown)
        - False -> shows the browser window (useful for debugging or testing)

Security note:
--------------
Avoid storing real credentials in plain text.
Use environment variables or a .env file instead, especially in production.
"""


AMAZON_URL = "https://www.amazon.com.mx/"
EMAIL = "platform.robs@gmail.com"
PASSWORD = "Testing002!"
HEADLESS = True
