import allure
from data.urls import Urls

class TestResetPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_reset_password(self, login_page):
        login_page.open_url(Urls.LOGIN_PAGE)          
        login_page.click_forgot_password() 
        assert login_page.click_reset_password()

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_enter_email(self, login_page):
        login_page.open_url(Urls.LOGIN_PAGE)        
        login_page.click_forgot_password()         
        login_page.add_data_user_email()
        assert login_page.click_reset_password()

    @allure.title("Проверка активации скрытия/показа пароля")
    def test_active_pass(self, login_page):
        login_page.open_url(Urls.LOGIN_PAGE)
        assert login_page.click_eye()