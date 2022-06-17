# DALLE mini auto retry
# github.com/Oreeeee/dalle-mini-auto-retry

# Import libraries
from cProfile import run
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import argparse


# Actual code
def init_driver(browser, browser_path):
    # Initialize webdriver
    if browser == "firefox":
        if browser_path != None:
            firefox_path = FirefoxBinary(browser_path)
            driver = webdriver.Firefox(firefox_binary=firefox_path)
        else:
            driver = webdriver.Firefox()
    elif browser == "chrome":
        if browser_path != None:
            chrome_path = ChromeOptions()
            chrome_path.binary_location = browser_path
            driver = webdriver.Chrome(chrome_options=chrome_path)
        else:
            driver = webdriver.Chrome()
    else:
        print("Invalid browser")
        exit()

    return driver

def dalle_loop(driver, query, retries):
    # Go to DALLE mini
    driver.get("https://huggingface.co/spaces/dalle-mini/dalle-mini")
    sleep(10)

    # Find input field and run button
    input_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div[1]/div/div/label/input")
    run_button = driver.find_element(By.ID, "8")

    # Enter query
    input_field.send_keys(query)

    # Loop through retries
    for retry in range(retries):
        print("Running!")
        run_button.click()

def main():
    # Create parser
    parser = argparse.ArgumentParser(
        description="Automatically retry when DALLE mini throws an error 'Too much traffic'")

    # Add arguments
    parser.add_argument(
        "-b", "--browser", help="Browser that script will use (default: Firefox)", default="firefox")
    parser.add_argument("-l", "--browser-path",
                        help="Path to browser executable if script crashes", default=None)
    parser.add_argument(
        "-q", "--query", help="Text that should be given to AI", required=True, default=None)
    parser.add_argument("-r", "--retries",
                        help="Max amount of retries (default: 10)", default=10)

    # Parse arguments
    args = parser.parse_args()

    # Initialize webdriver
    driver = init_driver(args.browser, args.browser_path)

    # Run DALLE mini loop
    dalle_loop(driver, args.query, args.retries)


if __name__ == "__main__":
    main()
