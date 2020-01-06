import functools


def partialclass(cls, *args, **kwds):

    class NewCls(cls):

        print(args, kwds)
        __init__ = functools.partialmethod(cls.__init__, *args, **kwds)

    return NewCls

def crawler_class_connector(crawler_class):
    return [func for func in dir(crawler_class)
            if callable(getattr(crawler_class, func))]

def get_xpath_attr(driver, xpath_text: str, attr_name: str):
    """
    driver: webdriver
    """
    pass