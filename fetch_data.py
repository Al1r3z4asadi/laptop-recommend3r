import requests
from bs4 import BeautifulSoup
import sys , time , re
from mongo_connect import Product


def translate_price(price):
    newprice = ''
    for i in price:
        if i == ',':
            continue
        newprice += chr((ord(i) - 1728))
    return float(newprice)




counters = 0 





url = 'https://www.digikala.com/search/category-notebook-netbook-ultrabook/'
plink = 'https://www.digikala.com'
info = dict()

for i in range(1,6):
    req = requests.get(url, params={'pageno':i})

    soup = BeautifulSoup(req.text , 'html.parser')
    link_products = soup.find_all('a' , class_='c-product-box__img c-promotion-box__image js-url js-product-item js-product-url')
    for link in link_products:
        
        lap_detail = plink + link['href'] + '#/tab-params'
        time.sleep(0.5) #sleep for preventing too many requests
        # print(lap_detail)
        detail_req = requests.get(lap_detail)
        info['link'] = detail_req.url
        detail_soup = BeautifulSoup(detail_req.text , 'html.parser')
        articles = detail_soup.find_all('article')
        info['title'] = articles[-1].h2.span.text
        price = detail_soup.find('div' , class_='c-product__seller-price-raw js-price-value')
        info['price'] =   translate_price(re.sub(r'\s+' , ' ' , price.text.strip()))
       
        sectoins = articles[-1].find_all('section')
        good_sectoins = sectoins[1:5]
        
        # {0 : pardazande , 1 : ram , 2 : hafeze dakheli , 3 : pardazende geraphic}
        
        for k , gs in enumerate(good_sectoins):    
            lis  = gs.ul.find_all('li')
            for j in range(len(lis)):
                # if k == 0 : 
                #     if j == 2 or j == 3 or j == 4 : 
                #         continue 
                # if k == 2: 
                #     if j != 0 :
                #         continue 

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
        
        laptop = Product()
        laptop['title'] = info['title']
        laptop['link'] = info['link']
        counters+=1
        # print(info)
        for key , value in info.items():
            if key == 'title':
                continue
            laptop[key] = value
        laptop.save()
