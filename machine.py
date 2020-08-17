from pymongo import MongoClient
from mongoengine import *
from mongo_connect import Product
import seaborn as sns
import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn import tree , preprocessing
import get_user_input
# define a generator for reading database



# def clean_mongo_data():
#     pass




def read_mongo(cursor):
    for doc in list(cursor):
        yield doc


mongo_client = MongoClient('localhost', 27017)
db = mongo_client.laptops
col = db.product
cursor = col.find()
 
docs = []
# mongo_docs = list(cursor)
what_not_need = ['ظرفیت حافظه داخلی' , 'محدوده سرعت پردازنده'   , 'link' , 'فرکانس پردازنده' , 'مدل پردازنده' ,'مدل پردازنده گرافیکی' ,'نوع حافظه داخلی' , 'مشخصات حافظه داخلی' ,'نوع حافظه RAM']

# print(mongo_docs[0])



for mongo_doc in read_mongo(cursor):
    pddoc = {}
    find_values = r'\d+'
    for key ,value in mongo_doc.items():
        if key in what_not_need:
            continue
        elif key == 'سازنده پردازنده' :
            key = 'processor'
        elif key == 'سری پردازنده' :
            key = 'sprocessor'
        elif key == 'حافظه Cache':
            key = 'cacheM'
            value = float(re.search(find_values,value).group())
        elif key == 'ظرفیت حافظه RAM':
            key = 'RAMM'
            value = float(re.search(find_values,value).group())
        elif key == 'سازنده پردازنده گرافیکی':
            key = 'Graphic'
        elif key == 'حافظه اختصاصی پردازنده گرافیکی':
            key = 'GraphicM'
            value = re.search(find_values , value)
            if value == None :
                value = 0 
            else:
                value = float(value.group())
                if value > 16 :
                    value = value / 1000
        elif key =='_id' :
            key = 'brand'
            value = value.split()
            if(value == []):
                value = 'asus'
            else :
                value = value[0].lower()

        pddoc[key] = value
    docs.append(pddoc)


# ****************************************************************************************
# trying to get internal memory

# for mongo_doc in mongo_docs:
#     for key , value in mongo_doc.items():
        
#         if key == 'ظرفیت حافظه داخلی':
#             print(value)
#             # print(mongo_doc['link'])
#             print(mongo_doc['مشخصات حافظه داخلی'])
#             print(mongo_doc['نوع حافظه داخلی'])
#             print('\n\n\n')
#             pddoc['SSD'] = 512
#             pddoc[''] = 1000
#             continue
#         pddoc[key] = value
#     docs.append(pddoc)

# print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
# print("docs is " , docs[:4])



# ***************************************************************************************
# IN first version of this , we will ignore the internal memory just to test the program
#****************************************************************************************

# print(docs)
data = pd.DataFrame(docs)


# print("fucking data is \n\n\n" , data)
# data.to_csv('/home/alireza/Python/jadi/project/lproj/laptops.csv')



output = data['price']

# oe = preprocessing.OrdinalEncoder()
# t_data = oe.fit_transform(data.drop(prcess_string , axis=1))


not_prcess_string = ['price' , 'cacheM' , 'GraphicM' , 'RAMM']

df_to_process = data.drop(not_prcess_string , axis=1)
prcessed_df = df_to_process.apply(preprocessing.LabelEncoder().fit_transform)


processe_string = ['brand' , 'processor' , 'Graphic' , 'sprocessor']
float_df = data.drop(processe_string , axis=1)
concated_df = pd.concat([prcessed_df,float_df], axis=1, sort=False)
# print(concated_df)



a = list(data['brand'])
b = list(concated_df['brand'])
brand_co = dict((x, y) for x, y in zip(a, b))
# print("brans are " , brand_co)

a = list(data['processor'])
b = list(concated_df['processor'])
processor_co = dict((x, y) for x, y in zip(a, b))
# print("processors are " , processor_co)


a = list(data['Graphic'])
b = list(concated_df['Graphic'])
Graphic_co = dict((x, y) for x, y in zip(a, b))
# print("graphics are " , Graphic_co)



a = list(data['sprocessor'])
b = list(concated_df['sprocessor'])
sprocessor_co = dict((x, y) for x, y in zip(a, b))
# print("seri processors are " , sprocessor_co)

clr = tree.DecisionTreeRegressor()
clr = clr.fit(concated_df.drop(['price'] , axis=1) , output)



# getting input from user
brand = get_user_input.get_brand()
cacheM = get_user_input.get_cache()
Graphic_m = get_user_input.get_GraphicM()
graphic = get_user_input.get_Graphic()
processor = get_user_input.get_processor()
sprocessor = get_user_input.get_sprocessor()
ram = get_user_input.get_ram()
# print("graphic is " , graphic)
# print(Graphic_co[graphic])
predict_this = [ brand_co[brand] , processor_co[processor] , Graphic_co[graphic],
                sprocessor_co[sprocessor],  cacheM , Graphic_m  ,
                 ram ]

# print(predict_this)

ans = clr.predict([predict_this])
print(ans[0])







