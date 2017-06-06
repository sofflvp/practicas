anio = input("ingrese un anio: ")
if anio % 4 == 0:
    print ("el anio %s es bisiesto" % (anio))
elif anio % 100 == 0:
    if anio % 400 == 0:
        print ("el anio %s es bisiesto" % (anio))
    else:
        print ("el anio %s no es bisiesto" % (anio))

gato = raw_input("Ponga el nombre del gato Tom: ")
if gato == "Tom":
    print("El gato %s es Tom" % (gato))

if gato != "Tom":
    print("El gato %s no es Tom" % (gato))
