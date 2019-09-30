A = float(input("Dame el valor de a:"))
B = float(input("Dame el valor de b:"))
C = float(input("Dame el valor de c:"))
DIS = B**2-4*A*C
X1 = ((-B)+DIS**0.5)/2*A
X2 = ((-B)-DIS**0.5)/2*A
if DIS > 0:
    print(f"las raices son: x1:{X1} y x2:{X2}")
print("Fin del programa")
