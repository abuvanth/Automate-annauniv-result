import requests,csv
from bs4 import BeautifulSoup as bs
url="http://cdn.b-u.ac.in/res_may2017/bsc.php"
data=requests.post(url,data={'rno':'1522J0371'})
sp=bs(data.content,'html.parser')
a=[]
f=open('budata.csv','a+')
writer=csv.writer(f)
for i in sp.find_all('tr'):
    data= i.text.split('\n')
    res=[x for x in data if x]
    a.append(res)
writer.writerow(['','',a[0][0],a[0][1]])
writer.writerow(['','',a[1][0],a[1][1]])
writer.writerow([a[2][0],a[2][1],a[2][2],a[2][3]])
b=a[3:]
for i in b:
    writer.writerow([i[0],i[1],i[2],i[3]])
print "success"
