import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# disable the image
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs", prefs)

# set up the selenium web driver
driver = webdriver.Chrome(chrome_options=chromeOptions)

# go to the target website
# target = input("Target url: ")
target = 'https://translate.google.com/#en/nl/'
driver.get(target)

# get the articles
with open('50_spintax.csv', 'r') as f:
    texts = f.readlines()

listArticles = []
for text in texts:
    article = text.split('";"')
    article[0] = article[0][1:]
    article[-1] = article[-1][:-2].strip()
    listArticles.append(article)

articles = []
for idx, x in enumerate(listArticles, start=1):
    print('memulai artikel ke...', idx)
    article = []
    input("mulai translate\n")
    
    for x_ in x:
        driver.find_element_by_id("source").clear()
        
        if (len(x_) < 5000):
            driver.find_element_by_id("source").send_keys(x_)
            input("pendek...\n")
            driver.find_element_by_id("gt-submit").click()
            time.sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            hasil = soup.select('span#result_box > span')
            hasil_akhir = []
            for hasil_ in hasil:
                hasil_akhir.append(hasil_.text)
            hasil_akhir = " ".join(hasil_akhir)
            article.append(hasil_akhir)
        else:
            # split the content
            x__ = x_.split(' #### ')
            x__ = list(filter(None, x__))
            x__ = [x + ' #### ' for x in x__]
            
            #translate every list item then save to list
            hasil_akhir = []
            for x__item in x__:
                driver.find_element_by_id("source").send_keys(x__item)
                input("panjang...\n")
                driver.find_element_by_id("gt-submit").click()
                time.sleep(2)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                hasil = soup.select('span#result_box > span')[0].text + ' #### '
                hasil_akhir.append(hasil)
                driver.find_element_by_id("source").clear()
            hasil_akhir = " ".join(hasil_akhir)
            
            article.append(hasil_akhir)
    articles.append(article)

with open('50_final.csv', 'w') as f:
    for a_ in articles:
        a_ = '"{}";"{}";"{}";"{}"'.format(a_[0],a_[1],a_[2],a_[3])
        f.write(a_ + '\n')

print("program selesai")
