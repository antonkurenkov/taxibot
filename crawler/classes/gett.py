from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import re

class Gett(object):

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def whoami(self):
        return type(self).__name__

    def get_length(self):
        
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://yandex.ru/maps/routes')

            elem = driver.find_elements_by_xpath('//input[@class="input_waypoint__control"]')[0]
            elem.send_keys(self.start)
            time.sleep(1)
            elem.send_keys(Keys.ARROW_DOWN)
            elem.send_keys(Keys.RETURN)

            elem = driver.find_elements_by_xpath('//input[@class="input_waypoint__control"]')[1]
            elem.send_keys(self.finish)
            time.sleep(1)
            elem.send_keys(Keys.ARROW_DOWN)
            elem.send_keys(Keys.RETURN)

            wait = WebDriverWait(driver, 30)

            if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="driving-route-form-view__route-title-secondary"]'))):
                route = re.split('&nbsp;', driver.find_element_by_xpath('//*[@class="driving-route-form-view__route-title-secondary"]').text)[0]
                route = re.split(' ', route.replace(',', '.'))[0]
            else:
                route = 0
                driver.quit()
                

            if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="driving-route-form-view__route-title-primary"]'))):
                duration = re.split('&nbsp;', driver.find_element_by_xpath('//*[@class="driving-route-form-view__route-title-primary"]').text)[0]
                duration = re.split(' ', duration.replace(',', '.'))[0]
            else:
                duration = 0
                driver.quit()
                

            trip = [route, duration]
            driver.quit()
            #print('get over')
            return trip
        except:
            driver.quit()
            return [0, 0]

    def calc(self):
        route = Gett.get_length(self)

        price_len = float(78 + (14 * (float(route[0]) - 1)))
        price_time = 78 + (5.5 * (float(route[1]) - 4))
        return round(min(price_len, price_time))


def main():
    gett = Gett(start='Революции 33к4', finish='Ленсовета 50к1')
    print(Gett.calc(gett))


if __name__ == '__main__':
    main()
