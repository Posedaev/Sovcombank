from selenium.webdriver.common.by import By


class GoogleLocators:
    SEARCH_FIELD = (By.ID, 'APjFqb')
    TIPS_FIELDS = (By.XPATH, '//*[contains(text(), "совкомбанк")]')
    SECOND_PIC = (By.XPATH, '//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img')
    SEARCH_RESULTS = (By.XPATH, '//a[@jsname="UWckNb"]')
    CHECK_LINK_IN_FIRST_FIVE_RES = (By.XPATH, '//a[@jsname="UWckNb" and @href="https://sovcombank.ru/"]')
    PICTURES = (By.XPATH, '//*[@class="MUFPAc"]//div/a[contains(text(), "Картинки")]')
    CHECK_SECOND_PIC = (By.XPATH, '//*[@id="islsp"]//a/img[@class="sFlh5c pT0Scc iPVvYb"]')