
class GroupProductInfo:

    def __init__(self, driver, func, gender, product_type, landing_url):
        self.driver = driver
        self.gender = gender
        self.product_type = product_type
        self.landing_url = landing_url
        self.info_to_acquire = []
        self.func = func
        self.get_group_products_urls_func = None
        self.driver.get(self.landing_url)
        self.prepare_self()

    def prepare_self(self):
        for a_func in self.func:
            self.set_func(a_func)

    def set_func(self, func):
        attr_name = func.__name__
        setattr(self, attr_name + '_func', func)
        self.info_to_acquire.append(getattr(self, attr_name))

    def acquire_info(self):
        info = {}
        for get_info in self.info_to_acquire:
            name = get_info.__name__.split('_', 1)[-1]
            info[name] = get_info()
        return info

    def get_group_products_urls(self):
        if not self.get_group_products_urls_func:
            raise NotImplementedError()
        else:
            res = self.get_group_products_urls_func(self.driver)
            return res
