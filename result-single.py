import requests
from bs4 import BeautifulSoup as bs
import csv
u=int(raw_input("Enter Your Reg No "))
r=requests.post('http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl',data={'regno':u})
s=bs(r.content,'html.parser')
f=open('audata-single.csv','a+')
writer=csv.writer(f)
a=[]
for st in s.find_all('strong'):
       a.append(st.text)
if len(a)!=6:
   while a:
         writer.writerow(a[:3])
         a=a[3:]
