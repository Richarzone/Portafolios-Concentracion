# Momento de Retroalimentación: Módulo 2 Uso de framework o biblioteca de aprendizaje máquina para la implementación de una solución. (Portafolio Implementación)
En este repositorio se entregaran lo siguientes documentos:
* `momento-retro2.ipybn`: Notebook de implementacion de modelos con uso de framework
* `momento-retro2.py`: Documento .py de que contiene el codigo solo de la implementacion de modelos con uso de framework
* `Estatura-peso_HyM.csv`: Data set ha analizar
* `reporte-momento-retro2.ipynb`: Notebook del reporte de analisis de rendimiento del mejor modelo
* `reporte-momento-retro2.pdf`: Documento pdf del reporte de analisis de rendimiento

## Librerias utilizadas
Uso general
* `pandas`
* `numpy`
* `matplotlib`

Modelacion
* `skelearn`

Metricas, evaluacion y utilidades
* `mlxtend`
* `seaborn`
* `sklearn`

## Desempeño

Nombre de modelo          | R^2          
-------------             | -------------  
Decision Tree Classifier  | 83.33%  
Random Forest Classifier  | 86.36% 
Logistic Regression       | 91.67%

## Predicciones
Valores aleatorios del dataset `Estatura-peso_HyM.csv`

Numero Prueba | Valores de Entrada | Valor Esperado | Valor Obtenido
------------- | -------------      | -------------  | -------------
1             | 1.61, 72.21        | 0              | 0
2             | 1.69, 74.5         | 1              | 0
3             | 1.68, 77.36        | 0              | 0
4             | 1.53, 44.87        | 1              | 1
5             | 1.55, 66.33        | 0              | 0
6             | 1.63, 63.98        | 1              | 1
7             | 1.63, 70.42        | 0              | 0
8             | 1.61, 52           | 1              | 1
9             | 1.71, 77.18        | 0              | 0
10            | 1.59, 50.05        | 1              | 1

Valores aleatorios externos (Basados en tabla de IMC)

Numero Prueba | Valores de Entrada | Valor Esperado | Valor Obtenido
------------- | -------------      | -------------  | -------------
1             | 1.68, 66.21        | 0              | 0
2             | 1.68, 61.83        | 1              | 1
3             | 1.78, 73.36        | 0              | 0
4             | 1.78, 64.0         | 1              | 1
5             | 1.65, 58.33        | 0              | 1
6             | 1.65, 52.12        | 1              | 1
7             | 1.73, 66.63        | 0              | 0
8             | 1.73, 59.42        | 1              | 1
9             | 1.65, 64.87        | 0              | 0
10            | 1.65, 59.52        | 1              | 1
