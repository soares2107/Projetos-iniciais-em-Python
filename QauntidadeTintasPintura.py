print('='*6,'Calculadora de tintas - Quantidade certa por m²','='*6,'\n')

altura = float(input('Informe a altura da parede: '))
comprimento = float(input('Informe o comprimento da parede: '))
AltJan = float(input('Informe a Altura da Janela: '))
LargJan = float(input('Informe a Largura da janela: '))
AltPort = float(input('Informe a altura da porta: '))
LargPort = float(input('Informe a largura da porta: '))
parede = altura * comprimento
janela = AltJan * LargJan
porta = AltPort * LargPort
area = parede - janela - porta
QuantidadeTin = area / pow(2,2)
latas = QuantidadeTin * 2
print('Sua parede tem dimensões {} x {} e sua área é de {:.0f} m².'.format(altura,comprimento,area))
print('Para pintar essa parede, você precisará de {:.2f} litros de tintas.'.format(latas))
print('='*66)

