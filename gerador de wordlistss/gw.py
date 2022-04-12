from itertools import *
from time import sleep

string = input('string a ser permutada: ')
resultado = permutations(string, len(string))

for i in resultado:
	print(''.join(i))
	sleep(1.5)