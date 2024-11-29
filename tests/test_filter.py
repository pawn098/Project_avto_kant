"""Проверка работы фильтров"""
from pages.Snowboard_page import Snowboard_page
from pages.catalog_page import catalog_page
from pages.main_page import main_page
from pages.Snowboarding_equipment_page import Snowboarding_equipment_page

def test_filter(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Snowboards()

    sp = Snowboard_page(driver1)
    sp.close_filters()

    sp.apply_filter_price()

