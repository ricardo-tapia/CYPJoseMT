SUMPAR = 0
SUMIMP = 0 
CUEPAR = 0
I = 1 
for I in range (1,271,1):
    NUM = int(input("Dame un numero entero:"))
    if NUM % 2 == 0:
        SUMPAR = SUMPAR + NUM
        CUEPAR = CUEPAR + 1
        I = 1 + 1
    else:
        SUMIMP = SUMIMP + NUM
        I = 1 + 1
PROPAR = SUMPAR / CUEPAR
print(f"promedio: {PROPAR}, Suma de impares:{SUMIMP}")
print("Fin del programa")
