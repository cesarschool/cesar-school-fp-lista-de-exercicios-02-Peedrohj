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
    n1 = int(input('Me informe um número: '))
    n2 = int(input('Me informe outro número: '))
    n3 = int(input('Me informe outro número: '))
    n4 = int(input('Me informe outro número: '))
    n5 = int(input('Me informe outro número: '))
    
    print('O maior número é : {}'.format(max(n1, n2, n3, n4, n5)))  
    print('O menor número é : {}'.format(min(n1, n2, n3, n4, n5)))  

if __name__ == '__main__':
    main()
