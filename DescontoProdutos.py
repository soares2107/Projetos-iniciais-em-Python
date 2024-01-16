print('====== Desconto em Supermercado ======')
produto = str(input('Produto: '))
valor = float(input('Preço: R$ '))
preço = valor * 5/100
desconto = valor - preço
print('Produto: {}.'.format(produto))
print('Preço com desconto R$ {:.2F}.'.format(desconto))
print('='*16)      
