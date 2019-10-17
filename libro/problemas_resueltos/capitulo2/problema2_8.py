COMPRA = float(input("Dame el precio de la compra:"))
if COMPRA < 500:
    PAGAR = COMPRA
    print(f"Se tiene que pagar: {PAGAR}")
else:
    if COMPRA <= 1000:
        PAGAR = COMPRA - COMPRA*0.05
        print(f"se tiene que pagar: {PAGAR}")
    else:
        if COMPRA <= 7000:
            PAGAR = COMPRA - COMPRA*0.11
            print(f"se tiene que pagar: {PAGAR}")
        else:
            if COMPRA <= 15000:
                PAGAR = COMPRA - COMPRA*0.18
                print(f"se tiene que pagar: {PAGAR}")
            else :
                COMPRA > 15000
                PAGAR = COMPRA - COMPRA*0.25
                print(f"se tiene que pagar: {PAGAR}")
print("Fin del programa")

