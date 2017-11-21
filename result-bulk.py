import requests
from bs4 import BeautifulSoup as bs
import csv
u=int(raw_input("Enter Your starting Reg No "))
n=int(raw_input("Enter Your Ending Reg No "))
while  u<=n:  #ending Register number
       r=requests.post('http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl',data={'regno':u})
       u=u+1
       s=bs(r.content,'html.parser')
       a=[]
       f=open('audata.csv','a+')
       writer=csv.writer(f)
       a=[]
       for st in s.find_all('strong'):
           a.append(st.text)
       if len(a)!=6:
          while a:
               writer.writerow(a[:3])
               a=a[3:]
