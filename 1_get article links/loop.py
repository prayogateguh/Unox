import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os


chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs", prefs)

# set up the selenium web driver
driver = webdriver.Chrome(chrome_options=chromeOptions)

# go to the target website
# target = input("Target url: ")
target = 'http://www.businessinsurance.com/'
driver.get(target)

# clean up the header
driver.execute_script("document.getElementsByClassName('header')[0].style.position = 'relative';")
driver.execute_script("document.getElementsByClassName('liveSlider')[0].style.position = 'relative';")
driver.execute_script("document.getElementById('dvMenuHeader').style.position = 'relative';")

# scraping article
article_links = []
def save_article():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')  
    
    articles = soup.select('li.article > span.sponsoredbox > h3 > a')
    for article in articles:
        article_links.append(article.get('href'))
    
    f = open("article_links.txt", "w", encoding='utf-8')
    f.write("\n".join(map(lambda x: str(x), article_links)) + "\n")
    f.close()

def loop_nav():
    while True:
        try:
            driver.find_element_by_css_selector('span.loadmore > a').click()
            time.sleep(1)
        except:
            try:
                time.sleep(5)
                driver.find_element_by_css_selector('span.loadmore > a').click()
            except:
                break
        try:
            elem = driver.find_element_by_css_selector('span.loadmore > a')
            driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        except:
            print("Habis")

    save_article();
    
if __name__ == "__main__":
    loop_nav()
    print("Finished")

