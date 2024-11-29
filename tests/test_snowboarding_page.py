"""Проверка кликабельности разделов во вкладке 'сноуборды'"""
from pages.catalog_page import catalog_page
from pages.main_page import main_page
from pages.Snowboarding_equipment_page import Snowboarding_equipment_page

def test_01(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Masks()
def test_02(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Helmets()
def test_03(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Bindings()
def test_04(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Backpacks()
def test_05(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Accessories_and_Spares()
def test_06(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Snowboard_Covers()
def test_07(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Snowboard_Boots()
def test_08(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Splitboarding()
def test_09(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Snowboard_Kits()
def test_10(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Protection()
def test_11(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Boot_Bags()
def test_12(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Avalanche_Gear()
def test_13(set_up):
    driver1 = set_up
    mp = main_page(driver1)
    mp.open_catalog_page()

    cp = catalog_page(driver1)
    cp.open_Snowboarding_equipment()

    sep = Snowboarding_equipment_page(driver1)
    sep.open_Tools_and_Care()