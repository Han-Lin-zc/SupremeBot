from selenium import webdriver
from config import keys
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

@timeme
def order(k):
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card_number"])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["card_cvv"])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k["card_exp_mo"])).click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k["card_exp_yr"])).click()
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[45]').click()
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    order(keys)    
    
