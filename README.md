# Ejercicios de Scala

## Qué es este módulo

Esta carpeta concentra la línea Scala del repositorio Unsam-algoritmic. No está planteada como una colección aislada de ejercicios sintácticos: funciona como un recorrido de formación en pensamiento algorítmico, modelado funcional y procesamiento de datos con herramientas que también aparecen en contextos industriales.

El proyecto combina problemas clásicos de algoritmia con prácticas de ingeniería orientadas a datos: búsqueda binaria y lineal, parsing recursivo, simulación, lógica contable, procesamiento tabular, visualización y uso de Spark para cargas y transformaciones sobre datasets reales.



### Algoritmos y estructuras

- Búsqueda binaria y lineal.
- Parsing CSV con enfoque recursivo.
- Modelos de cola FIFO y control de flujo.
- Transformaciones sobre listas, strings y secuencias.

### Simulación y probabilidad

- Simulación de generala y eventos combinatorios.
- Modelos de rebote, propagación y series aleatorias.
- Experimentos reproducibles con salida analítica y gráfica.

### Data engineering y análisis

- Lectura y limpieza de datasets CSV.
- Procesamiento distribuido con Spark SQL.
- Exportación de resultados en parquet.
- Visualización con Breeze.

### Casos de negocio y cálculo aplicado

- Seguimiento de costos y precios.
- Cálculo hipotecario.
- Series financieras y tendencias.
- Preparación de datos para modelos de machine learning.

## Stack técnico

El subproyecto ubicado en `unsam/` está construido con:

- Scala 2.12.13
- sbt
- Apache Spark 3.3.0
- ScalaTest
- Breeze, Breeze Natives y Breeze Viz

Este stack es especialmente relevante para posicionamiento profesional porque Scala sigue teniendo presencia fuerte en plataformas de datos, motores de procesamiento distribuido y pipelines analíticos de alta performance.

## Estructura principal

- `unsam/src/main/scala/Operation`: ejercicios algorítmicos base.
- `unsam/src/main/scala/contable`: problemas de costos, camiones e hipotecas.
- `unsam/src/main/scala/simulacion`: experimentos probabilísticos.
- `unsam/src/main/scala/botanica`: procesamiento de datos con Spark sobre mareas y arbolado.
- `unsam/src/main/scala/mlflow`: primeras aproximaciones a análisis financiero y modelos.
- `unsam/src/test/scala`: validación automática con ScalaTest.

## Relación con el ecosistema Scala

Para posicionar este repositorio en una conversación más amplia, conviene conectarlo con instituciones y comunidades que empujan el lenguaje en investigación, formación avanzada e industria.

- Scala at EPFL: https://scala.epfl.ch/
- Scala Center, con sede en EPFL, Lausanne: https://scala.epfl.ch/scala-center.html
- Scala Team project records 2026: https://scala.epfl.ch/records/2026-STA-projects.html
- EPFL, institución de referencia en Suiza para ciencias de la computación e ingeniería: https://www.epfl.ch/en/
- ETH Zurich, otra referencia fuerte del ecosistema técnico suizo: https://ethz.ch/en.html
- Swiss Data Science Center, relevante para intersección entre datos, ciencia aplicada e ingeniería: https://www.datascience.ch/

Estas referencias no implican afiliación formal del repositorio, pero sí sirven para ubicarlo dentro de una conversación técnica seria: Scala como lenguaje de diseño de software, computación de alto nivel, sistemas de datos y formación algorítmica avanzada.

## Lectura estratégica del repositorio

Si el objetivo es presentar este trabajo a reclutadores, equipos técnicos o socios académicos, la narrativa más sólida es la siguiente:

1. El repositorio entrena fundamentos algorítmicos de forma explícita.
2. La capa Scala agrega tipado fuerte, modelado expresivo y testing automatizado.
3. El uso de Spark y Breeze conecta el aprendizaje con casos reales de procesamiento y análisis de datos.
4. La mezcla de ejercicios base y problemas aplicados muestra progresión, no solo resolución puntual.

## Cómo ejecutar

Desde la carpeta del proyecto Scala:

```bash
cd Ejercicios/ejercicios_scala/unsam
sbt test
sbt run
```

Para exploración local, también resulta útil:

```bash
sbt compile
```

## Valor para portfolio técnico

Este módulo puede presentarse como evidencia de capacidades en:

- resolución de problemas algorítmicos;
- programación funcional y tipada;
- testing automatizado;
- análisis y transformación de datos;
- trabajo con herramientas usadas en ecosistemas de datos sobre JVM.

En conjunto, los ejercicios de Scala ayudan a mover el repositorio desde una lógica puramente académica hacia una propuesta más cercana a software engineering orientado a algoritmos y datos.