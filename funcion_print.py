# print tiene 4 formas de uso
"" "
1.- con comas
2.- con signo '+'
3.- Formato con la función ()
4.- Es una variante de formato ()
"" "

# 1.- Con comas, concatenar agregando
# un espacio y haciendo casting de tipo
edad =  10
nombre =  " Juan "
estatura =  1.67
imprimir (edad, nombre, estatura)

# 2.- con '+' hace lo mismo pero no
# realiza el casting automático
# no agrega espacios
print ( str (edad) +  str (estatura) + nombre)

# 3.- formato de función ()
print ( " Nombre: {} Edad: {} Estatura: {}  " .format (nombre, edad, estatura))

# 4.- con una variante de formato () simplificada
print ( f " Nombre: \" { nombre } \ " \ n Edad: \ t { edad } " ) 

# print y el argumento end
print ( " Sólo hay 10 tipos de personas, las que saben binario y las que no " , end = " --- " )
imprimir ( " otra línea " )
