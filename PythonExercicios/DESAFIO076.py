print('-'*30)
print('{:^30}'.format('Listagem Preços'))
print('-'*30)
itens = ('Lapis',1.75,'Borracha',2.0,'Caderno',15.90,
		 'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,
		 'Mochila',120.32,'Canetas',22.30,'Livros',40.90)

for pos in range(0,len(itens)):
	if pos % 2 == 0:
		print(f'{itens[pos]:.<25}',end=' ')
	else:
		print(f'R${itens[pos]:>.2f}')

#print(f'''
#	  {itens[0]}........ R${itens[1]}
#	  {itens[2]}........ R${itens[3]}
#	  {itens[4]}........ R${itens[5]}
#	  {itens[6]}........ R${itens[7]}
#	  {itens[8]}........ R${itens[9]}
#	  {itens[10]}........ R${itens[11]}
#	  {itens[12]}........ R${itens[13]}
#	  {itens[14]}........ R${itens[15]}
#	  {itens[16]}........ R${itens[17]}
#	  ''')
#print('-'*30)