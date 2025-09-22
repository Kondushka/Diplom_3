import allure
from data.urls import Urls

class TestBaseFunc:
        
    @allure.title('Проверка перехода на главную по клику на «Конструктор»')
    def test_click_constructor(self, main_page):
            main_page.open_url(Urls.HOME_PAGE)           
            assert main_page.click_constructor() == Urls.CONSTRUCTOR_PAGE
            
    @allure.title('Проверка перехода на главную по клику на «Лента заказов»')
    def test_click_feed_orders(self, main_page):
            main_page.open_url(Urls.HOME_PAGE)            
            assert main_page.click_feed_orders() == Urls.FEED_ORDER_PAGE
            
    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_open_pop_up_to_click_ingredient(self, main_page):
            main_page.open_url(Urls.HOME_PAGE) 
            assert main_page.click_ingredient()
            
    @allure.title('Проверка закрытия всплывающего окна при клике на крестик')
    def test_close_pop_up(self, main_page):
            main_page.open_url(Urls.HOME_PAGE)
            main_page.click_ingredient()
            assert main_page.close_pop_up_ingredient()
            
    @allure.title("Проверка увеличения кол-ва ингредиента при добавлении в заказ")
    def test_add_ingredient(self, main_page):
            main_page.open_url(Urls.HOME_PAGE)  
            main_page.click_sauce()      
            assert main_page.drag_and_drop_check_count()
            
    @allure.title("Проверка создания заказа авторизированным пользователем")
    def test_creat_order(self, login_page):           
            login_page.open_url(Urls.HOME_PAGE) 
            login_page.click_profile()
            login_page.login_user()
            login_page.drag_and_drop_bun()
            login_page.click_sauce()
            login_page.drag_and_drop_sauce_spicy()
            assert login_page.click_add_order()