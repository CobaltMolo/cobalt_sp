import time
from copy import copy


def wait_until_page_fully_loaded(driver, max_n=1000,
                                 wait_inteval=0.01):
    old_html = ''
    for i in range(max_n):
        new_html = driver.page_source
        if new_html == old_html:
            break
        else:
            old_html = copy(new_html)
        time.sleep(wait_inteval)
