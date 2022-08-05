
In this project we get our data which are all laptops with details from digikala using beautiful soup and save them in the database .
mongoDB is used as database . and the program will be running every two days with crontab in linux .

scikit learn gets all data like {ram , cpu , model of the laptop , ...} and learns the price of the laptops .

so by inserting the detials of the laptop , the program will offer you a price and a link in digikala so you can buy your laptop .



Run the fetch_data.py for getting data from the site or updating your database (can be done by cronetab)
Run the machine.py for getting input from user to predict the laptop price.

In the first version of this code the internal memory is ignored which will be added in the close future
and the links of laptops will be shown in the new version for you to easy buy your favirote laptop


So first step is to clone the project using the link :

`git clone https://github.com/Al1r3z4asadi/laptop-recommend3r.git <Name of folder`

Then you have to make your virtualenv with the following command :
 
`python -m venv <virtualname>`

for the app to work you first have to install the requiments , to do so you have to run the code below :

`pip install -r requirments.txt`

Then there are two file to run . The fetch_data which gets data from digikala . 

`python fetch_data.py`

You can run this once at your terminal or do it with cronjob for having new datas . 

This actually gets data and save it in documnetbase database witch here mongoDB is used . 


The final step is to run :

`python machine.py`

This file gets the input from you and gives the suggeted budget for your laptop . 


Its too easy . 



Thanks for your time .



Team tim : )
