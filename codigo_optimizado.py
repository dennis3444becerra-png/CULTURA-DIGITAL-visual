# Dennis Alexander Becerra Gavidia 
# 23-11-2025
# Ciencia de datos e IA
# Tercero A 

import time
import numpy as np
# optimisacion
def is_primo_optimi(n):
    if n < 2:
        return[]
    primos = [num for num in range(2, n + 1)
              if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return primos
# NumPy
def primo_numpy(n):
    if n < 2:
        return np.array([], dtype=int)
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    raiz_max = int(n**0.5)
    for m in range(2, raiz_max + 1):
        if sieve[m]:
            sieve[m*m:n+1:m] = False
    return np.nonzero(sieve)[0]
# el rango de busqueda 
lower = 1 
upper = 100000
imprimir = False
# puro optimisacion 
print(f"\n--- METODO OPTIMIZADO ---")
inicio = time.perf_counter()
primos_p = is_primo_optimi(upper)
fin = time.perf_counter()
primos_p_range = [p for p in primos_p if p >= lower ]

if imprimir:
    print("primos optimizados", primos_p_range)
print("la cantidad de primos", len(primos_p_range))
print("tiempo de ejecucion", fin - inicio)

# puro numpy 
print(f"\n--- METODO NUMPY ---")
inicio = time.perf_counter()
primos_np = primo_numpy(upper)
fin = time.perf_counter()
primos_np_range = primos_np[ primos_np >= lower ]

if imprimir:
    print("primos NumPy:", primos_np_range.tolist())
print("la cantidad de primos", primos_np_range.size)
print("tiempo de ejecucion", fin - inicio)
