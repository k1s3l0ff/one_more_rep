from steam_pages import SteamMain


def test_steam_search(browser):
    steam_main_page = SteamMain(browser)
    steam_main_page.go_to_site()
    
    steam_main_page.enter_word('The Witcher')
    steam_main_page.click_on_search_button()
    steam_main_page.sort_in_descending_order()