from datetime import datetime

# Crea una fecha actual
fecha = datetime(1879, 3, 14, 8, 0, 0) 

# Accede al día de la semana (0 = lunes, 1 = martes, ..., 6 = domingo)
dia_semana = fecha.weekday()

# Lista de días de la semana
dias_semana_lista = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Imprime el día de la semana
print("La fecha es:", fecha)
print("El día de la semana es:", dias_semana_lista[dia_semana])
