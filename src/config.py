"""
Main config file for the Amazon bot.

This file defines global settings that control how the bot behaves,
including the base URL and browser options.

Variables:
-----------
AMAZON_URL : str
    The main Amazon site the bot will work on.

HEADLESS_DEFAULT : bool
    Browser mode:
        - True  -> runs in headless mode (no browser window shown)
        - False -> shows the browser window (useful for debugging or testing)

SCREENSHOT_FOLDER : str
    Folder where screenshots will be saved.

Security note:
--------------
Credentials are now provided dynamically via API. Avoid storing them
in plain text in this file.
"""

AMAZON_URL = "https://www.amazon.com.mx/"
HEADLESS_DEFAULT = True
SCREENSHOT_FOLDER = "screenshots"
