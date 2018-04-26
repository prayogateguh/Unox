import time
import csv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import openpyxl


# setting up the openpyxl
wb = openpyxl.Workbook()
ws = wb.active

# setting up chorome
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs", prefs)

# set up the selenium web driver
driver = webdriver.Chrome(chrome_options=chromeOptions)

# go to the target website
# target = input("Target url: ")
target = 'http://www.businessinsurance.com/'
driver.get(target)

# Getting the urls from 'unik.txt' file
f = open("1000.txt", "r", encoding="utf-8", errors="ignore")
urls = f.readlines()
f.close()

# scraping an article
articles = []
def single_article(idx, url):
    print('Downloading {} - {}'.format(idx, url))
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')  
    
    article = []
    
    try:
        title = soup.select('h2.headArticle')[0].text
    except:
        title = '<No Title>'
    
    try:
        main_cat = soup.select('label.mngtag')[0].text
    except:
        main_cat = ''
    
    cats = []
    try:
        all_cats = soup.select('span.tags')
    except:
        all_cats = []
    if all_cats:
        for cat in all_cats:
            cats.append(cat.text)
    else:
        cats = ['']
    cats = ', '.join(cats)
        
    contents = []
    try:
        article_contents = soup.select('div.cmnleft > div.articledetailbox p')
    except:
        article_contents = []
    if article_contents:
        for article_content in article_contents:
            if (article_content.text.strip()):
                paragraf = " ##### {} #### ".format(article_content.text.strip())
                paragraf = paragraf.replace('\n', ' ')
                contents.append(paragraf)
    else:
        contents = ['']
    contents = ''.join(contents)
        
    article.append(title)
    article.append(main_cat)
    article.append(cats)
    article.append(contents)
    
    articles.append(article)
    
# scrape all articles from the url_list
def grab_all():
    for idx, url in enumerate(urls, 1):
        try:
            single_article(idx, url)
        except:
            continue
        time.sleep(3)
        
# save to csv
def save_csv(l):
    with open("1000.csv","w",newline="") as f:
        cw = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        cw.writerows(r for r in l)
    
if __name__ == "__main__":
    input('Bisa dimulai? (Enter to continue)')
    grab_all() # grab all articles data
    l = articles[:]
    save_csv(l) # save it to csv

    print("---Grabbed all data, program finished run")

