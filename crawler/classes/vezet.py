from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re

class Vezet(object):

    def __init__(self, start, finish):

        self.start = re.split(' ', start)[-2] + re.split(' ', start)[-1]
        self.finish = re.split(' ', finish)[-2] + re.split(' ', finish)[-1]

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
            driver.get('https://spb.rutaxi.ru/index.html')
            time.sleep(1)

            elem = driver.find_elements_by_xpath('//input[@type="text"]')[0]
            elem.clear()
            elem.send_keys(self.start[0])
            time.sleep(1)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_elements_by_xpath('//input[@type="text"]')[1]
            elem.send_keys(self.start[1])
            elem.send_keys(Keys.RETURN)
            elem = driver.find_elements_by_xpath('//input[@type="text"]')[2]
            elem.send_keys('1')

            elem = driver.find_elements_by_xpath('//input[@type="text"]')[3]
            elem.clear()
            elem.send_keys(self.finish[0])
            time.sleep(1)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_elements_by_xpath('//input[@type="text"]')[4]
            elem.send_keys(self.finish[1])
            elem.send_keys(Keys.RETURN)
            elem = driver.find_elements_by_xpath('//input[@type="text"]')[5]
            elem.send_keys('1')

            time.sleep(1)

            price = driver.find_element_by_xpath('//span[@class="new_price"]').text
            # price = re.split('\s', price)[0]
            driver.quit()
            #print('vt over')
            return int(price)
        except:
            driver.quit()
            return 'crawl err'

def main():
    
    vezet = Vezet(start='Санкт-Петербург шоссе, Революции 33к4', finish='Санкт-Петербург улица, Ленсовета 50к1')
    print(vezet.crawl())


if __name__ == '__main__':
    main()


