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
Una vez realizado el análisis y la ejecución de las diferentes versiones del programa, pudimos observar de manera clara cómo varían los tiempos de procesamiento al aplicar técnicas de optimización. Utilizando time.perf_counter() para una medición precisa y complementando el estudio con el análisis detallado que ofrece cProfile, se obtuvieron los siguientes resultados concretos:

En el código original, el tiempo de ejecución registrado fue de 0.72298, lo cual evidencia una demora considerable debido a la estructura inicial del algoritmo y la falta de optimizaciones.

En el código optimizado, el tiempo de ejecución se redujo significativamente a 0.2073, demostrando que las mejoras implementadas permitieron una disminución notable en el consumo de tiempo y recursos.

En la versión desarrollada con NumPy, el tiempo de ejecución fue de apenas 0.000328, mostrando un rendimiento excepcional gracias al procesamiento vectorizado que ofrece esta librería.

# CONCLUSION
Se pudo verificar que, al momento de realizar una optimización, se logra una mejora significativa en la aceleración del programa, así como una reducción notable en los tiempos de ejecución. Esto se debe principalmente a la eliminación de cálculos innecesarios y a la reorganización del código para hacerlo más eficiente cuando se trabaja con grandes cantidades de datos. Además, con la implementación de NumPy, fue posible realizar el cálculo de números primos con una eficiencia mucho mayor, aprovechando el procesamiento vectorizado que ofrece la librería.

El análisis realizado con cProfile permitió identificar con claridad cuáles eran las funciones más costosas en términos de rendimiento, lo que facilitó enfocar las mejoras en los puntos críticos del programa. Gracias a esto, se obtuvo un código más limpio, mejor estructurado y más fácil de analizar y mantener. En conjunto, todo el proceso demostró la importancia de optimizar y perfilar el código para obtener resultados rápidos, precisos y sostenibles en proyectos más grandes
