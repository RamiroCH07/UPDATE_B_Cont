import requests as req
from bs4 import BeautifulSoup as bs
import re

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
        
    def GET_ALL_RUCS(self):
        this_continue = True 
        new_page = 'BueCont0.html'
        while this_continue:
            url = self.ENDPOINT+new_page
            response = req.get(url,headers = self.headers)
            html = response.text
            soup = bs(html,'html.parser')
            ##RECUPERANDO LOS RUCS
            
            
            ##
            nextr = self._next_resource(soup)
            new_page = nextr[0]
            this_continue = nextr[1]
        
        
        
        
        
    
     
        
        
        
        

        
    
        
        
        
        
        
        
        
        
        
        

# FUNCION QUE COMPARE EL NUMERO DE REGISTROS DE LA PAGINA Y LA DE LA BASE DE DATOS

# FUNCION QUE RETORNE TODAS LOS RUCS 

# FUNCION QUE RETORNE LOS RUCS DE LOS ELE

