MAT = int(input("Dame la matricula:"))
CAL1 = float(input("Dame la primer calificacion:"))
CAL2 = float(input("Dame la segunda calificacion:"))
CAL3 = float(input("Dame la tercera calificacion:"))
CAL4 = float(input("Dame la cuarta calificacion:"))
CAL5 = float(input("Dame la quinta calificacion:"))
PRO = ( CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO >= 6:
    print(f"{MAT} Aprobado, el promedio es de: {PRO}")
else:
    print(f"{MAT} NO aprobado, el promedio es de: {PRO}")
