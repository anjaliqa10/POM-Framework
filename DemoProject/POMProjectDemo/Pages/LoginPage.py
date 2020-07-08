from DemoProject.POMProjectDemo.Locators.locators import locators

class LoginPage():  # Class name should always start with Capital letter

    # Here in loginpage class, I have added all the objects and also actions needs to be performed on those objects

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = locators.username_textbox_id  # keeping locators for web elements of the webpage
        self.password_textbox_id = locators.password_textbox_id
        self.login_button_id = locators.login_button_id
        self.invalid_cred_msg_xpath = locators.invalid_cred_msg_xpath

    def enter_username(self, username):  # defined argument as username
        self.driver.find_element_by_id(self.username_textbox_id).clear()  # clearing textbox before performing enter username action
        self.driver.find_element_by_id(locators.username_textbox_id).send_keys(username)  # whatever input user will provide, it will take that and pass it as we are calling argument username

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(locators.password_textbox_id).send_keys(password)

    def click_login_button(self):  # no need to define any argument as we do not need any input, and just have to click on login btn
        self.driver.find_element_by_id(locators.login_button_id).click()

    def invalid_cred_msg(self):
        msg = self.driver.find_element_by_xpath(locators.invalid_cred_msg_xpath).text
        print(msg)
        return msg

