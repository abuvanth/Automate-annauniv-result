import requests
from bs4 import BeautifulSoup as bs
import csv
c=raw_input('Single Result or Bulk Result (S/B)..?')
if c=='b' or c=='B':
   u=int(raw_input("Enter Your starting Reg No "))
   n=int(raw_input("Enter Your Ending Reg No "))
   while  u<=n:  #ending Register number
       r=requests.post('http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl',data={'regno':u})
       u=u+1
       s=bs(r.content,'html.parser')
       a=[]
       f=open('audata-bulk.csv','a+')
       writer=csv.writer(f)
       a=[]
       for st in s.find_all('strong'):
           a.append(st.text)
       if len(a)!=6:
          while a:
               writer.writerow(a[:3])
               a=a[3:]
else:
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
