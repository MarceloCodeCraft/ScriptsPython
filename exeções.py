# exceção um obejto que representa um erro que ocorreu ao executar o program....
# Blocos, try ... except

n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))

try:
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print(f' ///Não é possivél dividir por Zero///')
else:
    print(f'Resultado:{r}')