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

def setup_logger():
    logger = logging.getLogger("AmazonBot")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
