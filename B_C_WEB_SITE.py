import requests as req
from bs4 import BeautifulSoup as bs
import re
from time import sleep

#%%
class B_C_WEB_SITE:
     
    def __init__(self):
        self.ENDPOINT = 'https://ww3.sunat.gob.pe/descarga/BueCont/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

    def GET_NUM_ROWS(self):
        url = self.ENDPOINT+'BueCont0.html'
        response = req.get(url,headers = self.headers)
        html = response.text
        soup = bs(html,'html.parser')
        etiq_td = soup.find_all('td',align = 'center')[1]
        #Recupera el intervalo
        text_td = etiq_td.get_text()
        num_rows = re.findall('[0-9]+', text_td)[1]
        return num_rows
    
    def _next_resource(self,soup):
        etiq_td = soup.find('td',align = 'right')
        #OBTENER EL VALOR DE ATRIBUTO DE UNA ETIQUETA
        try:
            etiq_a = etiq_td.find('a').attrs
            return etiq_a['href'],True
        except:
            return None,False
    
    def _get_rucs(self,soup):
        rucs = []
        table = soup.find_all('table',cellpadding = '2')[0]
        trs = table.find_all('tr')
        for tr in trs:
            is_my_tr = len(tr.find_all('td',class_ = 'bg')) != 0
            if is_my_tr:
               ruc =  tr.find('td').find('a').get_text()
               rucs.append(ruc)
        return rucs
        
    def GET_ALL_RUCS(self):
        this_continue = True 
        new_page = 'BueCont0.html'
        all_rucs = []
        while this_continue:
            url = self.ENDPOINT+new_page
            response = req.get(url,headers = self.headers)
            html = response.text
            soup = bs(html,'html.parser')
            ##RECUPERANDO LOS RUCS
            #print('RECUPERANDO DEL RECURSO NUMERO: '+ re.search('[0-9]+',new_page).group())
            print(url)
            all_rucs = all_rucs + self._get_rucs(soup)
            ##
            nextr = self._next_resource(soup)
            new_page = nextr[0]
            this_continue = nextr[1]
            #sleep(1)
        return all_rucs
    
    def CRAWLING_TEST(self):
        num_page_error = []
        for i in range(2535):
            url = f'https://ww3.sunat.gob.pe/descarga/BueCont/BueCont{i}.html'
            try:
                response = req.get(url,headers = self.headers,timeout = 3)
                print(f'Conexion exitosa pagina {i}', response.status_code)
            except:
                print(f'No se establecio conexion pagina {i}')
                num_page_error.append(i)
        return num_page_error
                
                
                
            
    
    
    
    
    
        