print('============ Aluguel de Carros ============')
dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos quilometros rodados: '))
pagar = (dias * 60)+(km * 0.15)
print('Total a pagar R$ {:.2f}.'.format(pagar))
print('='*43)
