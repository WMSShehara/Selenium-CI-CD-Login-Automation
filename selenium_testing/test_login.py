from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

# Set up the Chrome driver service
service = Service('/usr/local/bin/chromedriver')

# Initialize the Chrome driver with options and service
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://selenium-ci-cd-login-automation.vercel.app/")

try:
    # Wait for the username field to be present
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("suchani")  # Your username

    # Wait for the password field to be present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("password")  # Your password

    # Wait for the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    time.sleep(10)  # Keep the browser open for 10 seconds
finally:
    driver.quit()  # Close the browser after execution
