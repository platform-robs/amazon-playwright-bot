import os
import subprocess
import sys

# Name of the virtual environment
VENV_DIR = "venv"

# Requirements file
REQUIREMENTS_FILE = "requirements.txt"

def create_virtualenv():
    """
    Create the virtual environment if it doesn't exist.

    rtype: None
    return: None
    """

    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in '{VENV_DIR}'...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print("Virtual environment created successfully.")
    else:
        print(f"The virtual environment '{VENV_DIR}' already exists.")

def install_packages():
    """
    Install dependencies from requirements.txt using the venv's pip.

    rtype: None
    return: None
    """

    if not os.path.isfile(REQUIREMENTS_FILE):
        print(f"Could not find '{REQUIREMENTS_FILE}'")
        sys.exit(1)

    print("Installing dependencies...")

    # Detect the correct pip path depending on the operating system
    pip_executable = os.path.join(VENV_DIR, "Scripts", "pip.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")

    # Safely install dependencies
    subprocess.check_call([pip_executable, "install", "-r", REQUIREMENTS_FILE])
    print("Dependencies installed successfully.")

def main():
    create_virtualenv()
    install_packages()
    print("All done! The virtual environment is ready with all dependencies installed.")

if __name__ == "__main__":
    main()
