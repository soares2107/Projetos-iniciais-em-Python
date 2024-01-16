print('='*11,'Conversor de Medidas','='*11)

metros = float(input('Metros(m): '))
Decimetro = metros * 10
Centimetros = metros * 100
Milimetros = metros * 1000
Diametro = metros / 10
hectometro = metros / 100
kilometro = metros / 1000
print('================ Conversões ================')
print('Decimetro: {:.0f} dm.'.format(Decimetro))
print('Centimetros: {:.0f} cm.'.format(Centimetros))
print('Milimetros: {:.0f} mm.'.format(Milimetros))
print('Diâmetro: {:.2f} dam.'.format(Diametro))
print('Hectometro: {:.4f} hm.'.format(hectometro))
print('Kilometro: {:.4f} km.'.format(kilometro))
print('='*44)
