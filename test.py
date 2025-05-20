import selenium
from selenium import webdriver
import sys
import os

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
if not EMAIL or not PASSWORD:
    print("Please set the EMAIL and PASSWORD environment variables.")
    sys.exit(1)

LOGIN_URL = "https://mon-vie-via.businessfrance.fr/?nav=profile"

def login(driver, email, password):
    driver.get(LOGIN_URL)
    driver.implicitly_wait(10)  # Wait for the page to load

    # Find and fill the email field
    email_field = driver.find_element("name", "email")
    email_field.send_keys(email)

    # Find and fill the password field
    password_field = driver.find_element("name", "password")
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()

    # Wait for the page to load after login
    driver.implicitly_wait(10)

def main():
    # Set up the WebDriver (make sure to have the appropriate driver installed)
    driver = webdriver.Chrome()  # or use webdriver.Firefox() for Firefox

    try:
        login(driver, EMAIL, PASSWORD)
        print("Login successful!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()