
class ProductInfo:

    def __init__(self, driver, func, sub_product_func, sub_product_info_class):
        self.driver = driver
        self.go_to_sub_product_func = None
        self.get_product_id_func = None
        self.info_to_acquire = []
        self.func = func
        self.sub_product_info_class = sub_product_info_class
        self.sub_product_func = sub_product_func
        self.prepare_self()

    def prepare_self(self):
        for a_func in self.func:
            self.set_func( a_func)

    def set_func(self, func):
        attr_name = func.__name__
        setattr(self, attr_name + '_func', func)
        self.info_to_acquire.append(getattr(self, attr_name))

    def acquire_info(self):
        product_info = {}
        sub_product_info = []
        sub_product_taken = False
        for get_info in self.info_to_acquire:
            res = get_info()
            if isinstance(res, dict):
                product_info.update(res)
            elif isinstance(res, list):
                if not sub_product_taken:
                    sub_product_info = res
                    sub_product_taken = True
                else:
                    raise ValueError('no more than one sub product info')
            else:
                raise ValueError('wrong type')
        if not sub_product_info:
            raise ValueError('need to have sub product info')

        new_sub_product_info = []
        for sub in sub_product_info:
            sub.update(product_info)
            new_sub_product_info.append(sub)

        return new_sub_product_info

    def go_to_sub_product(self):
        if not self.go_to_sub_product_func:
            raise NotImplementedError()
        else:
            res = self.go_to_sub_product_func(self.driver,
                                              self.sub_product_func,
                                              self.sub_product_info_class)
            return res

    def get_product_id(self):
        if not self.get_product_id_func:
            raise NotImplementedError()
        else:
            res = self.get_product_id_func(self.driver)
            return res

    def gen_product_id(self):
        pass

    def get_product_name(self):
        pass


class SubProductInfo:

    def __init__(self, driver, func):
        self.driver = driver
        self.get_image_urls_func = None
        self.info_to_acquire = []
        self.func = func
        self.prepare_self()

    def prepare_self(self):
        for a_func in self.func:
            self.set_func( a_func)

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

    def get_image_urls(self):
        if not self.get_image_urls_func:
            raise NotImplementedError()
        else:
            image_urls = self.get_image_urls_func(self.driver)
            return image_urls

    def get_yarn_contents(self):
        raise NotImplementedError()

    def get_colors(self):
        raise NotImplementedError()

    def get_available_sizes(self):
        raise NotImplementedError()

    def get_out_of_stock_sizes(self):
        raise NotImplementedError()

    def get_price(self):
        raise NotImplementedError()

    def get_discount_price(self):
        raise NotImplementedError()


