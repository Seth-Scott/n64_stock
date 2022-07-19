from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./chromedriver"
URL = 'https://www.nintendo.com/store/products/nintendo-64-controller/'

SERVICE = Service(CHROME_DRIVER_PATH)
DRIVER = webdriver.Chrome(service=SERVICE)


def check_stock():
    """checks to see if the defined CSS selector says 'sold out'. Returns True if item is in stock, and False if it's
    not """
    # load the URL, wait for all of the javascript elements to load
    DRIVER.get(URL)
    DRIVER.implicitly_wait(10)

    # exception handling
    try:
        stock_string = DRIVER.find_element(By.CSS_SELECTOR,
                                           '#main > section.Herostyles__HeroSection-sc-1gi6jtj-0.kKfMBG > div > '
                                           'div.Herostyles__HeroInfo-sc-1gi6jtj-8.gAHENY > '
                                           'div.Gridstyles-sc-1sq8hhn-0.khqeGV > button > span').text
    except NoSuchElementException:
        return True
    finally:
        DRIVER.quit()

    if stock_string == "Sold out":
        return False
    else:
        return True


status = check_stock()

print(status)