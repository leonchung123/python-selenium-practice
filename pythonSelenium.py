# Leon Chung 2019
# Selenium Practice

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

SLEEP_TIME = 2 # in seconds

# Test Scenario 1 - A user fills out the left form
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

        time.sleep(SLEEP_TIME)

    def tearDown(self):
        self.driver.close()


class LeftFormNoName(unittest.TestCase):
    """Test Case 2
    Filling out all text fields in the left form except the name text field
    results in an error message asking the user to enter a name in the name text field.
    """
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.ultimateqa.com/filling-out-forms/")
        self.assertIn("Filling Out Forms - Ultimate QA", driver.title)

        message_field = driver.find_element_by_id("et_pb_contact_message_0")

        message_field.send_keys("here is my message")

        submit_button = driver.find_element_by_class_name("et_pb_contact_submit.et_pb_button")
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message p") ))

        assert "Please, fill in the following fields:" in driver.page_source
        # check that a <li> element in the div with class name 'et-pb-contact-message' contains the text 'Name'
        assert check_exists_by_xpath(driver, "//div[contains(@class, 'et-pb-contact-message') and contains(.//li, 'Name')]")

        time.sleep(SLEEP_TIME)

    def tearDown(self):
        self.driver.close()

class LeftFormNoMessage(unittest.TestCase):
    """Test Case 3
    Filling out all text fields in the left form except the message text field
    results in an error message asking the user to enter a message in the message text field.
    """
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.ultimateqa.com/filling-out-forms/")
        self.assertIn("Filling Out Forms - Ultimate QA", driver.title)

        name_field = driver.find_element_by_id("et_pb_contact_name_0")
        name_field.send_keys("name")

        submit_button = driver.find_element_by_class_name("et_pb_contact_submit.et_pb_button")
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".et-pb-contact-message p") ))

        assert "Please, fill in the following fields:" in driver.page_source
        # check that a <li> element in the div with class name 'et-pb-contact-message' contains the text 'Message'
        assert check_exists_by_xpath(driver, "//div[contains(@class, 'et-pb-contact-message') and contains(.//li, 'Message')]")

        time.sleep(SLEEP_TIME)

    def tearDown(self):
        self.driver.close()


# Helper functions
def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


if __name__ == "__main__":
    unittest.main()
