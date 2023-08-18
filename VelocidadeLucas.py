velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado')
    multa = (velocidade-80) * 7
    multa('Você foi multado em {:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança')