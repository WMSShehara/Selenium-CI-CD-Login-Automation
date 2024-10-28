from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

# Set up Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

class LoginTests(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver service
        service = Service('/usr/local/bin/chromedriver')
        # Initialize the Chrome driver with options and service
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://selenium-ci-cd-login-automation.vercel.app/")

    # check for invalid login
    def test_invalid_login(self):
        driver = self.driver
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
    
        username_input.send_keys("invalidUser")
        password_input.send_keys("wrongPassword")
    
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
        # Verify error message
        error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "msg"))
    )
        self.assertEqual(error_message.text, "Invalid username or password")
        pass  
        
    # check for empty fields
    def test_empty_fields(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # Check for validation messages
        error_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "msg"))
    )
        self.assertEqual(error_message.text, "Username and password are required")
        pass 

    def test_valid_login(self):
        driver = self.driver
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
    
        username_input.send_keys("admin")
        password_input.send_keys("admin123")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # Wait for the page redirect or success message
        success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "msg"))
    )
        self.assertEqual(success_message.text, "Welcome!")
        pass  

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
