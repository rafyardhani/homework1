from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Scraper:
  def __init__(self):
    self.driver = webdriver.Firefox()

  def get_data(self,product_name):
    url = "https://www.tokopedia.com/search?st=&q=" +product_name
    self.driver.get(url)
    
    counter_page = 0
    datas = []

    while counter_page < 10:
      for _ in range(0, 6500, 500):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")

    #   elements = self.driver.find_elements(by=By.CLASS_NAME, value='divProductWrapper')
    #   print(elements)
    #   for element in elements:
    #     # img = element.find_element(by=By.CLASS_NAME, value='css-1c345mg').get_attribute('src')
    #     name = element.find_element(by=By.CLASS_NAME, value='spnSRPProdName').text
    #     price = element.find_element(by=By.CLASS_NAME, value='css-h66vau').text
    #     city = element.find_element(by=By.CLASS_NAME, value='css-1kdc32b').text

    #     datas.append({
    #     #   'img': img,
    #       'name': name,
    #       'price': price,
    #       'city': city
    #     })

      counter_page += 1
      next_page = self.driver.find_element(by=By.XPATH, value='//button[text()="' + str(counter_page + 1) + '"]')
      next_page.click()
    
    return datas