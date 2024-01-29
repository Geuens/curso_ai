from sklearn import LinearRegression, mean_squared_error, r2score, train_test_split
import pandas as pd


df = pd.read_csv('data/precios_pisos.csv') # Datos pisos
df_distritos = pd.read_csv('data/distritos.csv') # Nombres e ids de distrito

# X son las características (superficie_construida y distritos_id) e Y es lo que queremos predecir (precio)
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']

df['precio_m2'] = df['precio'] / df['superficie_construida']

# Eliminar los valores atípicos usando el percentil 99 y 1 para precio m2
df = df[df['precio_m2'] < df['precio_m2'].quantile(0.09)]
df = df[df['precio_m2'] > df['precio_m2'].quantile(0.01)]
# Con los datos limpios volvemos a reasignar x e y
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']

# Normalizar los datos
media_superficie = x['superficie_construida'].mean()
std_superficie = x['superficie_construida'].std()
superficie_normalizada = (df['superficie_construida'] - media_superficie) / std_superficie
# Combinar la superficie normalizada con 'distritos_id' no normalizado
caracteristicas = pd.DataFrame({
'superficie_construida': superficie_normalizada,
'distritos_id': df['distritos_id']
})
precios = (y - y.mean()) / y.std()

# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(x_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(x_test)
# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'R²: {r2}')

# Dividir los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(caracteristicas, precios, test_size=0.2, random_state=42)