import os
import subprocess
import sys

# Name of the virtual environment
VENV_DIR = "venv"

# Requirements file
REQUIREMENTS_FILE = "requirements.txt"

def create_virtualenv():
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in '{VENV_DIR}'...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print("Virtual environment created successfully.")
    else:
        print(f"The virtual environment '{VENV_DIR}' already exists.")

def install_packages():
    if not os.path.isfile(REQUIREMENTS_FILE):
        print(f"Could not find '{REQUIREMENTS_FILE}'")
        sys.exit(1)

    print("Installing dependencies...")

    pip_executable = os.path.join(VENV_DIR, "Scripts", "pip.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")

    # Install requirements.txt
    subprocess.check_call([pip_executable, "install", "-r", REQUIREMENTS_FILE])

    # Install Playwright
    subprocess.check_call([pip_executable, "install", "playwright"])

    print("Dependencies installed successfully.")

def install_playwright_browsers():
    print("Installing Playwright browsers (Chromium, Firefox, WebKit)...")
    python_executable = os.path.join(VENV_DIR, "Scripts", "python.exe") \
        if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    subprocess.check_call([python_executable, "-m", "playwright", "install"])
    print("Playwright browsers installed successfully.")

def main():
    create_virtualenv()
    install_packages()
    install_playwright_browsers()
    print("All done! The virtual environment is ready with all dependencies installed.")

if __name__ == "__main__":
    main()
