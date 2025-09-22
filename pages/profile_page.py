from pages.base_page import Methods
from locators.locators_buttons import LocatorsButtons as LB
from locators.locators_elements import LocatorsElements as LE


class ProfilePage(Methods):

    def click_exit(self):
        self.wait_visible(LB.BUTTON_EXIT)
        self.find_element_and_click(LB.BUTTON_EXIT)
        return self.wait_visible(LE.INPUT_EMAIL)
    
    def click_history_orders(self):
        self.wait_visible(LB.BUTTON_HISTORY_ORDERS)
        self.find_element_and_click(LB.BUTTON_HISTORY_ORDERS)
        return self.wait_visible(LE.ACTIVE_HISTORY_ORDERS)

    def click_my_order(self):
        self.wait_visible(LE.MY_ORDER)
        self.find_element_and_click(LE.MY_ORDER)
            
    def check_item_order(self):
        return self.wait_visible(LE.POP_UP_ORDER_ITEMS)
    
    def find_number_order_in_hisroty_orders(self, order_id):
        by, template = LE.DYNAMIC_ORDER
        locator = (by, template.format(order_id=order_id))
        return self.wait_visible(locator).is_displayed()