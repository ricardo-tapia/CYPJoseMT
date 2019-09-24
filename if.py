edad = int(input("dame tu edad:"))
INE = bool(int(input("tienes ine (0 NO / 1 SI):")))

if edad >= 18 and INE == True:
    print("es mayor de edad")
    print("puedes entrar al bar")
print("fin del programa")
