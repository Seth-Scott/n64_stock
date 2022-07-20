from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Stock:
    def __init__(self):
        self.chrome_driver_path = "./chromedriver"
        self.url = 'https://www.nintendo.com/store/products/nintendo-64-controller/'
        self.service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def load_url(self):
        # load the URL, wait for all the javascript elements to load
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def check_stock(self):
        """checks to see if the defined CSS selector says 'sold out'. Returns True if item is in stock, and False if it's
        not """
        # exception handling
        try:
            stock_string = self.driver.find_element(By.CSS_SELECTOR,
                                                    '#main > section.Herostyles__HeroSection-sc-1gi6jtj-0.kKfMBG > '
                                                    'div > '
                                                    'div.Herostyles__HeroInfo-sc-1gi6jtj-8.gAHENY > '
                                                    'div.Gridstyles-sc-1sq8hhn-0.khqeGV > button > span').text
        except NoSuchElementException:
            return True
        finally:
            # TODO figure out why I can't exit the program with this line
            self.driver.quit()

        if stock_string == "Sold out":
            return False
        else:
            return True


stock = Stock()
stock.load_url()
print(stock.check_stock())
# TODO figure out why I can't make this exit during exception handling in the function/class itself
stock.driver.quit()
