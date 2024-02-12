# Import library yang dibutuhkan
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Buat sebuah permintaan HTTP ke website Tokopedia
def get_data(keyword,pages):
    URL = "https://www.tokopedia.com/search?st=&q="
    url_target = URL+keyword
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url_target)

    data = {}
    
    for i in range(0,pages):
        for _ in range(0, 7000, 500):
            time.sleep(1)
            driver.execute_script("window.scrollBy(0,500)")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        containers = soup.findAll('div', attrs = {'class':'css-54k5sq'})
        count = (i * 85)+1
        for container in containers:
            try:
                rating = container.find('span', attrs = {'class':'prd_rating-average-text css-t70v7i'})
                if rating is None:
                    rating = ""
                else:
                    rating = container.find('span', attrs = {'class':'prd_rating-average-text css-t70v7i'}).text
                terjual = container.find('span', attrs = {'class':'prd_label-integrity css-1sgek4h'})
                if terjual is None:
                    terjual = ""
                else:
                    terjual = container.find('span', attrs = {'class':'prd_label-integrity css-1sgek4h'}).text
                diskon = container.find('div', attrs = {'class':'prd_badge-product-discount css-1xelcdh'})
                if diskon is None:
                    diskon = ""
                else:
                    diskon = container.find('div', attrs = {'class':'prd_badge-product-discount css-1xelcdh'}).text
                harga = container.find('div', attrs = {'class':'prd_label-product-slash-price css-xfl72w'})
                if harga is None:
                    harga = ""
                else:
                    harga = container.find('div', attrs = {'class':'prd_label-product-slash-price css-xfl72w'}).text
                data[count] = {
                "Nama Produk": container.find('div', attrs = {'data-testid':'spnSRPProdName'}).text,
                "Rating": rating,
                "Nama Toko": container.find('span', attrs = {'class':'prd_link-shop-name css-1kdc32b flip'}).text,
                "Lokasi Toko": container.find('span', attrs = {'class':'prd_link-shop-loc css-1kdc32b flip'}).text,
                "Terjual": terjual,
                "URL": container.find('img', attrs = {'class':'css-1q90pod'})['src'],
                "Diskon": diskon,
                "Harga Diskon": container.find('div', attrs = {'class':'prd_link-product-price css-h66vau'}).text,
                "Harga Normal": harga
                }
                count += 1
            except AttributeError:
                continue
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,-500)")

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
        time.sleep(3)
    return data