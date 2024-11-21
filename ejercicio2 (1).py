nombre = input("Ingrese su nombre completo en formato Nombre Apellido1 Appelido2: ")
nombre_sep = nombre.split(" ")
nombre1 = nombre_sep[0]
apellido1 = nombre_sep[1]
apellido2 = nombre_sep[2]
nombrefinal = nombre_sep[0].title()
apellido1final = nombre_sep[1].title()
apellido2final = nombre_sep[2].title()

print (nombrefinal)
print (apellido1final)
print (apellido2final)