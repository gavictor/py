from ipaddress import *
from  time import sleep

ip = '192.168.0.100/24'

rede = ip_network(ip, strict=False)

for ip in rede:
	print(f'{ip}')
	sleep(1)