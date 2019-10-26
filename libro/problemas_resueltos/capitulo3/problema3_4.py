NOM = 0
SUE = 0
while SUE != -1:
	SUE = float(input("Dame el sueldo del trabajador(-1 para salir):$"))
	if SUE < 1000 and SUE > 0:
		NSUE = SUE * 1.15
		print(f"El nuevo sueldo es: ${NSUE}")
		NOM += NSUE
	elif SUE >= 1000:
		NSUE = SUE * 1.12
		print(f"El nuevo sueldo es: ${NSUE}")
		NOM += NSUE
print(f"El total de la nueva nomima es: ${NOM}")
print("Fin del programa")
