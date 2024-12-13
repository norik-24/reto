#Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, 
# caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve
#  una contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.
# Instrucciones:
#
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
# Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y 
# símbolos.
# Utilizará una función para generar la contraseña según las preferencias del usuario.
# Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
# Si el usuario decide salir, se despedirá y el programa se cerrará.

print("bienvenido al generador de contraseñas seguras,a continuacion debera insertar la longitud de su contraseña, y que tipo de caracteres desea usar")

minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
mayusculas = ["A""B""C""D""E""F""G""H""I""J""K""L""M""N""Ñ""O""P""Q""R""S""T""U""V""W""X""Y""Z"]
simbolos = ["<"">""+""`""*""+""]""¡""'""!""·""$""%""&""/""("")"]
alfanumericos = ["1""2""3""4""5""6""7""8""9""0"]
contraseña = []
def generador():
    print("a continuacion, ingrese el numero de resputas.")

    minus =  int(input("desea incluir minusculas) 1)si 2)no: "))
    if minus == 1: minus = True
    elif minus == 2 : minus = False
    
    mayus  =  int(input("desea incluir mayusculas) 1)si 2)no: "))
    if mayus == 1: mayus = True
    elif mayus == 2 : mayus = False

    alfa  =  ayus  =  int(input("desea incluir alfanumericos) 1)si 2)no: "))
    if mayus == 1: mayus = True
    elif mayus == 2 : mayus = False

    simb = int(input("desea incluir simbolos) 1)si 2)no: "))
    if simb == 1: simb = True
    elif simb == 2 : simb = False

    long = int(input("ingrese en numeros el tamaño de caracteres que quiere que posea su contraseña"))
    
    total_char = 0
    if minus == True: total_char = total_char+1

    if mayus == True: total_char = total_char+1

    if simb == True: total_char = total_char+1

    if alfa == True: total_char = total_char+1

    saltos = int(input("ingrese un numero aleatorio"))
    
    if minus == True :
        while len(contraseña) < long/total_char:
            for i in minusculas:
                contraseña.append(i)
    elif mayus == True :
                while len(contraseña) < long/total_char:
                     for i in contraseña():
                        mayusculas += i + saltos
                        contraseña.append(i)
    elif alfa == True :
        while len(contraseña) < long/total_char:
            for i in contraseña():
                alfanumericos += i + saltos
                contraseña.append(i)
    elif simb == True :
        while len(contraseña) < long/total_char:
            for i in contraseña():
                simbolos += i + saltos
                contraseña.append(i)
    return contraseña
print(generador())
print(contraseña)
