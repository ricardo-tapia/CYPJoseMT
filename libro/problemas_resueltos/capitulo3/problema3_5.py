N = int(input("Dame el numero de datos:"))
SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
I = 1
for I in range (1, N, 1):
	if I <= N:
		NUM = int(input("Dame un numero entero:"))
		if NUM > 0 :
			SUMPOS += NUM
			CUEPOS += 1
		else:
			SUMOTR += NUM
	I += 1
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS / CUEPOS)
print(f"Los numeros posivos son: {CUEPOS}")
print(f"El promedio de los numeros positivos es: {PROPOS}")
print(f"El promedio general es: {PROGEN}")
print("Fin del programa")
