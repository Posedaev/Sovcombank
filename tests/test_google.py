from Sovcombank.pages.google_page import GooglePage
from Sovcombank.config import *


def test_search_in_google(browser):
    '''Первый сценарий'''
    page = GooglePage(browser)
    page.go_to_site(main_url)
    google_search = page.check_search_field()
    tips = page.send_and_check_results_search_field('Совкомбанк')
    for tip in tips:
        assert 'совкомбанк' in tip
    page.press_enter()
    page.check_link_in_first_five_results()


def test_pictures_in_google(browser):
    '''Второй сценарий'''
    page = GooglePage(browser)
    page.go_to_site(stage_two_link)
    page.check_and_click_pictures_btn()
    page.open_picture_and_check()
    page.go_next_pic_go_back_and_check()



