#Programa que calcula el promedio de calificaciones de alumnos de un grado escolar 

promedio, total, contar = 0.0, 0, 0    #Creación e inicialización de variables en 0

print ("Introduzca la calificacion del alumno (-1 para salir): ") #Solicita datos de entrada al usuario
grado = int(input())	
while grado != -1:    #Inicia un ciclo para recopilar las calificaciones, se repetirá hasta recibir un -1
    total = total + grado
    contar = contar + 1
    print ("Introduzca la calificacion del alumno (-1 para salir): ")
    grado = int(input())
promedio = total / contar
print ("Promedio de calificaciones del grado escolar es: " + str(promedio)) #Imprime el resultado
