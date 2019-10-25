SERIE = 0
N = int(input("Dame un numero entero:"))
BAND = 'T'
I = 1
for I in range(1,N,1):
    if BAND == 'T':
        SERIE += 1/ I
        BAND ='F'
    else:
        SERIE -=1/I
        BAND = 'T'
    I += 1
print("La serie es:", SERIE)
