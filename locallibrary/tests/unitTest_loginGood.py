"""Valid admin login should authenticate and show Log out on Local Library."""
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
        # REPLACE with your Local Library admin username/password if different
        user = "testuser"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        try:
            # Successful login shows the Log out button (not a Login link)
            driver.find_element(By.XPATH, "//button[normalize-space()='Log out']")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings="ignore")
