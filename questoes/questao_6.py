## QUESTÃO 6 ##
# Escreva um programa que calcule a porcentagem de nucleotídeos A, C, G e T em 
# uma cadeia de DNA informada pelo usuário. Indicar também a quantidade e a 
# porcentagem de nucleotídeos inválidos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    cadeia = input('Me informe a cadeia de DNA: ').upper()
    total = len(cadeia)
    a = (100 * cadeia.count('A')) / total
    t = (100 * cadeia.count('T')) / total
    c = (100 * cadeia.count('C')) / total
    g = (100 * cadeia.count('G')) / total
    invalido = 100 - (a + c + t + g)
    print('''A cadeia de DNA eh {:.2f}
    A quantidade de adenina eh {:.2f}
    A quantidade de tinina eh {:.2f}
    A quantidade de citosina eh {:.2f}
    A quantidade de guanina eh {:.2f}
    A porcentagem de nucleotideos invalidos eh {:.2f}%'''.format(total, cadeia.count('A'), cadeia.count('T'), cadeia.count('C'), cadeia.count('G'), invalido))
    
    print('''A porcentagem de adenina equivale a {:.2f}%
    A porcentagem de tinina equivale a {:.2f}%
    A porcentagem de citosina equivale a {:.2f}%
    A porcentagem de guanina equivale a {:.2f}%'''.format(a, t, c, g,))
    
if __name__ == '__main__':
    main()
