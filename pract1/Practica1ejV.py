persona = ["Sofia","Quierco", 35947903, 20121991, 0]
print (persona)
print (persona[1])
clave_personal = persona[2] * persona[3]
print(clave_personal)
persona[4] = clave_personal
print (persona)
pgp_casera = (clave_personal,"34rf4D6&r/")
print(pgp_casera)
usuario = {}
usuario = {"Nombre":persona[0], "Apellido": persona[1], "DNI":persona[2], "Nacimiento":persona[3], "Clave_personal":persona[4], "pgp_casera": pgp_casera}
print(usuario["DNI"])
print(usuario["pgp_casera"])
