# для фикстур
# python -m pytest -v --html=.\Reports\report.html --driver Chrome --driver-path C:/Users\test/PycharmProjects/FixPrise/chromedriver.exe Tests/login.py

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service
        cls.driver = webdriver.Chrome(
            executable_path='C:/Users/test/PycharmProjects/FixPrise/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_invalid_username_message(self):
        """Ввод неверного логина"""
        driver = self.driver
        driver.get('https://fix-price.ru/personal/')

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov80mail.ru')
        login.enter_password('Kruglik0v85')
        login.click_login()
        login.check_invalid_username_message()
        message = driver.find_element(By.XPATH, '//div[@class="form-login__opt"]').text
        assert 'Email введен некорректно' in message


    def test_02_invalid_password_message(self):
        """Ввод неверного пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('1234567')
        login.click_login()
        login.check_invalid_password_message()
        message_2 = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]/text()').text
        self.assertEqual(message_2, 'Пользователь с таким логином и паролем не найден.')

    def test_03_invalid_username_and_password_message(self):
        """Ввод неверных логина и пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('Kruqwert')
        login.click_login()
        login.check_invalid_password_message()
        message_3 = driver.find_element(By.XPATH, '//div[@class="form-line auth-result"]/text()').text
        self.assertEqual(message_3, 'Пользователь с таким логином и паролем не найден.')

    def test_04_login_valid(self):
        """Ввод верных логина и пароля"""
        driver = self.driver

        driver.find_element(By.XPATH, "//label[@for='switcher-auth__email']").click()
        login = LoginPage(driver)
        login.enter_username('6arikov85@mail.ru')
        login.enter_password('Kruglik0v85')
        login.click_login()
        message_4 = driver.find_element(By.XPATH, "//div[@class='personal-info__greeting']").text
        self.assertEqual(message_4, 'ЗДРАВСТВУЙТЕ,')

    def test_05_click_my_favorite(self):
        """Проверка кликабельности кнопки 'Избранные товары'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_favorite()

        message_5 = driver.find_element(By.XPATH, '//*[@id="favoritesCounter"]').text
        self.assertEqual(message_5, 'Избранные товары')

    def test_06_click_my_basket(self):
        """Проверка кликабельности кнопки 'Моя корзина'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_basket()

        message_6 = driver.find_element(By.XPATH, '//*[@id="basketCounter"]').click()
        self.assertEqual(message_6, 'Моя корзина')

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print('Test completed')

    if __name__ == '__main__':
        unittest.main()