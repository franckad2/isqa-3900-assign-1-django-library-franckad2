"""Invalid login should not authenticate the user on Local Library."""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "baduser"
        pwd = "wrongpass"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(2)
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        time.sleep(2)
        try:
            # If Log out is present, invalid login incorrectly succeeded
            elements = driver.find_elements(By.XPATH, "//button[normalize-space()='Log out']")
            if elements:
                self.fail("Invalid credentials allowed login")
            # Login link should still be available
            driver.find_element(By.LINK_TEXT, "Login")
            assert True
        except NoSuchElementException:
            self.fail("Expected Login link after failed authentication")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings="ignore")
