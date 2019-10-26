MAY = -100000
MEN = 100000
N = int(input("Dime cuanto enteros se ingresan:"))
I = 1
for I in range (1,N,1):
	NUM = int(input("Dame un numero entero:"))
	if NUM > MAY:
		MAY = NUM
	else:
		if NUM < MEN:
			MEN = NUM
I += 1
print(f"El numero mayor es: {MAY}")
print(f"El numero menos es:{MEN}")
print("Fin del programa")
