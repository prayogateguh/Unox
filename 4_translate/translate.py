import time
import sys

import urllib.error

import goslate


with open('single_spintax.csv', 'r') as f:
    texts = f.readlines()

listArticles = []
for text in texts:
    article = text.split('";"')
    article[0] = article[0][1:]
    article[-1] = article[-1][:-2].strip()
    listArticles.append(article)

gs = goslate.Goslate()

articles = []
for idx, x in enumerate(listArticles, start=1):
    print('Processing...', idx)
    article = []
    for x_ in x:
        time.sleep(5)
        try:
            hasil = gs.translate(x_, 'nl')
            article.append(hasil)
        except urllib.error.HTTPError:
            print("503: your process have been rejected by Google... :(")
            break
        print("translating...")

    time.sleep(30)
    articles.append(article)

#print(article)
#sys.exit()

with open('50_hasil.csv', 'w') as f:
    for a_ in articles:
        #pass
        #print(a_)
        a_[3] = a_[3].replace("</ p>", "</p>")
        a_[3] = a_[3].replace("<p> ", "<p>")
        a_[3] = a_[3].replace("</ p>", "</p>")
        a_[3] = a_[3].replace(" </p>", "</p>")
        a_[3] = a_[3].replace("</ P>", "</p>")
        a_[3] = a_[3].replace(" <p>", "<p>")
        a_ = '"{}";"{}";"{}";"{}"'.format(a_[0],a_[1],a_[2],a_[3])
        f.write(a_ + '\n')

print("Program selesai")
