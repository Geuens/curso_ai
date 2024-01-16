# Ejemplo de códigos ANSI para diferentes colores
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_NARANJA = "\033[38;5;208m"  # Código ANSI para naranja
COLOR_MORADO = "\033[95m"         # Código ANSI para morado claro
RESET_COLOR = "\033[0m"  # Para resetear el color a su valor por defecto

print(COLOR_VERDE + "1. Añadir película"  + RESET_COLOR)