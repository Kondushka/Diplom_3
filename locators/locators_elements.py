from selenium.webdriver.common.by import By


class LocatorsElements:
    
    INPUT_EMAIL = By.CSS_SELECTOR, "input.text.input__textfield[name='name']"
    INPUT_PASSWORD = By.CSS_SELECTOR, "input.text.input__textfield[name='Пароль']"
    DETAILS_INGREDIENT = By.XPATH, "//*[text()='Детали ингредиента']"
    COUNT_INGREDIENT_0 = By.XPATH, f"//a[contains(@href,'{'61c0c5a71d1f82001bdaaa72'}')]//p[contains(@class,'counter__num') and normalize-space()='0']"
    COUNT_INGREDIENT_1 = By.XPATH, f"//a[contains(@href,'{'61c0c5a71d1f82001bdaaa72'}')]//p[contains(@class,'counter__num') and normalize-space()='1']"
    BUSCET = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    SAUCE_SPICY = By.XPATH, "//p[text()='Соус Spicy-X']"
    POP_UP_ADD_ORDER = By.XPATH, "//p[text()='идентификатор заказа']"
    ACTIVE_HISTORY_ORDERS = By.CLASS_NAME, "Account_link_active__2opc9"
    MY_ORDER = By.CSS_SELECTOR, "a[href='/account/order-history/68cd7da99ed280001b6a36f6']"
    POP_UP_ORDER_ITEMS = By.XPATH, "//p[text()='Cостав']"
    DEFAULT_NUMBER = (By.XPATH, '//h2[text()="9999"]')
    PROCESS_LIST = By.XPATH, "//p[text()='В работе:']"
    ORDER_PROCESS = By.XPATH, "//p[text()='В работе:']/following-sibling::*[1]"
    ORDERS_ALL = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::*"
    ORDERS_TODAY = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::*"
    FEED_ORDERS_LIST = By.CLASS_NAME, "OrderFeed_list__OLh59"
    BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_NUMBER = By.CSS_SELECTOR, "h2.text_type_digits-large"
    PIN = By.XPATH, "//*[text()='Введите код из письма']"
    EYE_PASSWORD = By.CSS_SELECTOR, ".input__icon.input__icon-action"
    ACTIVE_INPUT_CONTAINER = By.CSS_SELECTOR, "div.input.input_type_text.input_size_default.input_status_active"
    DYNAMIC_ORDER  = By.XPATH, ".//p[contains(., '{order_id}')]"
    