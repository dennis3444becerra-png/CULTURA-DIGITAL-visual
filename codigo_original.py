# Dennis Alexander Becerra Gavidia 
# 23-11-2025
# Ciencia de datos e IA
# Tercero A 

# Buscar los números primos en un rango de 1 a 100,000

import time

# el rango de busqueda 
lower = 1 
upper = 100000

inicio = time.time() # para ver el inicio del  cronometro

print("Los numeros primos", lower, "and", upper, "son")
for num in range(lower, upper + 1): # ciclo que ve todos los numero
    if num > 1:
        is_primo = True
        for i in range (2, int(num**0.5)+1):
            if num % i == 0:
                is_primo = False
                break
        if is_primo:
            print(num)

fin = time.time() # para el final del cronometro 
print("Tiempo de ejecucion:", fin - inicio, "segundos")
