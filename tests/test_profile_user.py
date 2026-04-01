import allure
from data.urls import Urls

class TestProfileUser:
    
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_open_profile(self,login_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        assert login_page.click_profile()
            
    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_open_history_orders(self, login_page, profile_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        login_page.click_profile()
        assert profile_page.click_history_orders()
        
    @allure.title("Проверка выхода из аккаунта")
    def test_exit_user(self, login_page, profile_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        login_page.click_profile()
        assert profile_page.click_exit()