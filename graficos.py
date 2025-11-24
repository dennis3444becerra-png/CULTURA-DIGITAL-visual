import time
import numpy as np
import matplotlib.pyplot as plt

# codigo original 
def encontrar_primos_original(lower, upper):
    primos = []
    for num in range(lower, upper + 1):
        if num > 1:
            is_primo = True
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    is_primo = False
                    break
            if is_primo:
                primos.append(num)
    return primos
# codigo optimizado
def is_primo_optimi(n):
    if n < 2:
        return []
    return [num for num in range(2, n+1)
            if all(num % i != 0 for i in range(2, int(num**0.5)+1))]

def primo_numpy(n):
    if n < 2:
        return np.array([], dtype=int)
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for m in range(2, int(n**0.5)+1):
        if sieve[m]:
            sieve[m*m:n+1:m] = False
    return np.nonzero(sieve)[0]
# rango
LOWER = 1
UPPER = 100000

#  Medicion de tiempos 
print("\nMidiendo tiempos")

t0 = time.perf_counter()
encontrar_primos_original(LOWER, UPPER)
t_original = time.perf_counter() - t0

t0 = time.perf_counter()
is_primo_optimi(UPPER)
t_opt = time.perf_counter() - t0

print(f"Original : {t_original:.6f} s")
print(f"Optimizado : {t_opt:.6f} s")

# Distribución de tiempos 
plt.figure(figsize=(7,4))
plt.bar(["Original", "Optimizado", ], [t_original, t_opt])
plt.ylabel("Tiempo (segundos)")
plt.title("Comparativa de tiempos de ejecución")
plt.tight_layout()
plt.savefig("comparativa_tiempos.png")
plt.show()
# Distribución detallada: 
tiempos = np.array([t_original, t_opt])
labels = ["Original", "Optimizado"]

plt.figure(figsize=(7,4))
plt.barh(labels, tiempos)
plt.xlabel("Tiempo (segundos)")
plt.title("Distribucion de tiempos de ejecucion")
plt.tight_layout()
plt.savefig("distribucion_tiempos.png")
plt.show()
