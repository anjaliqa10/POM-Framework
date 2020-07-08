import os
import sys
import time
import unittest
import HtmlTestRunner
from selenium import webdriver

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from DemoProject.POMProjectDemo.Pages.HomePage import HomePage
from DemoProject.POMProjectDemo.Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):  # Inheriting from untitest.testcase class, so that we can use unittest functions


    @classmethod
    def setUpClass(cls):  # Inside braces cls is present, you can name anything and use it in subsequent line to execute
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid_username(
            self):  # for test it is always important to start test function with test and again in braces self is avail, so add this in subsequent line at the starting of the code
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    def test_02_login_invalid_username(
                self):  # for test it is always important to start test function with test and again in braces self is avail, so add this in subsequent line at the starting of the code
            driver = self.driver

            driver.get("https://opensource-demo.orangehrmlive.com/")

            login = LoginPage(driver)
            login.enter_username("Admin1")
            login.enter_password("admin123")
            login.click_login_button()
            message = login.invalid_cred_msg()
            self.assertEqual(message, 'Invalid credentials')



    @classmethod
    def tearDownClass(
            cls):  # using tearDownClass because i will be closing the browser only once after all the tests are completed
        cls.driver.close()
        cls.driver.quit()

        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Anjali/PycharmProjects/Selenium-Framework/reports'))
