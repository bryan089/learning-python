#Tipos de datos en Python
#Python es un lenguaje dinámicamente tipado (cuando declaro una variable o una constante, 
#no es obligatorio determinar su tipo)
#Python es un lenguaje INTERPRETADO**

#1. Numéricos
##Enteros Z
num1 = 42
print("num1 es: ",num1, type(num1))
##Flotantes o decimales (R)
num2 = 50.5
print("num2 es: ", type(num2))
##Complejos --> complex
num3 = 2j
print("num3", type(num3))
print("/n")

#2. Cadena --> todo lo que este entre comillas simples o dobles idica cadena
## el signo + en este tipo de datos cumple con la funcion de concatenar los datos
my_name = "Brayan"
last_name = '''S
o
l
a
r
t
e'''
profile = '''Soy una persona enfocada en hacer
    las cosas lo mejor posible para mi beneficio 
    y el de los demás'''
adress = "calle 26 # 26 - 96 "
number_cel = '3238166219'
print("My name is: ", type(my_name))
print("My last neme is: ", type(last_name))
print("My address is: ", type(adress))
print("my number_cel is: ", type(number_cel))

a = 1
b = 1
suma1 = a + b 
print("suma1 es: ", suma1)

c = '1'
d = '1'
suma2 = c + d
print("suma2 es: ", suma2)

#suma3 = a + c #En python no es posible sumar un dato int con un string
#print(suma3)


#3. Lógicos --> son valores o expresiones booleanas
usuario_activo = True
pago_realizado = False
print("usuario_activo ", type(usuario_activo))
print("pago_realizado ", type(pago_realizado))

#4. Listas
frutas = ['Apple', 'Banana']
colors = ['Blue', 'yellow']
detodito = ["brayan", 34, 600000, "Las Cuadras", 1.80, 75]
print(frutas)
print("frutas es: ", type(frutas))
print(colors)
print("colors es: ", type(colors))
print(detodito)
print("detodito es: ", type(detodito[4]))

#5. Tuplas


#6. Diccionarios
#7. Conjuntos