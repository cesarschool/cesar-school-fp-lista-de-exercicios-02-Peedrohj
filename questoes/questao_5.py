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
    print('Me informe o tamanho de três retas ')
    a = float(input('Me informe o tamanho do primeiro lado: '))
    b = float(input('Me informe o tamanho do segundo lado: '))
    c = float(input('Me informe o tamanho do terceiro lado: '))
    if abs(a - b) < c < a + b or abs(a - c) < b < a + c or abs(b - c) < a < b + c:
        tri = True
        if a == b == c:
            print('O triangulo eh equilatero')
        elif a == b != c or a == c != b or c == b != a:
            print('O tirangulo eh isosceles')
        else:
            print('O triangulo eh escaleno')
    else:
        print('Não pode formar um triângulo')
    
if __name__ == '__main__':
    main()
