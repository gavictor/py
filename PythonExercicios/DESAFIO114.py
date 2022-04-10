import urllib
import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
	print(f'Não consegui ter acesso ao site.')
else:
	print(f'Consegui acessar o site, tudo ok!')