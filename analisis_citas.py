import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('citas_medicas.csv')

print("=== Análisis Descriptivo ===")
print(df.describe())

print("\n=== Especialidades más demandadas ===")
print(df['especialidad'].value_counts())

print("\n=== Porcentaje de estados ===")
print(df['estado'].value_counts(normalize=True)*100)

df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

x = np.array(df.groupby('mes').size().index).reshape(-1, 1)
y = np.array(df.groupby('mes').size().values)

modelo = LinearRegression()
modelo.fit(x, y)

prediccion = modelo.predict([[13]])

print(f"\n=== Predicción de citas para el próximo mes (mes 13) ===")
print(f"{prediccion[0]:.0f} citas")
