import allure 
from pages.main_page import MainPage
from data.data_user import DataUser as DU
from locators.locators_buttons import LocatorsButtons as LB
from locators.locators_elements import LocatorsElements as LE


class LoginPage(MainPage):
    
    @allure.step('Нажимаем "восстановить пароль"')
    def click_forgot_password(self):         
        self.wait_visible(LB.BUTTON_FORGOT_PASSWORD)
        self.find_element_and_click(LB.BUTTON_FORGOT_PASSWORD)
        return self.driver.current_url

    @allure.step('Нажимаем "восстановить"')
    def click_reset_password(self):
        self.wait_visible(LB.BUTTON_RESET_PASSWORD)
        self.find_element_and_click(LB.BUTTON_RESET_PASSWORD)
        return self.wait_visible(LE.PIN)

    @allure.step('Нажимаем на глазик - скрытие/отображение пароля')
    def click_eye(self):
        self.wait_visible(LE.EYE_PASSWORD)
        self.find_element_and_click(LE.EYE_PASSWORD)
        return self.wait_visible(LE.ACTIVE_INPUT_CONTAINER)
        
    @allure.step('Вводим почту')
    def add_data_user_email(self):
        self.input_keys(LE.INPUT_EMAIL, DU.EMAIL_USER)
        
    @allure.step('Вводим почту и пароль')
    def add_data_user_email_and_password(self):
        self.add_data_user_email()
        self.input_keys(LE.INPUT_PASSWORD, DU.PASSWORD_USER)

    @allure.step('Нажимаем "войти"')
    def click_enter_login(self):
        self.find_element_and_click(LB.BUTTON_ENTER)
        return self.driver.current_url

    @allure.step('Логинимся')
    def login_user(self):
        self.click_profile()
        self.add_data_user_email_and_password()
        self.click_enter_login()
        return self.driver.current_url