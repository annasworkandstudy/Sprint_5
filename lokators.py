from selenium.webdriver.common.by import By

class Lokators_name:
    #Поле для ввода Имени
    INPUT_NAME=(By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    #Поле для ввода Email
    INPUT_EMAIL=(By.XPATH, ".//label[text()='Email']/following-sibling::input")
    #Поле для ввода пароля
    INPUT_PASSWORD=(By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    
    #Кнопка Зарегистрироваться
    BUTTON_REGISTRATION=(By.XPATH, ".//button[text()='Зарегистрироваться']")
    #Кнопка Войти
    BUTTON_ACCOUNT_ENTER=(By.XPATH, ".//button[text()='Войти']")
    #Кнопка Войти в аккаунт на главной
    BUTTON_ACCOUNT_ENTER_MAIN=(By.XPATH, ".//button[text()='Войти в аккаунт']")
    #Кнопка Оформить заказ
    BUTTON_ORDER=(By.XPATH, ".//button[text()='Оформить заказ']")
    #Кнопка личный кабинет на главной странице
    BUTTON_PERSONAL_ACCOUNT=(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    #Кнопка Войти на форме регистрации и восстановление пароля
    BUTTON_ENTER_ACCOUNT_REGISTRATION=(By.XPATH, ".//a[text()='Войти']")
    #Сообщение о некорректном пароле
    MESSAGE_UNCORRECT=(By.XPATH, ".//p[contains(text(),'Некорректный пароль')]")
    
    #Кнопка Отмена при переходе в личный кабинет
    BUTTON_CANCEL=(By.XPATH, ".//button[text()='Отмена']")
    #Кнопка Конструктор
    BUTTON_CONSTRUCTOR=(By.XPATH, ".//p[text()='Конструктор']")
    #Заголовок Соберите бургер
    HEADER_BURGER=(By.XPATH, ".//h1[text()='Соберите бургер']")
    #Кнопка Выход
    BUTTON_EXIT=(By.XPATH, ".//button[text()='Выход']")
    
    #Кнопка Булки
    BUN=(By.XPATH, ".//span[text()='Булки']/parent::div")
    #Кнопка Соусы
    SAUCES=(By.XPATH, ".//span[text()='Соусы']/parent::div")
    #Кнопка Начинки 
    FILLINGS=(By.XPATH, ".//span[text()='Начинки']/parent::div")
    
    # Локатор для проверки активной вкладки (если нужно проверить переключение)
    TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")