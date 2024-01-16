import copy

empleados = [
["Pedro", ["Python", "SQL"]],
["Manolo", ["Java", "C++", "JavaScript"]],
["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

empleados_copia = empleados.copy()
empleados_copia_profunda = copy.deepcopy(empleados)

empleados[0][1].append("Machine learning")

print("print 1")
print(empleados)
print(empleados_copia)
print(empleados_copia_profunda)
print("n")

empleados_copia[0][1].append("Machine learning copy")
empleados_copia_profunda[0][1].append("Machine learning deep copy")

print("print 2")
print(empleados)
print(empleados_copia)
print(empleados_copia_profunda)