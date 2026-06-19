import data
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        assert 'Comfort' in routes_page.get_comfort_text()

    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        assert routes_page.get_phone_number() == data.phone_number

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        assert routes_page.get_payment_method() == 'Tarjeta'

    def test_write_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.set_message_for_driver(data.message_for_driver)
        assert routes_page.get_message_for_driver() == data.message_for_driver

    def test_order_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.order_blanket_and_tissues()
        assert routes_page.is_blanket_selected()

    def test_order_two_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.order_blanket_and_tissues()
        routes_page.add_two_ice_creams()
        assert routes_page.get_ice_cream_count() == '2'

    def test_search_taxi_modal_appears(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.order_blanket_and_tissues()
        routes_page.add_two_ice_creams()
        routes_page.order_taxi()
        assert routes_page.get_search_modal_text() != ''

    def test_driver_info_appears(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.set_message_for_driver(data.message_for_driver)
        routes_page.order_blanket_and_tissues()
        routes_page.add_two_ice_creams()
        routes_page.order_taxi()
        assert routes_page.wait_for_driver_info().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()