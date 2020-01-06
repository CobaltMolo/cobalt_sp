from selenium import webdriver

from spiders.crawlers.product_info import SubProductInfo, ProductInfo
from spiders.crawlers.group_product_info import GroupProductInfo
from spiders.utils.get_element import get_element_when_clickable
from spiders.utils.wait import wait_until_page_fully_loaded
from selenium.webdriver.support.ui import Select



# groups
def get_groups_url(driver):
    driver.get('https://www.kohls.com/')
    wait_until_page_fully_loaded(driver)
    menu_element = get_element_when_clickable(driver, '//li/a/p/span')
    print(menu_element)
    wait_until_page_fully_loaded(driver)




# group_products
def get_group_products_urls(driver):
    wait_until_page_fully_loaded(driver)
    group_products_urls = []
    group_products_elements = driver.find_elements_by_xpath(
        '//div[1]/div[3]/ul/li/div/a')
    for group_products_element in group_products_elements:
        group_product_url = group_products_element.get_attribute('rel')
        print(group_product_url)
        group_product_url = 'https://www.kohls.com' + group_product_url
        group_products_urls.append(group_product_url)
    return group_products_urls


# product
def get_product_id(driver):
    url_text = driver.current_url
    url_text = url_text.split('/prd-', 1)[-1]
    url_text = url_text.split('/', 1)[0]
    return {'product_id': url_text}


def go_to_sub_product(driver, sub_product_func, sub_product_class, max_trial=100):
    sub_product_info = []
    sub_product = sub_product_class(driver, sub_product_func)
    sub_product_info.append(sub_product.acquire_info())
    for n in range(max_trial):
        next_active_element = get_element_when_clickable(
            driver, '//div[contains(@class, "active")]/following-sibling::div[1]/a')
        if next_active_element is not None:
            next_active_element.click()
            sub_product = sub_product_class(driver, sub_product_func)
            sub_product_info.append(sub_product.acquire_info())
        else:
            break
    return sub_product_info


# sub product
def get_image_urls(driver):
    image_elements = driver.find_elements_by_xpath(
        '//*[@id="container"]/div[3]/div[1]/div[2]/div[1]'
        '/div[1]/div[1]/div[1]/div/ul/li/a')
    image_rels = []
    for image_element in image_elements:
        image_rel = image_element.get_attribute('rel')
        if 'image' in image_rel:
            image_rel = image_rel.split('?')[0]
            image_rels.append(image_rel)
    return image_rels


group_info_func =[
    get_group_products_urls
]


sub_info_func = [
    get_image_urls,
    # get_yarn_contents,
    # get_colors,
    # get_available_sizes,
    # get_out_of_stock_sizes,
]

product_info_func = [
    get_product_id,
    go_to_sub_product,
]


class NineWestCrawlers:

    def __init__(self, group_info_func, produdt_info_func, sub_info_func, sub_product_info_class):
        chromedriver_path = 'C:\\Users\\domin\\cobalt_spiders\\' \
                            'drivers/chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument('headless')
        self.driver = webdriver.Chrome(
            chromedriver_path, chrome_options=options)

        # self.driver.get(
        #     'https://www.kohls.com/product/prd-3899300/womens-nine-west-pleated-long-sleeve-sweater-dress.jsp?
        #      color=Black&prdPV=1')
        self.sub_info_func = sub_info_func
        self.product_info_func = produdt_info_func
        self.sub_product_info_class = sub_product_info_class
        self.group_info_func = group_info_func
        # self.sub_product_info = self.prepare_sub_product_info()
        get_groups_url(self.driver)

    def get_group_product_info(self):
        group_info_input = {'gender': 'women', 'product_type': 'sweater',
                            'landing_url': 'https://www.kohls.com/catalog/nine-west-sweaters-tops-clothing.jsp?CN='
                                            'Brand:Nine%20West+Product:Sweaters+Category:Tops+Department:Clothing&S='
                                            '1&PPP=60&kls_sbp=68744280629584040040158085713213608748&pfm=browse-pdp-'
                                            'breadcrumb%20refine'}
        group_product_info = GroupProductInfo(driver=self.driver, func=group_info_func, **group_info_input)
        acquired_product_info = group_product_info.acquire_info()

    def get_product_info(self):
        product_info = ProductInfo(driver=self.driver,
                                   func=self.product_info_func,
                                   sub_product_func=self.sub_info_func,
                                   sub_product_info_class=self.sub_product_info_class)
        acquired_product_info = product_info.acquire_info()
        print(acquired_product_info)


n = NineWestCrawlers(group_info_func, product_info_func, sub_info_func, sub_product_info_class=SubProductInfo)
# n.get_group_product_info()
# n.get_product_info()

