P = int(input("Dame el primer valor:"))
Q = int(input("Dame el segundo valor:"))
EXP = P**3 + Q**4 - 2 * P**2
print(f"el calculo es igual a:{EXP}")
if EXP < 680:
    print(f"valores: {P,Q}")
print("fin del programa")
