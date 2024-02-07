import math
print("Programa de cálculo de Raíz cuadrada")
print()
numero=int(input("Introduce un número: "))

intentos=0

while numero<0:
    print("No se puede hayar la raíz cuadrada de un nímero negativo.")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;

    numero=int(input("Introduce un número: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es: " + str(solucion))
    print("El programa ha finalizado.")
