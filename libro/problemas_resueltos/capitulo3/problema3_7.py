MED = 0
CHI = 0
GRA = 0
N = int(input("Dame en numero de ventas:"))
I = 1
for I in range (1,N,1):
	V =  float(input("Dame el precio de la venta:"))
	if V <= 200:
		CHI += 1
	else:
		if V < 400:
			MED += 1
		else:
			GRA += 1
print(f"Las ventas menores a 200 son: {CHI}")
print(f"Las ventas mayores a 200 son: {MED}")
print(f"Las ventas mayored a 400 son: {GRA}")
print("Fin del programa")
