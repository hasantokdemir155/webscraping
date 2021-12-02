import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk





imd='https://www.imdb.com/chart/top/'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')
vr3=soup.find('tbody',{'class':'lister-list'}).find_all('tr',limit=10)

for i in vr3:

    sn=i.find('td',{'class':'titleColumn'}).find('a').text
    print(sn)


     


    
 

