from selenium.webdriver.common.by import By

class LocatorsButtons:
    
    BUTTON_FORGOT_PASSWORD = By.CSS_SELECTOR, "a[href='/forgot-password']"
    BUTTON_RESET_PASSWORD = By.XPATH, "//button[text()='Восстановить']"
    BUTTON_CONSTRUCTOR = By.CSS_SELECTOR, "a[href='/']"
    BUTTON_FEED_ORDERS = By.CSS_SELECTOR, "a[href='/feed']"
    BUTTON_INGREDIENT = By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d']"
    BUTTON_EXIT_POP_UP = By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK'
    BUTTON_SAUCE = By.XPATH, "//span[text()='Соусы']"
    BUTTON_ENTER = By.XPATH, "//button[text()='Войти']"
    BUTTON_PROFILE = By.XPATH, "//p[text()='Личный Кабинет']"
    BUTTON_HISTORY_ORDERS = By.XPATH, "//a[text()='История заказов']"
    BUTTON_EXIT = By.XPATH, "//button[text()='Выход']"
    BUTTON_ADD_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'

    
    