# Uso general
import pandas as pd
import warnings

# Sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

warnings.filterwarnings("ignore")

# Lectura de csv y creacion de dataframe
data = pd.read_csv("Estatura-peso_HyM.csv")

# Division de informacion por sexo
dataH = data.loc[:, ["H_estat", "H_peso"]]
dataH.columns = ["Estatura", "Peso"]
dataM = data.loc[:, ["M_estat", "M_peso"]]
dataM.columns = ["Estatura", "Peso"]

# Identificadores de sexo: 0 = Hombre, 1 = Mujer
dataH["Sexo"] = 0
dataM["Sexo"] = 1

# Union de ambos dataframes
df = pd.concat([dataH, dataM])

s = StandardScaler()

# Separacion de variable dependiente y variables independiantes
x = s.fit_transform(df.drop(columns="Sexo", axis=1))
y = df.Sexo.values

# Creacion de datos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Logistic Regression": LogisticRegression()
}

# Entrenamiento de modelos
print("Accuracy Scores y Matrices de Confuncion:")
for name, model in models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print(f"{name}: {accuracy_score(y_test, y_pred)*100:.2f}%")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

print()

print("Predicciones con datos del dataset")
# Lista de predicciones
predicciones = {"AyP": [[1.61, 72.21],
                        [1.69, 74.5],
                        [1.68, 77.36],
                        [1.53, 44.87],
                        [1.55, 66.33],
                        [1.63, 63.98],
                        [1.63, 70.42],
                        [1.61, 52],
                        [1.71, 77.18],
                        [1.59,50.05]],
                "Sexo":[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}

prediccionesDF = pd.DataFrame(predicciones)

result_pred = []

for caso in prediccionesDF["AyP"]:
    x = s.transform([caso])
    result_pred.append(models["Logistic Regression"].predict(x)[0])

for i in range(len(prediccionesDF)):
    print(f"Prediccion {i + 1} con datos de prediccion: {prediccionesDF['AyP'][i]}")
    print(f"-    Resultado Esperado: {prediccionesDF['Sexo'][i]}  Resultado Real: {result_pred[i]}")

print()
print(f"Logistic Regression: {accuracy_score(prediccionesDF['Sexo'], result_pred)*100:.2f}%")
print()

print("Predicciones con datos fuera del dataset (Basados en el IMC)")

predicciones = {"AyP": [[1.68, 66.21],
                        [1.68, 61.83],
                        [1.78, 73.36],
                        [1.78, 64.0],
                        [1.65, 58.33],
                        [1.65, 52.12],
                        [1.73, 66.63],
                        [1.73, 59.42],
                        [1.65, 65.87],
                        [1.65, 59.52]],
                "Sexo":[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}

prediccionesDF = pd.DataFrame(predicciones)

result_pred = []

for caso in prediccionesDF["AyP"]:
    x = s.transform([caso])
    result_pred.append(models["Logistic Regression"].predict(x)[0])

for i in range(len(prediccionesDF)):
    print(f"Prediccion {i + 1} con datos de prediccion: {prediccionesDF['AyP'][i]}")
    print(f"-    Resultado Esperado: {prediccionesDF['Sexo'][i]}  Resultado Real: {result_pred[i]}")

print()
print(f"Logistic Regression: {accuracy_score(prediccionesDF['Sexo'], result_pred)*100:.2f}%")