from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver (ensure you have the correct path)
driver = webdriver.Chrome() 
driver.get("https://selenium-ci-cd-login-automation.vercel.app/")  

try:
    # Wait for the username field to be present
    username_input = WebDriverWait(driver, 10).until(
        #find the element by name
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("suchani")  # your username

    # Wait for the password field to be present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("password")  # your password

    # Wait for the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    time.sleep(10)  # Keep the browser open for 10 seconds

finally:
    driver.quit()  #  browser closes after execution
