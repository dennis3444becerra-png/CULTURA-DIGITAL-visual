# Dennis Alexander Becerra Gavidia 
# 23-11-2025
# Ciencia de datos e IA
# Tercero A 

# INTRODUCION 
En este proyecto se llevó a cabo un análisis y una optimización del código original encargado de calcular los números primos dentro de un rango de 1 a 100000. El programa inicial presentaba un tiempo de ejecución considerablemente alto debido a la estructura de su algoritmo. Por ello, se aplicaron mejoras orientadas a aumentar la eficiencia computacional y reducir el tiempo de procesamiento, garantizando resultados correctos y un desempeño significativamente superior.

# PROBLEMAS
No utiliza tecnicas eficientes 
Imprimir cada numero teniendo sobrecarga 
Dificultad en el analisis 

# OPTIMIZACION 
Se desarrolló una versión optimizada del programa, manteniendo el mismo método de verificación de números primos pero minimizando la sobrecarga en la ejecución. Además, se implementó un enfoque vectorizado utilizando la librería NumPy, lo que permitió mejorar significativamente el rendimiento, ya que NumPy está diseñado para realizar operaciones masivas de manera eficiente y con uso optimizado de memoria.

Gracias a estas mejoras, se obtuvieron varios beneficios importantes:

Eliminación del costo asociado a impresiones excesivas.

Reducción notable del tiempo de ejecución.

Aprovechamiento de estructuras vectorizadas altamente eficientes.

# RESULTADOS
una vez realizado el analisis y ejecucion pudimos ver que los tiempos con time.perf_counter() y el analissi con cProfile se pudo obtener los siguientes resultados:
En el codigo original tenemos el tiempo de ejecucion: 0.72298
En el codigo optimizado el tiempo de ejecucion: 0.2073
En el codigo de Numpy el tiempo de ejecucion: 0.000328

# CONCLUSION
Se pudo verificar que al momento de realizar una optimizacion se mejora la aceleracion y reducion de los tiempos de ejecucion y eliminacion de los calculos que no son necesarios con grandes cantidades, ademas con la implementacion de NumPy se pudo realizar el calculo de numeros primos con mas eficiencia y el analisis con cProfile nos permitio identificar las funciones mas costosas pudiendo obtener un codigo mas limpio, facil para ser analizado. 
