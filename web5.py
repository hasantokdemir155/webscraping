import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk




imd='https://www.kariyer.net/is-ilanlari/antalya?ct=7&kw=sql&is=1'

r=requests.get(imd)
print('mmmmmmm')

soup=BeautifulSoup(r.text,'html.parser')




vr1=soup.find('div',{'class':'row no-gutters'})

ver2=vr1.find('div',{'class':'list-items-wrapper'})
vr2=soup.find_all('div',{'class':'list-items'},limit=15)



dz=[]


for i in vr2:

    sn=i.a['href']
    dz=sn.split('i/')
    print(dz[1])


