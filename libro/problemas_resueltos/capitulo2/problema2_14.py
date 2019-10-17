TIPOENF = int(input("Dame la enfermedad del paciente:"))
EDAD = int(input("Dame la edad del paciente:"))
DIAS = int(input("Dame el numero de días que el paciente estuvo hospitalizado:"))
if TIPOENF == 1:
    COSTOT = DIAS*25
elif TIPOENF == 2:
    COSTOT = DIAS*16
elif TIPOENF == 3:
    COSTOT = DIAS*20
elif TIPOENF == 4:
    COSTOT = DIAS*32
if EDAD >= 14:
    if EDAD <= 22:
        COSTOT = COSTOT*1.10
print(f"Costo total:{COSTOT}")
print("Fin del programa")
