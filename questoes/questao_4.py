## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos 
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o 
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de 
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    valor = float(input('Me informe o valor da casa: '))
    salario = float(input('Me informe o seu salario: '))
    meses = int(input('Me informe a qunatidade de meses a pagar:'))
    mensalidade = ((valor * 30) /100) / meses
    if salario < mensalidade:
        print('o emprestimo foi negado')
    else:
        print('O emprestimo foi concebido')

if __name__ == '__main__':
    main()
