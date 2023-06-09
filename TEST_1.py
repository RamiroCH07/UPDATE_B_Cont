from bs4 import BeautifulSoup

#%%

f = open('html_test.txt','r')
html = f.read()
f.close()

#%%

soup = BeautifulSoup(html,'html.parser')

table = soup.find_all('table',cellpadding = '2')[0]
trs = table.find_all('tr')

print(trs[8].find('td').find('a').get_text())

#%%

print(len(trs[0].find_all('td',class_ = 'bg')))

#%%
for tr in trs:
    
    is_my_tr = len(tr.find_all('td',class_ = 'bg')) != 0
    if is_my_tr:
        print(tr.find('td').find('a').get_text())
    
#%%    
##print(tr.find('td').find('a').get_text()) 


a = ['a','b','y','afsa','qwe']
b = ['n','zx','qasd','lpoki']
vac = []
c = a+b
d = c+vac
print(d)
#%%
import re 

txt = 'BueCont1513.html'
print(re.search('[0-9]+',txt).group())




