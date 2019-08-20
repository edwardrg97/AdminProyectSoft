#Programa que calcula el promedio de calificaciones de alumnos de un grado escolar 

promedio, total, contar = 0.0, 0, 0    #Creación e inicialización de variables en 0
print ("En este programa podra calcular el promedio de un alumno, acontinuación le pediran las calificaciones, recuerde ingresarlas uno a uno conforme se las piden y no olvide que el numero -1 es para terminar") 
print ("Introduzca la calificacion del alumno (-1 para salir): ") #Solicita datos de entrada al usuario
grado = int(input())	
while grado != -1:    #Inicia un ciclo para recopilar las calificaciones, se repetirá hasta recibir un -1
    total = total + grado
    contar = contar + 1 #varible contador para mover while, tambien sera usada para calcular el promedio final
    print ("Introduzca la calificacion del alumno (-1 para salir): ") # texto repetitivo para pedir varias calificaciones
    grado = int(input())
promedio = total / contar #calculo final de promedio
print ("Promedio de calificaciones del grado escolar es: " + str(promedio)) #Imprime el resultado
