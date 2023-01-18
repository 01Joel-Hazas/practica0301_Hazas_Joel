# Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de
# fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
# Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.

import datetime

# Recursivo
def fibRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibRec(n-1) + fibRec(n-2)

# Bucles

def fibBuc(n):
    a = 0
    b = 1

    for k in range(n):
        c = b + a
        a = b
        b = c

    return a

start_time = datetime.datetime.now()
#print(fibRec(40))
print(fibBuc(40))
end_time = datetime.datetime.now()
print(end_time - start_time)
