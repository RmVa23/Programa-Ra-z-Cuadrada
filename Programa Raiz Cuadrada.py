import math
print("Programa de cálculo de Raíz cuadrada")
print()
numero=int(input("Introduce un número: "))

intentos=0

while numero<0:
    print()
    print("No se puede hayar la raíz cuadrada de un numero negativo.")
    print()

    if intentos==2:
        print()
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;

    numero=int(input("Introduce un número: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print()
    print("La raíz cuadrada de " + str(numero) + " es: " + str(solucion))
    print()
    print("El programa ha finalizado.")
