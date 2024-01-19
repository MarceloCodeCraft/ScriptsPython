# Escopos Globla e local

var_global = 'Curso Completo de Python'

def escreve_texto():
    var_local ='Marcelo Nascimento de Jesus'
    print (f'Variável Global: {var_global}')
    print (f'Varável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()
    print ('tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
    # print(f'Vara´vel Local: {var_local}')
