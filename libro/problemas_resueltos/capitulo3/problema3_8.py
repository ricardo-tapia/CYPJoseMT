num = int(input("Dame un número: "))

if num > 0:
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        print (num)
else:
    print ("El número tiene que ser un entero positivo")
