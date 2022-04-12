from hashlib import *

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
	print(f'Hash 1 é diferente de Hash 2')
	print(f'O hash do arquivo a.txt é: {hash1.hexdigest()}')
	print(f'O hash do arquivo b.txt é {hash2.hexdigest()}')
else:
	print(f'Hash 1 e 2 são iguais.')
	print(f'O hash do arquivo a.txt é: {hash1.hexdigest()}')
	print(f'O hash do arquivo b.txt é {hash2.hexdigest()}')