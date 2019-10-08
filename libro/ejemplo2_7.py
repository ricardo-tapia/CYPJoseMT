NUM = int(input("Ingrese un numero entero positivo:"))
V = int(input("Ingrese otro numero entero positivo:"))
VAL = 0
if NUM == 1:
    VAL = 100 * V
elif NUM == 2:
    VAL = 100 ** V
elif NUM == 3:
    VAL = 100 / V
else:
    VAl = 0
print(VAL)
print("Fi del programa")
