'''
Script description:
cree una funcion genere el lanzamiento de 2 dados (1-6)
y que muestre por pantalla un mensaje GANADOR cuando genere dados iguales
de lo contrario, el mensaje dirá, SIGUE INTENTANDO
'''

#Importo biblioteca para generar numeros aleatorios enteros.
from random import randint

#Generar los valores o lanzar los dos dados
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

d = dices()
d1 = d[0]
d2 = d[1]
print("Dices : ", d)
print("Dice 1 : ", d1)
print("Dice 2: ", d2)


#print("Dice1: ", dice1)
#print("Dice2: ", dice2)