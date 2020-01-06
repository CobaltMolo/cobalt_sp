from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common import action_chains


def click_element(driver, element):
    driver.execute_script("arguments[0].click();", element)


def hover_over_element(driver: WebDriver, xpath_text):
    """Moves the mouse pointer to the element and hovers"""
    element = driver.find_element_by_xpath(xpath_text)
    action_chains.ActionChains(driver).move_to_element(element).perform()


def hover_over_element_and_click(driver: WebDriver, xpath_text):
    """Moves the mouse pointer to the element and hovers"""
    element = driver.find_element_by_xpath(xpath_text)
    action_chains.ActionChains(driver).move_to_element(element).click().perform()


def hover_over_location_and_click(driver: WebDriver, location):
    """Moves the mouse pointer to the element and hovers"""
    action = action_chains.ActionChains(driver)
    action.move_by_offset(location['x'], location['y'])
    action.click()
    action.perform()


def scroll_to(driver: WebDriver, y: str):
    driver.execute_script("window.scrollTo(0, {});".format(y))


def scroll_to_page_bottom(driver: WebDriver):
    """Scrolls to te page bottom using JS
    Args:
        driver (base.CustomDriver)
    """
    scroll_to(driver, "document.body.scrollHeight)")
