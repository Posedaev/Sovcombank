from Sovcombank.pages.base_page import BasePage
from Sovcombank.locators import *
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


class GooglePage(BasePage):
    def check_search_field(self):
        try:
            search_field = self.find_element(GoogleLocators.SEARCH_FIELD)
            print('Присутствует поле поиска')
            return search_field
        except TimeoutException:
            print('Поле поиска отсутствует')

    def send_and_check_results_search_field(self, input_value):
        search_field = self.find_element(GoogleLocators.SEARCH_FIELD)
        search_field.send_keys(input_value)
        tips = self.find_elements(GoogleLocators.TIPS_FIELDS)
        tips_text = [i.text for i in tips]
        if tips:
            print('Присутствует таблица с подсказками:', tips_text)
            return tips_text
        else:
            print('Таблиа с подсказками отсутствует')

    def press_enter(self):
        elem = self.find_element(GoogleLocators.SEARCH_FIELD)
        elem.submit()

    def check_link_in_first_five_results(self):
        results = self.find_elements(GoogleLocators.SEARCH_RESULTS)
        if results:
            print('Появилась таблица результатов поиска')
        else:
            print('Таблица результатов поиск не появилась')
        link_on_sovcombank = self.find_elements(GoogleLocators.CHECK_LINK_IN_FIRST_FIVE_RES)
        target_url = 'https://sovcombank.ru/'
        count = 0
        link_in_results = 0
        for result in link_on_sovcombank:
            link = result.get_attribute('href')
            count += 1
            if link in target_url:
                link_in_results += 1
            if count == 5:
                break
        print(f'Найдено {link_in_results} ссылок на https://sovcombank.ru в первых пяти результатах поиска')

    def check_and_click_pictures_btn(self):
        try:
            pictures = self.find_element(GoogleLocators.PICTURES)
            print('Кнопка "Картинки" присутствует на странице')
            pictures.click()
        except TimeoutException:
            print('Кнопка "Картинки отсутствует"')

    def open_picture_and_check(self):
        second_pic = self.find_element(GoogleLocators.SECOND_PIC)
        try:
            second_pic.click()
            if second_pic:
                print('Вторая картинка открылась')
        except TimeoutException:
            print('Картинка не открылась')

    def go_next_pic_go_back_and_check(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_RIGHT)
        action.send_keys(Keys.ARROW_LEFT).perform()
        try:
            check_second_pic = self.find_element(GoogleLocators.CHECK_SECOND_PIC)
            if check_second_pic:
                print('После нажатия кнопок: "вперед" и "назад" картинка изменилась на картинку из шага 4')
        except TimeoutException:
            print('Картинка не открылась')





