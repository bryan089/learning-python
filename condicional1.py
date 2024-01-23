#LOS CONDIONALES
'''
Pueden ser simples o compuestos / anidados
Es necesario usar una tabla de operadores logicos:
> --> mayor que
< --> menor que
>= --> mayor o igual que
<= --> menor o igual que
<> --> diferente de
!= --> diferente de
= --> asignacion
== --> igual a (operador de comparacion)
se usan los valores o expresiones booleanas
'''

n1 = 10
if n1 > 0: #True o False
    print("El número ", n1," es positivo")
elif n1 < 0:
    print("El número ", n1 , " es negativo")
else:
    print("El número es cero [0]")