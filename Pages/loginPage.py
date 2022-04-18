# страница авторизации
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_link_xpath = Locators.login_button_link_xpath
        self.invalidUsername_message_xpath = Locators.invalidUsername_message_xpath
        self.invalidPassword_message_xpath = Locators.invalidPassword_message_xpath
        self.invalidUsernameAndPassword_xpath = Locators.invalidUsernameAndPassword_xpath

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_link_xpath).click()

    def check_invalid_username_message(self):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        msg_2 = self.driver.find_element(By.XPATH, self.invalidUsername_message_xpath).text
        return msg_2

    def check_invalid_password_message(self):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        msg_3 = self.driver.find_element(By.XPATH, self.invalidPassword_message_xpath).text
        return msg_3

    def check_invalid_username_and_password_message(self):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        msg_4 = self.driver.find_element(By.XPATH, self.invalidUsernameAndPassword_xpath).text
        return msg_4
