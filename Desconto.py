print('======== Desconto em Supermercado ========')
produto = str(input('Produto: '))
preço = float(input('Qual é o valor do seu Produto: R$ '))
desconto = preço - (preço * 5/100)
print('O produto {} que custava R$ {:.2F},na promoção com desconto de 5% vai custar R$ {:.2f}.' .format(produto,preço, desconto))
print('='*36)   

