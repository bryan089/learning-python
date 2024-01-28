'''
Bucle: loop, repetir una accion N veces, interacciones (Cantidad de ejecuciones).
Contadores (cuenta o incrementa)
Acumulador (Acumulacion de valores. peje. Sumar valores)
contar es diferente de sumar valores
'''
import os

os.system("clear")
#Funcion bucle para imprimir los numeros del 1 al 10 en pantalla
def list_numbers():
    #Bucle que imprime lista de números por pantalla
    i = 1
    print("::: Lista de numeros impresos del 1 al 100 ::: \n")
    while i <= 100:
        print(i)
        i = i + 1
    print('\n')
    print("i : ", i, '\n')

def list_numbers2():
    #Bucle que imprime lista de números por pantalla
    i = 1
    status = True
    print("::: Lista de numeros impresos del 1 al 10 ::: \n")
    while status:#while status == True
        if i == 11:
            break
        print(i)
        i = i + 1
    print('\n')
    print("i : ", i, '\n')

def list_numbers3():
    #Bucle que imprime lista de números por pantalla
    i = 1
    status = True
    print("::: Lista de numeros impresos del 1 al 10 ::: \n")
    while status:#while status == True
        print(i)
        i = i + 1
        if i > 10:
            status = False
    print('\n')
    print("i : ", i, '\n') 

def list_numbers4():
    #Bucle que imprime lista de números por pantalla
    i = 1
    status = False
    print("::: Lista de numeros impresos del 1 al 10 ::: \n")
    while not status:#while status != False
        print(i)
        i = i + 1
        if i > 10:
            status = True
    print('\n')
    print("i : ", i)  

list_numbers()
list_numbers2()
list_numbers3()
list_numbers4()
