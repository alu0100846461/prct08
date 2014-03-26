#! /usr/bin/python
#!encoding: UTF-8

#Declaramos una función destinada a calcular el valor aproximado del número pi.

def f (n):
    suma = 0.0
    for i in range (1, int(n+1)):
        xi = (i-0.5)/n
        fxi = 4/(1+xi**2)
        suma += fxi
    pi = suma/n 
    return pi

# Bloque de comprobaciones.

if (__name__ == "__main__"):
    #Importamos la librería sys para permitir el uso de sys.argv.
    import sys
    if (len(sys.argv) == 1):
        print "Se requiere la presencia de dos argumentos: número de intervalos e iteraciones."
        n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
        t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
    elif (len(sys.argv) == 2):
        print "Hemos detectado un único argumento en la línea de comandos."
        print "Se requiere la presencia de dos argumentos: número de intervalos e iteraciones."
        print "Por favor, siga las instrucciones que se proporcionan a continuación."
        n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
        t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
    else: 
        n = int(sys.argv[1])
        t = int(sys.argv[2])
    #Almacenamos el valor de referencia de pi con 35 decimales.
    PI = 3.1415926535897931159979634685441852
    print "Iteración\tValor obtenido\tValor real\tError cometido"
    for j in range (1, t+1):
        pi = f(j*n)
        print "%d\t\t%1.10g\t%1.10g\t%1.10f" %(j, pi, PI, abs(pi-PI)) 
