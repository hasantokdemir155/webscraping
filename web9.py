import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk



#########olay burada bitiyor#########

imd='https://www.toyota.com.tr/dealers/index.json'

r=requests.get(imd)
soup=BeautifulSoup(r.text,'html.parser')
#print(soup)

ver1 = soup.find_all("div",attrs={"class":"col-xs-12 col-sm-6 col-md-3"})
print(ver1)           



f2= open("okh.txt", "r")

while True:
        
        m=f2.readline()
        if m != "" :
            
            print(m)
            
        
   

ver2 = ver1.find_all("strong")



halt


###############burası####################    


lstx2.pack()    

