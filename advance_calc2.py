'''
Script description:
realice la operación aritmética que el usuario desee.
Puede escoger entre sumar, restar, multiplicar o dividir.
'''

import os

os.system("clear")

def calculator(x,y,z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return 'No es posible dividir entre cero (0)'
        else:
            return x / y
    elif z == '5':
        return x + y, x - y, x * y, x / y
    else:
        print("::: Fail, invalid option :::")
        return 'Fail, invalid option'


n1 = float(input("Ingrese primer valor: "))
n2 = float(input("Ingrese segundo valor: "))

print(":::  MENÚ CALCULADORA :::")
print("[1]. SUMAR")
print("[2]. RESTAR")
print("[3]. MULTIPLICAR")
print("[4]. DIVIDIR")
print("[5]. TODAS")

opc = input("Digite una opción del menú: ")

ans = calculator(n1,n2,opc)
print("Resultado: ", ans)