def sumar(x,y):
    z = x + y
    return z

def restar (x,y):
    return x - y

def mi_print(texto):
    print(f"este es mi print:{texto}")

def multiplica(valor,veces):
    if veces == None:
        print("debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)

def comanda(mesa, comensal, entrada, medio, fuerte, postre="gelatina de limon"):
    print(f"Mesa:{mesa} Comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")

def comanda2(**comida):
    llaves= comida.keys()
    for elem in llaves:
        print(elem,"-->", comida[elem])

def imprime_argumentos(*argumentos):
    for index in range(len(argumentos)):
        print(argumentos[index])

    
a = 10
b = 5
c = sumar(a,b)
print(f"la suma de {a} y {b} es {c}")
c = restar(a,b)
print(f"la resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica("hola",3)
comanda(2,1,"Ensalada","sopa de rana", "filete pompi de sirena","flan")
comanda("Ensalada","sopa de rana", "filete pompi de sirena","flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte= "filete pompi de sirena", mesa=2, comensal=1)
imprime_argumentos('hola',True,3.1416,1000,{'id':'sc01', 'nombre':'juan'})
imprime_argumentos()
comanda2(entrada="Ensalada",medio="sopa de rana",fuerte= "filete pompi de sirena", mesa=2, comensal=1,postre="strude de manzanza",bebida='coca light')
