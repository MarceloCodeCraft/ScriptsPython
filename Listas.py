# Lista: representa uma seuquência de valores 

# Sintaxe: nome_lista = [valores]

# notas = [5, 7, 8, 6, 9]
# print(notas)

# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,11]
# valores = n1 + n2 
# print(valores)
# print(type(valores))
# valores[0] = 9
# # print(valores[-2:])
# print(len(valores))
# print(sorted(valores, reverse = True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))
# valores.append(13)
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,50)
# print(valores)
# print(50 in valores)
# planetas = ['Mercúrio' ,'Vênus', 'Terra', 'Marte','Saturno', 'Urano', 'Netuno' ]
# for planetas in planetas:
#     print(planetas)
# Solicita ao usuário que digite suas 5 bebidas favoritas
bebidas_favoritas = []
for i in range(5):
    bebida = input(f"Digite a {i+1}ª bebida favorita: ")
    bebidas_favoritas.append(bebida)

# Ordena a lista em ordem alfabética
bebidas_favoritas.sort()

# Exibe os elementos da lista em ordem alfabética usando um loop for
print("Bebidas favoritas em ordem alfabética:")
for bebida in bebidas_favoritas:
    print(bebida)
