# Leon Chung 2019
# Selenium Practice

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class LeftFormSuccess(unittest.TestCase):
    """Test Case 1
    Filling out all text fields in the left form
    results in a message 'Form filled out successfully'
    """
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.ultimateqa.com/filling-out-forms/")
        self.assertIn("Filling Out Forms - Ultimate QA", driver.title)

        name_field = driver.find_element_by_id("et_pb_contact_name_0")
        message_field = driver.find_element_by_id("et_pb_contact_message_0")

        name_field.send_keys("name")
        message_field.send_keys("here is my message")

        submit_button = driver.find_element_by_class_name("et_pb_contact_submit.et_pb_button")
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message p") ))

        assert "Form filled out successfully" in driver.page_source

        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()