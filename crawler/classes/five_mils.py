

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re

class Five(object):

    def __init__(self, start, finish):
        self.start = start
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
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('http://www.5-000-000.ru/online/')
            elem = driver.find_elements_by_xpath('//input[@type="text"]')[0]
            elem.clear()
            elem.send_keys(self.start)
            time.sleep(1)
            elem.send_keys(Keys.TAB)
            elem.send_keys(Keys.RETURN)

            elem = driver.find_elements_by_xpath('//input[@type="text"]')[1]
            elem.clear()
            elem.send_keys(self.finish)
            time.sleep(1)
            elem.send_keys(Keys.TAB)
            elem.send_keys(Keys.RETURN)
            time.sleep(2)

            price = driver.find_element_by_id('rcost').text
            price = re.split(' ', price)[-2]

            driver.quit()
            #print('5m over')
            return int(price)
        except:
            driver.quit()
            return 'crawl err'
            
def main():
    
    five_mils = Five(start='Революции 33к4', finish='Ленсовета 50к1')
    print(five_mils.crawl())


if __name__ == '__main__':
    main()
