ARSU = 0
ARNO = 0
MERSU = 50000
ARCE = 0
I = 1
MES = 0
for I in range (1,13,1):
    print(f"mes(I):")
    RNO = int(input("Dame el promedio de lluvias del mes Zona norte:"))
    RCE = int(input("Dame el promedio de lluvias del mes Zona centro:"))
    RSU = int(input("Dame el promedio de lluvias del mes Zona sur:"))
              
    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU
              
    if RSU < MERSU:
        MERSU = RSU
        MES = I
PRORCE = ARCE / 12
print(f"Promedio region centro:¨{PRORCE}")
print(f"Mes con menor lluvia en region sur: {MES}")
print(f"Registro de mes con menor lluvia es: {MERSU}")
if ARNO > ARCE :
    if ARNO > ARSU:
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif ARCE > ARSU:
    print("La region con mayor lluvias es la regio centro")
else:
    print("La region con mayores lluvias es la region sur")
print("Fin del programa")
