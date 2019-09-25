L1 = float(input("Dame la longitud del lado 1 del triangulo:"))
L2 = float(input("Dame la longitud del lado 2 del triangulo:"))
L3 = float(input("Dame la longitud del lado 3 del triangulo:"))
S = (L1 + L2 + L3) / 2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5
print(f"el area del trigungulo es: {AREA}")

