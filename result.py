import requests
from bs4 import BeautifulSoup as bs
u=913013104001
while  u<=913013104053:
       r=requests.post('http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl',data={'regno':u})
#print r.content
       u=u+1
       s=bs(r.content,'lxml')
       for st in s.find_all('strong'):
           print st.string
           stra=str(st.string)
           stra=stra+'\n'
           with open('result.txt','a') as txtfile:
                txtfile.write(stra)
