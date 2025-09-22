from pages.base_page import Methods
from locators.locators_buttons import LocatorsButtons as LB
from locators.locators_elements import LocatorsElements as LE                               

class MainPage(Methods):

    def click_constructor(self):
        self.find_element_and_click(LB.BUTTON_CONSTRUCTOR)            
        self.wait_visible(LE.BURGER_TITLE)
        return self.driver.current_url
        
    def click_feed_orders(self):
        self.find_element_and_click(LB.BUTTON_FEED_ORDERS)            
        self.wait_visible(LE.FEED_ORDERS_LIST)
        return self.driver.current_url
        
    def click_ingredient(self):
        self.wait_clickable_and_click(LB.BUTTON_INGREDIENT)
        return self.wait_visible(LE.DETAILS_INGREDIENT)
        
    def close_pop_up_ingredient(self): 
        self.find_element_and_click(LB.BUTTON_EXIT_POP_UP)
        return self.wait_invisible(LE.DETAILS_INGREDIENT)
        
    def click_sauce(self):
        self.wait_visible(LB.BUTTON_SAUCE)
        return self.find_element_and_click(LB.BUTTON_SAUCE)
        
    def click_profile(self):
        self.wait_visible(LB.BUTTON_PROFILE)
        self.find_element_and_click(LB.BUTTON_PROFILE)
        return self.driver.current_url
    
    def drag_and_drop_sauce_spicy(self):
        self.wait_visible(LE.SAUCE_SPICY)     
        return self.drag_and_drop_element(LE.SAUCE_SPICY, LE.BUSCET)
    
    def drag_and_drop_bun(self):
        self.wait_visible(LE.BUN)     
        return self.drag_and_drop_element(LE.BUN, LE.BUSCET)
        
    def drag_and_drop_check_count(self):
        self.click_sauce()
        self.wait_visible(LE.COUNT_INGREDIENT_0) 
        self.drag_and_drop_sauce_spicy()      
        return self.wait_visible(LE.COUNT_INGREDIENT_1)
    
    def click_add_order(self):
        self.wait_clickable_and_click(LB.BUTTON_ADD_ORDER)
        return self.wait_visible(LE.POP_UP_ADD_ORDER)
    
    def create_order(self):
        self.drag_and_drop_bun()
        self.drag_and_drop_sauce_spicy()
        self.click_add_order()
        self.wait_until_element_is_invisible(LE.DEFAULT_NUMBER)
        element = self.find_element(LE.ORDER_NUMBER).text
        return f"0{element}"
    
    def close_pop_up_order(self):
        self.wait_visible(LE.POP_UP_ADD_ORDER)    
        self.find_element_and_click(LB.BUTTON_EXIT_POP_UP)
        return self.wait_invisible(LE.POP_UP_ADD_ORDER)
    
    
    
    