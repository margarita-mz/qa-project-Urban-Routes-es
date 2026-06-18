import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [
                log["message"] for log in driver.get_log('performance')
                if log.get("message") and 'api/v1/number?number' in log.get("message")
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd(
                    'Network.getResponseBody',
                    {'requestId': message_data["params"]["requestId"]}
                )
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    return code
        except WebDriverException:
            time.sleep(1)
            continue

    raise Exception("No se encontró el código de confirmación del teléfono.")


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_tariff = (By.XPATH, "//div[contains(@class, 'tcard')][.//div[text()='Comfort']]")
    phone_field = (By.XPATH, "//div[contains(@class, 'np-button')]")
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    sms_code_input = (By.XPATH, "//input[@id='code']")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    phone_text = (By.CLASS_NAME, 'np-text')
    payment_method = (By.XPATH, "//div[contains(@class, 'pp-button')][.//div[contains(@class, 'pp-text') and contains(text(), 'Método de pago')]]")
    add_card = (By.XPATH, "//div[contains(@class, 'pp-row')][.//div[contains(text(), 'Agregar tarjeta')]]")
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, "//div[contains(@class, 'card-code')]//input[@id='code']")
    add_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_payment_window = (By.XPATH, "//div[contains(@class, 'payment-picker')]//button[contains(@class, 'section-close')]")
    payment_text = (By.CLASS_NAME, 'pp-value-text')
    message_input = (By.ID, 'comment')
    blanket_switch = (By.XPATH, "//div[contains(@class, 'r-type-switch')][.//div[text()='Manta y pañuelos']]//span[contains(@class, 'slider')]")
    blanket_checkbox = (By.XPATH, "//div[contains(@class, 'r-type-switch')][.//div[text()='Manta y pañuelos']]//input[@type='checkbox']")
    ice_cream_plus = (By.XPATH, "//div[contains(@class, 'r-counter-container')][.//div[text()='Helado']]//div[contains(@class, 'counter-plus')]")
    ice_cream_value = (By.XPATH, "//div[contains(@class, 'r-counter-container')][.//div[text()='Helado']]//div[contains(@class, 'counter-value')]")
    final_order_button = (By.XPATH, "//button[contains(@class, 'smart-button')][.//span[contains(text(), 'Pedir un taxi')]]")
    search_taxi_modal = (By.CLASS_NAME, 'order-header-title')
    driver_rating = (By.CLASS_NAME, 'order-btn-rating')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_present(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def set_from(self, from_address):
        self.wait_for_visible(self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.wait_for_visible(self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.wait_for_visible(self.from_field).get_property('value')

    def get_to(self):
        return self.wait_for_visible(self.to_field).get_property('value')

    def select_comfort_tariff(self):
        self.wait_for_clickable(self.order_taxi_button).click()
        self.wait_for_clickable(self.comfort_tariff).click()

    def get_comfort_text(self):
        return self.wait_for_visible(self.comfort_tariff).text

    def set_phone_number(self, phone_number):
        self.wait_for_clickable(self.phone_field).click()
        self.wait_for_visible(self.phone_input).send_keys(phone_number)
        self.wait_for_clickable(self.next_button).click()

        code = retrieve_phone_code(self.driver)

        self.wait_for_visible(self.sms_code_input).send_keys(code)
        self.wait_for_clickable(self.confirm_button).click()

    def get_phone_number(self):
        return self.wait_for_visible(self.phone_text).text

    def add_credit_card(self, card_number, card_code):
        payment_button = self.scroll_to_element(self.payment_method)
        payment_button.click()

        self.wait_for_clickable(self.add_card).click()

        self.wait_for_visible(self.card_number_input).send_keys(card_number)
        self.wait_for_visible(self.card_code_input).send_keys(card_code)
        self.wait_for_visible(self.card_code_input).send_keys(Keys.TAB)

        self.wait_for_clickable(self.add_card_button).click()
        self.wait_for_clickable(self.close_payment_window).click()

    def get_payment_method(self):
        return self.wait_for_visible(self.payment_text).text

    def set_message_for_driver(self, message):
        self.scroll_to_element(self.message_input).send_keys(message)

    def get_message_for_driver(self):
        return self.wait_for_visible(self.message_input).get_property('value')

    def order_blanket_and_tissues(self):
        self.scroll_to_element(self.blanket_switch)
        self.wait_for_clickable(self.blanket_switch).click()

    def is_blanket_selected(self):
        return self.wait_for_present(self.blanket_checkbox).is_selected()

    def add_two_ice_creams(self):
        self.scroll_to_element(self.ice_cream_plus)
        self.wait_for_clickable(self.ice_cream_plus).click()
        self.wait_for_clickable(self.ice_cream_plus).click()

    def get_ice_cream_count(self):
        return self.wait_for_visible(self.ice_cream_value).text

    def order_taxi(self):
        self.scroll_to_element(self.final_order_button)
        self.wait_for_clickable(self.final_order_button).click()

    def get_search_modal_text(self):
        return self.wait_for_visible(self.search_taxi_modal).text

    def wait_for_driver_info(self):
        return WebDriverWait(self.driver, 70).until(expected_conditions.visibility_of_element_located(self.driver_rating))


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
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert 'Comfort' in routes_page.get_comfort_text()

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone_number(data.phone_number)
        assert routes_page.get_phone_number() == data.phone_number

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(data.card_number, data.card_code)
        assert routes_page.get_payment_method() == 'Tarjeta'

    def test_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_driver(data.message_for_driver)
        assert routes_page.get_message_for_driver() == data.message_for_driver

    def test_order_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_tissues()
        assert routes_page.is_blanket_selected()

    def test_order_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_two_ice_creams()
        assert routes_page.get_ice_cream_count() == '2'

    def test_search_taxi_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_taxi()
        assert routes_page.get_search_modal_text() != ''

    def test_driver_info_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.wait_for_driver_info().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()