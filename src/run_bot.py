import asyncio
from src.tests import AmazonBot


def get_user_input():
    email = input("Ingresa tu correo de Amazon: ").strip()
    password = input("Ingresa tu contraseña: ").strip()

    mode = ""
    while mode.lower() not in ["headless", "headed"]:
        mode = input("Modo de navegador ('headless' o 'headed'): ").strip()

    headless = True if mode.lower() == "headless" else False
    return email, password, headless


if __name__ == "__main__":
    email, password, headless = get_user_input()
    bot = AmazonBot(email=email, password=password, headless=headless)
    asyncio.run(bot.run_test())
