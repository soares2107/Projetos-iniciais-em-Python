print('======== Conversor de Temperatura ========')
#Converter Celsius para Fahrenheit e Kelvin
C = float(input('Informe a Temperatura em Celsius(ºC): '))
F = C * 1.8 + 32
K = C + 273
print('A temperatura de {:.0f}ºC corresponde à {:.0f}ºF.'.format(C,F))
print('A temperatura de {:.0f}ºC corresponde à {:.0f}ºK.'.format(C,K))
print('============================================')

#Converter Fahreneit em Celsius e Kelvin
F = float(input('Informe a Temperatura em Fahrenheit(ºF): '))
C = (F - 32) / 1.8
K = (F - 32) * 5/9 + 273
print('A temperatura de {:.0f}ºF corresponde à {:.0f}ºC.'.format(F,C))
print('A temperatura de {:.0f}ºF corresponde à {:.0f}ºK.'.format(F,K))
print('============================================')

#Converter Kelvin em Celsius e Fahrenheit
K = float(input('Informe a temperatura em Kelvin(ºK)  '))
C = K - 273
F = (K - 273) * 1.8 + 32
print('A temperatura de {:.0f}ºK corresponde à {:.0f}ºC.'.format(K,C))
print('A temperatura de {:.0f}ºK corresponde à {:.0f}ºF.'.format(K,F))
print('============================================')



