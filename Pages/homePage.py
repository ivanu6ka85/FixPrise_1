# страница пользовательского профиля
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_xpath = Locators.welcome_xpath
        self.click_my_tabs_xpath = Locators.click_my_tabs_xpath
        self.my_basket_xpath = Locators.my_basket_xpath

        

    def check_welcome_message(self):
        msg = self.driver.find_element(By.XPATH, self.welcome_xpath).text
        return msg

    def click_my_favorite(self):
        self.driver.find_element(By.ID, self.click_my_tabs_xpath).click()

    def click_my_basket(self):
        self.driver.find_element(By.ID, self.my_basket_xpath).click()






    