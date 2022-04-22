import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# URL para Scrapping de una tabla de datos
URL = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'

#Configuración de Selenium para el navegador Chrome
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Ingresamos a la url a travez de selenium y esperamos 2 minutos en caso de que
# el navegador sea lento para obtener todos los datos
website = driver.get(URL)
time.sleep(2)

#Extraemos los titulos de las cabeceras de la tabla
thead = driver.find_element_by_tag_name('thead')
columns = [th.text for th in thead.find_elements_by_tag_name('th')]

#Utilizamos BeautifulSoup para extraer el contenido del cuerpo de la tabla
soup = BeautifulSoup(driver.page_source,'html.parser')
tbody = soup.find('tbody')

#Iteramos y creamos una lista con los datos de cada fila
data = []
for td in tbody.find_all('tr'):
    row = [i.text for i in td.find_all('td')]
    data.append(row)

#Creamos un DataFrame para mostrar los datos
df = pd.DataFrame(data=data, columns=columns)

print(df)
print(df.to_json())

#Guardado de los datos en un archivo CSV
df.to_csv('datos.csv')
