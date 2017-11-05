import requests
from bs4 import BeautifulSoup as bs
#u=913013104001  #starting Register  number
u=int(raw_input("Enter Your starting Reg No "))
n=int(raw_input("Enter Your Ending Reg No "))
while  u<=n:  #ending Register number
       r=requests.post('http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl',data={'regno':u})
#print r.content
       u=u+1
       s=bs(r.content,'html.parser')
       for st in s.find_all('strong'):
           print st.string
           stra=str(st.string)
           stra=stra+'\n'
           with open('result.txt','a') as txtfile:
                txtfile.write(stra)
