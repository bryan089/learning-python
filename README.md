# learning-python
Repositorio de lenguaje de Python en el Diplomado en Inteligencia Computacional
# Proceso de Staging:

Primmer comando: Enviar paquete a Staging o a la cola
$git add . / $git add --all / git add FILE_NAME.ext / git add FOLDER_NAME

Segundo comando: Anexar mensaje - ¿Que contiene el paquete?
$git commit -m "AQUI VA EL MENSAJE" //-m significa mensaje

Tercer comando: Enviar o desplegar el paquete hacia su destino (RAMA)
$git push origin BRANCH_NAME / $git push

# Comando para hacer seguimiento del Staging:
$git status // verificar el estado 
$git reset FILE_NAME.ext // saca el archivo de la cola de Staging
$git restore --stage FILE_NAME.ext
$git log // ver la trasabilidad o log de cambios realizados