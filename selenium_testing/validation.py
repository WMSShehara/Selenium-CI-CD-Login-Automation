from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium-ci-cd-login-automation.vercel.app/")

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
        pass  # (Write your valid login test here)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
