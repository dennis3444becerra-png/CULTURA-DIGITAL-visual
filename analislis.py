import cProfile
import pstats
import time


# CODIGO ORIGINAL
def encontrar_primos_original(n):
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# CODIGO OPTIMIZADO
def encontrar_primos_optimizado(n):
    return [
        num for num in range(2, n + 1)
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    ]
# PERFILADO
def perfilar(func, nombre_archivo, n=10000):
    profiler = cProfile.Profile()
    profiler.enable()

    func(n)  # ejecutar funcion

    profiler.disable()

    with open(nombre_archivo, "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats("tottime")
        stats.print_stats()

    # calcular tiempo real
    t0 = time.time()
    func(n)
    t1 = time.time()
    return t1 - t0

# MAIN

if __name__ == "__main__":
    print("Profiling codigo original...")
    t_original = perfilar(encontrar_primos_original, "profiling_original.txt")

    print("Profiling codigo optimizado...")
    t_opt = perfilar(encontrar_primos_optimizado, "profiling_optimizado.txt")

    print("\n--- RESULTADOS ---")
    print(f"Tiempo codigo original : {t_original:.6f} s")
    print(f"Tiempo codigo optimizado: {t_opt:.6f} s")
    print(f"Mejora: {(t_original - t_opt) / t_original * 100:.2f} %")
