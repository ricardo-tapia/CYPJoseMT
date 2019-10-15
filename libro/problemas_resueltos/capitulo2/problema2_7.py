A = int(input("Dame un numero:"))
B = int(input("Dame otro numero:"))
C = int(input("Dame otro numero:"))
if A < B:
    if B < C:
        print(f"Los números están en orden creciente.")
    else:
        print(f"Los números no están en orden creciente.")
else:
    print(f"Los números no están en orden creciente.")
print("fin del programa")
