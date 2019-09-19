from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import re

class Yandex(object):

    def __init__(self, start, finish):
        self.start = start.replace(',', '')
        self.finish = finish

    def whoami(self):
        return type(self).__name__

    def crawl(self):

        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get('https://taxi.yandex.ru/#index')

            wait = WebDriverWait(driver, 30)

            wait.until(EC.visibility_of_element_located((By.NAME, 'gfrom')))
            elem = driver.find_element_by_name('gfrom')
            elem.clear()
            elem.send_keys(self.start)
            time.sleep(1)
            elem.send_keys(Keys.RETURN)
            elem.send_keys(Keys.ARROW_DOWN)
            elem.send_keys(Keys.RETURN)

            wait.until(EC.visibility_of_element_located((By.NAME, 'gto')))
            elem = driver.find_element_by_name('gto')
            elem.clear()
            elem.send_keys(self.finish)
            time.sleep(1)
            elem.send_keys(Keys.RETURN)
            elem.send_keys(Keys.ARROW_DOWN)
            elem.send_keys(Keys.RETURN)

            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'routestats__price')))
            price = driver.find_element_by_class_name('routestats__price').text
            price = re.split(' ', price)
            price = re.split('\D', price[-1])[0]
            driver.quit()
            #print('ya over')
            return price
        except:
            return 'crawl err full'

def main():
    
    ya = Yandex(start='Санкт-Петербург Шоссе Революции 33к4', finish='Санкт-Петербург Улица Ленсовета 50к1')
    print(ya.crawl())


if __name__ == '__main__':
    main()

# ya = Yandex(start='Революции 33к4', finish='Ленсовета 50к1')
# print(ya.crawl())