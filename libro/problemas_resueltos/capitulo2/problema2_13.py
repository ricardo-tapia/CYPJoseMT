MAT = int(input("Dame la matricula del alumno:"))
CARR = str(input("Dame la carrera del alumno:"))
SEM = int(input("Dame el numero de semestre del alumno:"))
PROM = float(input("Dame el promedio del alumno:"))
if CARR == "economia":
    if SEM >= 6:
        if PROM >= 8.8:
            print(f"Matricula:{MAT}, Carrera: {CARR}, Aceptado")
elif CARR == "computacion":
    if SEM > 6:
        if PROM >= 8.5:
            print(f"Matricula:{MAT}, Carrera: {CARR}, Aceptado")
elif CARR == "contabilidad":
    if SEM > 5:
        if PROM > 8.5:
            print(f"Matricula:{MAT}, Carrera: {CARR}, Aceptado")
elif CARR == "administracion":
    if SEM > 5:
        if PROM > 8.5:
            print(f"Matricula:{MAT}, Carrera: {CARR}, Aceptado")
print("Fin del programa")
