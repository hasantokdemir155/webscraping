import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk


######aynı çalışmanın 2 farklı yöntemi##########
######1,yöntem########


imd='https://www.allday.com.tr/tunik'
r=requests.get(imd)
soup=BeautifulSoup(r.text,'html.parser')


vr2=soup.find_all('div',{'class':'product-info'},limit=5)
#print(vr2)


for i in vr2:

    sn=i.text
    print(sn)

input()


#######2.yöntem########

#########olay burada bitiyor#########

imd='https://www.allday.com.tr/tum-urunler'

r=requests.get(imd)
soup=BeautifulSoup(r.text,'html.parser')
ver1=soup.findAll(class_="product-info")
#ver2=ver1.findAll(class_="link position")

sisters = soup.select(".product-price")


for sister in sisters:
    p=sister.string
    #print(p)

for x in ver1:
    m=x.text
    print(type(m))
    print(m)


###############burası####################    
