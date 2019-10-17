CLAVE = int(input("Dame la clave de la zona geografica:"))
NUMIN = int(input("Dame la duracion de la llamada en minutos:"))
if  CLAVE == 12:
    COST = NUMIN * 2
elif CLAVE == 15:
    COST = NUMIN * 2.2
elif CLAVE == 18:
    COST = NUMIN * 4.5
elif CLAVE == 19:
    COST = NUMIN * 3.5
elif CLAVE == 23 or 25:
    COST = NUMIN * 6
if CLAVE == 29:
    COST = NUMIN * 5
print(f"Costo de la llamada: {COST}")
print("Fin del programa")
