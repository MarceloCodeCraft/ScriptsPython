# Simples, Composto, Encadeado 
n1 = n2 = 0.0
media = 0.0

n1 = float(input('digite a primeira nota.'))
n2 = float(input('digite a segunda nota.'))

# Calcular a média aritimetica das notas
media = (n1 + n2) / 2

if (media >= 7):
    print('resultado: aprovado! ')
    print('Parabéns!')
elif (media >= 5):
    print ('voce esta de recuperação!!! ')    
else: 
    print('aluno reprovado...')

print('Sua média é {}'.format(media))    
