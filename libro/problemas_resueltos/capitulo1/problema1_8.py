X1 = float(input("dame el la coordenada 1 del eje x:"))
Y1 = float(input("dame el la coordenada 1 del eje y:"))
X2 = float(input("dame el la coordenada 2 del eje x:"))
Y2 = float(input("dame el la coordenada 2 del eje y:"))
P1 = (X1,Y1)
P2 = (X2,Y2)
DIS = ((X1 -X2) ** 2 + (Y1 - Y2) ** 2) ** 0.5
print(f"la distancia entre {P1} y {P2} es igual a : {DIS}")
