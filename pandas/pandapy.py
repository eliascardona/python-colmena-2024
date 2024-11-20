import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/elias/Desktop/colmena/python/numpy/GeneticDataSource.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
edades = df['Age']
# datos_generales = df[['First name', 'Last name', 'Age']]
predis = df[df['Genetic Disease Predisposition'] == 'Yes']
tipos_de_sangre = df['Blood Type'].value_counts()

edad_prom = df['Age'].mean()


print(edad_prom)