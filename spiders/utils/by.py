from selenium.webdriver.common.by import By


def locator_by_xpath(xpath_text):
    return By.XPATH, xpath_text

