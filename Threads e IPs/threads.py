from threading import Thread
from time import sleep

def carro(velocidade, piloto):
	trajeto = 0
	while trajeto <= 100:
		trajeto += velocidade
		sleep(0.5)
		print(f'Piloto: {piloto}, {trajeto}')


t_carro1 = Thread(target=carro, args=[1, 'Gabriel'])
t_carro2 = Thread(target=carro, args=[1.5, 'Python'])

t_carro1.start()
t_carro2.start()
