print('=== Conversor de unidades ===')
metros = float(input('Metros(m): '))
print('\n=== Conversões ===')
print('Decímetro: {:.0f} dm.'.format(metros * 10))
print('Centrimetro: {:.0f} cm'.format(metros * 100))
print('Milimetro: {:.0f} mm.'.format(metros * 1000))
print('Diâmetro: {} dam.'.format(metros / 10))
print('Hectômetro: {:.4} hm.'.format(metros / 100))
print('Kilometro: {} km.'.format(metros / 1000))