SERIE = 0
N = int(input("Dame el numero de terminos:"))
I = 1
for I in range (1,N,1):
	SERIE += I**I
	I += 1
print(f"La serie es:{SERIE}")
print("Fin del programa")
