"""Проверка процесса выбора и покупки товара"""
from pages.Card_page import card_page
from pages.Cloth_Men_page import Cloth_Men_page
from pages.Cloth_page import cloth_page
from pages.Product_page_cloth_men import product_page_cloth
from pages.Snowboard_page import Snowboard_page
from pages.catalog_page import catalog_page
from pages.product_page_snowboard import product_page_snowboard
from pages.main_page import main_page
from pages.Snowboarding_equipment_page import Snowboarding_equipment_page

def test_buy_product_1(set_up):
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

    pp = product_page_snowboard(driver1)
    pp.adding_product_to_cart()

    mp.open_card()

    cap = card_page(driver1)
    cap.open_select_all_products()

def test_buy_product_2(set_up):
    driver = set_up

    mp = main_page(driver)
    mp.open_catalog_page()

    cp = catalog_page(driver)
    cp.open_Cloth()

    clp = cloth_page(driver)
    clp.open_Men_clothing()

    cmp = Cloth_Men_page(driver)
    cmp.close_filters()
    cmp.apply_filter_price()

    ppc = product_page_cloth(driver)
    ppc.adding_product_to_cart()

    mp.open_card()

    cap = card_page(driver)
    cap.open_select_all_products()



