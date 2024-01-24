import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Semilla para la reproducibilidad
np.random.seed(0)

# Paso 1: Crear un conjunto de datos de ejemplo
# Supongamos que tenemos 100 registros de datos
Fertilizante = np.random.choice(range(1, 4), 100)  # Fertilizante 1, 2, 3
Cultivo = np.random.choice(range(1, 4), 100)       # Cultivo 1, 2, 3
Produccion = np.random.rand(100) * 10             # Producción en toneladas
Beneficio = Produccion * np.random.rand(100) * 100  # Beneficio en dólares

# Combinando en una matriz
X = np.column_stack((Fertilizante, Cultivo, Produccion, Beneficio))

# Paso 2: Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Paso 3: Aplicar PCA
pca = PCA(n_components=2)  # Reducir a 2 dimensiones
X_pca = pca.fit_transform(X_scaled)

# Visualización de los resultados
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('Primer Componente Principal')
plt.ylabel('Segundo Componente Principal')
plt.title('Análisis PCA de Datos de Agricultura')
plt.show()