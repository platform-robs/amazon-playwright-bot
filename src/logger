"""
Logger setup for the Amazon bot.

This file configures the logging system used across the bot.
It creates both a file log (saved in the /logs folder) and a
console output so you can track what’s happening in real time.

How it works:
-------------
- Creates a "logs" folder automatically if it doesn’t exist.
- Generates a new log file every time you run the bot.
- Each log entry includes:
    * Timestamp
    * Log level (INFO, ERROR, etc.)
    * Message from the bot

Example log entry:
------------------
2025-10-13 13:45:22 [INFO] Logged into Amazon successfully.

Tip:
----
Use `logger.info()` for regular updates, and
`logger.error()` to record exceptions or failed actions.
"""


import logging
import os

from datetime import datetime


def setup_logger():
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger("AmazonBot")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(
        os.path.join(log_folder, f"amazon_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
        mode='w'
    )
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Console output
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger
