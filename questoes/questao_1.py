## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    n1 = int(input('Me informe um numero: '))
    n2 = int(input('Me informe outro numero: '))
    n3 = int(input('Me informe outro numero: '))
    n4 = int(input('Me informe outro numero: '))
    n5 = int(input('Me informe outro numero: '))
    
    print('O maior numero e : {}'.format(max(n1, n2, n3, n4, n5)))  

if __name__ == '__main__':
    main()
