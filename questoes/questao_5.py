## QUESTÃO 5 ##
# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
# Equilátero, Isósceles ou Escaleno.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    lado1 = float(input('Me informe o primeiro lado: '))
    lado2 = float(input('Me informe o segundo lado: '))
    lado3 = float(input('Me informe o terceiro lado: '))
    
    if lado1 == lado2 == lado3:
        print('O triangulo eh equilatero')
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
        print('O tirangulo eh isosceles')
    else:
        print('O triangulo eh escaleno')
    
if __name__ == '__main__':
    main()
