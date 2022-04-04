a = [2,3,4,5,7]
b = a[:] # isso faz uma copia dos itens da lista, não associa uma na outra.
b[2] = 8
print(a)
print(b)



'''
valores = list()
for c in range(0,5):
	valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores): #enumerate mostra a posição do valor na lista.
	print(f'nas posições {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
'''

'''
valores = []
valores.append(5)
valores.append(6)
valores.append(7)
for c, v in enumerate(valores): #enumerate mostra a posição do valor na lista.
	print(f'nas posições {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
'''

'''
num = [0,9,6,7,5]
num[2] = 3
num.append(8) # append adiciona algo no fim da lista, enquanto o insert adiciona no inicio
num.sort(reverse=True) # sort vai organizar, se por entre parentesed com o reverse=True, mostra organizado ao contrario
num.insert(2,5)
num.pop(2)
num.remove()#remove procura a primeira ocorrencia do valor que quero eliminar
print(num)
print(f'essa lista tem {len(num)} elementos')
'''