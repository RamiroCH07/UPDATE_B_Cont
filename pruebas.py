###PRUEBAS###
import requests as req
from lxml import etree
from bs4 import BeautifulSoup as bs
#%%
url = 'https://ww3.sunat.gob.pe/descarga/BueCont/BueCont0.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
response = req.get(url,headers = headers)
html = response.text
#%%
soup = bs(html,'html.parser')
table = soup.find_all('table',cellpadding="2")[1]
trs = table.find_all('tr')
#%%
print(trs[8].find('td').find('a').get_text)
#%%


#%%%
trs = tbody.parents

#%%
for tr in trs:
    td = tr.find('td')
    ruc = td.find('a').get_text
    print(ruc)