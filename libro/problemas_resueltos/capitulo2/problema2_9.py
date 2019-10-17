PREBAS = float(input("Dame el precio del producto:"))
if PREBAS > 500:
    IMP = 20 * 0.30 + (PREBAS - 40) * 0.50
    PRETOT = PREBAS + IMP
else: 
    if PREBAS > 40:
        IMP = 20 * 0.30 + (PREBAS - 40) * 0.40
        PRETOT = PREBAS + IMP
    else:
        if PREBAS > 20:
            IMP = (PREBAS - 20) * 0.30
            PRETOT = PREBAS + IMP
        else:
            IMP = 0
            PRETOT = PREBAS + IMP
print(f"El cliente debe pagar:{PRETOT} porque sus impuestos son: {IMP}")
print("Fin del programa")
