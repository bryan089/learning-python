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
        if y == 0:
            return x + y, x - y, x * y, 'No es posible dividir entre cero (0)'
        else:
            return x + y, x - y, x * y, x / y
    else:
        return 'Fail, invalid option'


n1 = float(input("Ingrese primer valor: "))
n2 = float(input("Ingrese segundo valor: "))

print(":::  MENÚ CALCULADORA :::\n")
print("[1]. SUMAR")
print("[2]. RESTAR")
print("[3]. MULTIPLICAR")
print("[4]. DIVIDIR")
print("[5]. TODAS")
opc = input("Digite una opción del menú: ")

print("Formato de salida de resultados 1 \n")
if opc == '1' or opc == '2' or opc == '3' or opc == '4':
    ans = calculator(n1, n2, opc)
    print("Resultado: ", ans)

elif opc == '5':
    ans = calculator(n1, n2, opc)
    print("Suma: ", ans[0], '\n')
    print("Resta: ", ans[1], '\n')
    print("Multiplicacion: ", ans[2], '\n')
    print("Division: ", ans[3], '\n')

print("Formato de salida de resultados calculator 2 \n")
#ans = calculator(n1,n2,opc, '\n')
print("Resultado: ", calculator(n1, n2, opc))

