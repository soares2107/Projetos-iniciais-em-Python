print('=========== Conversor de Moedas ===========') 
valor = float(input('Insira quantia em Real(BRL):'))
dolar = valor/4.72
print('Valor a converter - R$ {:.2f}.'.format(valor))
print('Resultado da conversão para Dolar(USD): US$ {:.4f}'.format(dolar))
print('='*46)