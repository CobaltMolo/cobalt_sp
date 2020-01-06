import logging

from selenium.common import exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import by, wait


logger = logging.getLogger(__name__)


def get_element_when_visible(
        driver: WebDriver, xpath_text: str,
        wait_seconds=1, return_bool=False,
        wait_until_fully_loaded=True):
    """
    Args:
      driver (base.CustomDriver)
      xpath_text str
    Returns:
        selenium.webdriver.remote.webelement.WebElement
    """
    if wait_until_fully_loaded:
        wait.wait_until_page_fully_loaded(driver)
    locator = by.locator_by_xpath(xpath_text)
    try:
        element = WebDriverWait(driver, wait_seconds).until(
            EC.presence_of_element_located(locator))
        if not return_bool:
            return element
        else:
            return True
    except exceptions.TimeoutException:
        return False


def get_element_when_clickable(
        driver: WebDriver, xpath_text: str, wait_seconds=1,
        wait_until_fully_loaded=True):
    """
    Args:
      driver (base.CustomDriver)
      xpath_text str
      wait_seconds: int
      return_element: bool
    Returns:
        bool or selenium.webdriver.remote.webelement.WebElement
    """
    if wait_until_fully_loaded:
        wait.wait_until_page_fully_loaded(driver)
    locator = by.locator_by_xpath(xpath_text)
    try:
        element = WebDriverWait(driver, wait_seconds).until(
            EC.element_to_be_clickable(locator))
        return element
    except exceptions.TimeoutException:
        return None


def get_element_location_when_clickable(
        driver: WebDriver, xpath_text: str, wait_seconds=1,
        wait_until_fully_loaded=True):
    """
    Args:
      driver (base.CustomDriver)
      xpath_text str
      wait_seconds: int
      return_element: bool
    Returns:
        bool or selenium.webdriver.remote.webelement.WebElement
    """
    if wait_until_fully_loaded:
        wait.wait_until_page_fully_loaded(driver)
    locator = by.locator_by_xpath(xpath_text)
    try:
        element = WebDriverWait(driver, wait_seconds).until(
            EC.element_to_be_clickable(locator))
        return element.location
    except exceptions.TimeoutException:
        return None


def get_element_when_text_appear(driver: WebDriver, xpath_text,
                                 text, wait_seconds=1,
                                 wait_until_fully_loaded=True):
    """
      Args:
        driver (base.CustomDriver)
        locator (tuple)
        text (str)
    """
    if wait_until_fully_loaded:
        wait.wait_until_page_fully_loaded(driver)
    locator = by.locator_by_xpath(xpath_text)
    return WebDriverWait(driver, wait_seconds).until(
        EC.text_to_be_present_in_element(locator, text))