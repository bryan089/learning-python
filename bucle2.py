#Funcion para simular los intentos de ingreso de clave en cajero automatico
#Intentos permitidos: 3
import os
os.system("clear")
def cajero():
    #Clave registrada en el banco
    my_clave_banco = '2024'

    cont_attemps = 1
    status = True
    while status:
        #Clave digitada en el ATM
        clave = input("Digita tu clave: ")
        if my_clave_banco == clave:
            print("Has ingresado a tu cuenta")
            print(f"Intento satisfactorio: {cont_attemps}")
            status = False #breack
        else:
            if cont_attemps < 3:
                print(f"Intento {cont_attemps}: Clave erronea, vuelve a intentarlo \n")
                cont_attemps += 1
            else:
                print(f"Intento {cont_attemps}: Clave Incorrecta")
                cont_attemps += 1

            if cont_attemps > 3:
                print("Se han agotado los intentos permitidos. \nTu cuenta se ha bloqueado")
                break
        
cajero()