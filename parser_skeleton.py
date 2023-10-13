# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:11:13 2022

Skeleton code for HTML parsing. 

@author: lcuev
"""
import requests 
from bs4 import BeautifulSoup 
import csv

# initialize list(s) where you will store your data
texts = []

# load in the web page(s) you will be parsing
page = requests.get('https://en.wikipedia.org/wiki/Jack_and_Jill')

# create a soup object from the web page you imported 
soup = BeautifulSoup(page.content, 'html.parser')

# this is the tricky part
# you need to look through the HTML tags in the web page
# and find which ones correspond to the data you need
# (in this case I am getting all <p> tags, which i assume is short for paragraph)
# you can do this using the inspect element funtion on your computer 
# or Beautiful Soup itself
peas = soup.find_all('p')


# for every <p> tag, store the text it marks into your data list
for pea in peas:
    # get the text marked by <p>
    text = pea.get_text()
    
    # add the text to your data list
    texts += [text]





# save the file to your computer as a csv file 
with open('texts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([[text] for text in texts])




    
    

    
    
        




            
    