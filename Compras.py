print('============== Compras ==============')
produto = str(input('Produto: '))
valor = float(input('R$ '))
vista = valor - (valor * 10 / 100)
prazo = valor + (valor * 8 / 100)
parcela = prazo / 12
print('Produto: {}.\n'.format(produto))
print('R$ {:.2f} à vista [com 10% de desconto].'.format(vista))
print('Ou 12 x de R$ {:.2f} com juros [8% de juros].'.format(parcela))
print('=' * 66)

