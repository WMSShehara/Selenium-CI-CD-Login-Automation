from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options for headless mode
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Prevent permission issues in CI
options.add_argument("--disable-dev-shm-usage")  # Overcome resource limitations
options.add_argument("--remote-debugging-port=9222")  # Useful for debugging if needed

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
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

    time.sleep(10)  # Keep the browser open for 10 seconds (adjust as needed for your testing)
finally:
    driver.quit()  # Close the browser after execution
