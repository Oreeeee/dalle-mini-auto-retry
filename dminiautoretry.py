# DALLE mini auto retry
# github.com/Oreeeee/dalle-mini-auto-retry

# Import libraries
from selenium.webdriver.common.by import By
from selenium import webdriver
import argparse


# Actual code

def main():
    # Create parser
    parser = argparse.ArgumentParser(description="Automatically retry when DALLE mini throws an error 'Too much traffic'")

    # Add arguments
    parser.add_argument("-b", "--browser", help="Browser that script will use (default: Firefox)", default="firefox")
    parser.add_argument("-l", "--browser-path", help="Path to browser executable if script crashes", default=None)
    parser.add_argument("-q", "--query", help="Text that should be given to AI", required=True ,default=None)
    parser.add_argument("-r", "--retries", help="Max amount of retries (default: 10)", default=10)

    # Parse arguments
    args = parser.parse_args()

if __name__ == "__main__":
    main()