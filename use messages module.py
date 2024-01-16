from messages import messageFormatter

print(messageFormatter("Error: Este mensaje es de error", "error"))
print()
print(messageFormatter("Éxito: Ete mensaje es de éxito", "success"))
print()
print(messageFormatter("Advertencia: Este mensaje es una advertencia",
"warning"))
print()
print(messageFormatter("Información: Este mensaje es informativo", "info"))
print()
print("Este mensaje es normal") 