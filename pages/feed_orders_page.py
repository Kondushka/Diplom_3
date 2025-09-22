from pages.base_page import Methods
from locators.locators_elements import LocatorsElements as LE


class FeedOrdersPage(Methods):
            
    def get_all_day_number_order(self):
        self.wait_visible(LE.ORDERS_ALL)
        element = self.find_element(LE.ORDERS_ALL)
        return element.text
        
    def get_today_number_order(self):
        self.wait_visible(LE.ORDERS_TODAY)
        element = self.find_element(LE.ORDERS_TODAY)
        return element.text
        
    def check_process_list(self):
        self.wait_visible(LE.PROCESS_LIST)
        element = self.find_element(LE.ORDER_PROCESS)
        return element.text
    
    def find_number_order_in_feed_orders(self, order_id):
        by, template = LE.DYNAMIC_ORDER
        locator = (by, template.format(order_id=order_id))
        return self.wait_visible(locator).is_displayed()
    