BAND = 'T'
SUMSER = 0
I = 2
while (I <= 1800):
    SUMSER += 1
    print (f"Incremento de: {I}")
    if BAND == 'T':
        BAND = 'F'
        I += 3
    else:
       BAND = 'T'
       I += 2
print(f"La suma de todos los terminos es: {SUMSER}")
print("Fin del programa")
