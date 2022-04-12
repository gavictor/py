from bs4 import BeautifulSoup
from requests import *
from time import sleep

site = get("https://www.climatempo.com.br/").content
# objeto  site recebendo todo o conteúdo do site.
soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixando do site o html

#print(soup.prettify())
#transforma o html em string
print(soup.title.string)
sleep(3)