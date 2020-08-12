import requests
from bs4 import BeautifulSoup
import sys , time
import re

url = 'https://www.digikala.com/search/category-notebook-netbook-ultrabook/'
plink = 'https://www.digikala.com'
for i in range(1,6):
    req = requests.get(url, params={'pageno':i})
    soup = BeautifulSoup(req.text , 'html.parser')
    link_products = soup.find_all('a' , class_='c-product-box__img c-promotion-box__image js-url js-product-item js-product-url')
    for link in link_products:

        lap_detail = plink + link['href'] + '#/tab-params'
        time.sleep(0.1)
        detail_req = requests.get(lap_detail)
        detail_soup = BeautifulSoup(detail_req.text , 'html.parser')
        articles = detail_soup.find_all('article')
        
        sectoins = articles[-1].find_all('section')
        good_sectoins = sectoins[1:5]
        
        # {0 : pardazande , 1 : ram , 2 : hafeze dakheli , 3 : pardazende geraphic}

        info = dict()
        for k , gs in enumerate(good_sectoins):    
            lis  = gs.ul.find_all('li')
            print(i)
            for j in range(len(lis)):
                if k == 0 : 
                    if j == 2 or j == 3 or j == 4 : 
                        continue 
                if k == 2: 
                    if j != 0 :
                        continue 

                key = lis[j].find('div' , class_="c-params__list-key")
                value = lis[j].find('div' , class_='c-params__list-value')

                if key.a != None:   
                    key = key.a.text
                else : 
                    key = key.text
                if value.a != None :
                    value = value.a.text
                else :
                    value = value.text 
                key = re.sub(r'\s+' , ' ' , key)
                value = re.sub(r'\s+' , ' ' , value)
                info[key] = value
        
        # for key , value in info.items():
            # print("key is " , key , " value is " , value)
        
        


