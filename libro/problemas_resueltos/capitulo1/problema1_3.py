NOM = str(input("Escribe el nombre del dinosaurio:"))
PES = float(input("Escribe el peso del dinosaurio en kilos:"))
LON = float(input("Escribe la longitud del dinosaurio expresado en pies:"))
PESKIL = PES*1000
LONMET = LON*0.3047
print(f"El peso en toneladas del {NOM} es igual a: {PESKIL} dado que el peso es igual a {PES} kilos")
print(f"La longitud en metros del {NOM} es igual a: {LONMET} dado que la longitud es igual a {LON} pies")
