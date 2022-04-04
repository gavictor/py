print('===== Desafio 011 =====')
print('Vamos Ver A Quantia de Tinta Necessária Para  Sua Parede!')
larg = float(input('Digite a largura de sua parede em metros: '))
alt = float(input('Digite a altura de sua parede em metros: '))
área = alt*larg
tinta = área / 2 
print(f'sua parede tem a dimensão de {larg}x{alt} e sua área é de {área:.3f}m²')
print(f'a quantia de tinta necessária para {larg}m de largura e {alt}m de altura são {tinta:.3f} litros de tinta')