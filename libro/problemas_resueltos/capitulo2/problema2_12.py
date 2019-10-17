SUE = float(input("Dame el sueldo del trabajador:"))
CATE = int(input("Dame la categoria del trabajador:"))
HE = int(input("Dame las horas extra:"))
if  CATE  ==  1 :
    PHE  =  30
    HE  <  30
    NSUE  =  SUE + HE * PHE
elif  CATE  ==  2 :
    PHE  =  38
    HE  >  30
    NSUE  =  SUE + 30 * PHE
elif  CATE  ==  3 :
    PHE  =  50
    HE  >  30
    NSUE  =  SUE + 30 * PHE
elif  CATE  ==  4 :
    PHE  =  70
    HE  >  30
    NSUE  =  SUE + 30 * PHE
elif  CATE  >= 5 :
    PHE  =  0
    HE  <  30
    NSUE  =  SUE + HE * PHE
print(f"El sueldo que se tiene que pagar al trbajador es de: {NSUE} porque ha trabajado: {HE} horas extras")
print("Fin del programa")
