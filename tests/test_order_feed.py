import allure
from data.urls import Urls

class TestOrderFeed:
    
    @allure.title('Проверка октрытия всплывающего окна с деталями при клике на заказ')    
    def test_get_item_order(self, login_page, profile_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        login_page.click_profile()
        profile_page.click_history_orders()
        profile_page.click_my_order()
        assert profile_page.check_item_order()
        
    @allure.title('Проверка увеличения счётчика "Выполнено" при создании нового заказа ЗА ВСЕ ВРЕМЯ')        
    def test_assert_all_day_done_counter_grew(self, login_page, feed_orders_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        login_page.click_feed_orders()
        befor = feed_orders_page.get_all_day_number_order()
        login_page.click_constructor()
        login_page.create_order()
        login_page.close_pop_up_order()
        login_page.click_feed_orders()
        after = feed_orders_page.get_all_day_number_order()
        assert befor < after
        
    @allure.title('Проверка увеличения счётчика "Выполнено" при создании нового заказа ЗА СЕГОДНЯ')       
    def test_assert_today_done_counter_grew(self, login_page, feed_orders_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        login_page.click_feed_orders()
        befor = feed_orders_page.get_today_number_order()
        login_page.click_constructor()
        login_page.create_order()
        login_page.close_pop_up_order()
        login_page.click_feed_orders()
        after = feed_orders_page.get_today_number_order()
        assert befor < after
        
    @allure.title('Проверка появления нового заказа в "В работе"')
    def test_check_numder_order_in_process_list(self, login_page, feed_orders_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        number_order = login_page.create_order()
        login_page.close_pop_up_order()
        login_page.click_feed_orders()
        assert number_order in feed_orders_page.check_process_list()

    @allure.title('Проверка отображения на странице "Лента заказов" заказ пользователя из раздела «История заказов»')    
    def test_check_new_order_in_feed_orders_and_history_orders(self, login_page, feed_orders_page, profile_page):
        login_page.open_url(Urls.HOME_PAGE)
        login_page.login_user()
        number_order = login_page.create_order()
        login_page.close_pop_up_order()
        login_page.click_feed_orders()
        
        with allure.step(f'заказ номер: {number_order} есть в ленте заказов'):
            assert feed_orders_page.find_number_order_in_feed_orders(number_order)
            
        login_page.click_profile()
        profile_page.click_history_orders()
            
        with allure.step(f'заказ номер: {number_order} есть в истории заказов'):
            assert profile_page.find_number_order_in_hisroty_orders(number_order)
        