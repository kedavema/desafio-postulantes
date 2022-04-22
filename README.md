# Desafio Fapro

## Scrapping de datos de una URL en específico

Se utilizó el siguente URL [Link](https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html).

Obs: se requiere utilizar el navegador de Google Chrome.

### Instalación y ejecución

1. Descargue o clone el proyecto.
2. Ejecutar en la consola, en la carpeta del proyecto:
~~~
python3 -m venv .env
~~~
3. Inicialice el ambiente virtual
~~~
source ./.env/bin/activate
~~~
4. Instale los requerimentos
~~~
pip install -r requirements.txt
~~~
5. Ejecute el programa
~~~
python3 main.py
~~~

Se imprimirán en consola los datos en formato DataFrame y en JSON, luego se generará un archivo .csv
