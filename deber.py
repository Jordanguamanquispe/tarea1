#Crear un algoritmo que tenga las siguientes consideraciones: 
#Solicitar nombre y apellidos 
#Solicitar el año de nacimiento
#Crear una función para calcular la edad 
#Crear una función para determinar si es mayor de edad 
#Crear una función para generar el correo electrónico con la 
#siguiente nomenclatura:
# primera letra del nombre + apellido paterno + primera letra del apellido materno. 
# Ejemplo: kpalaciosz@unemi.edu.ec
#Crear una función para generar una clave aleatoria que contenga
#15 caracteres y combinaciones entre números, letras mayúsculas y minúsculas. 
#Presentar un mensaje con todos los datos generados de la persona.
#Subir el archivo .py del algoritmo generado en Python. 

print("\t UNIVERSIDAD ESTATAL DE MILAGRO ")
print("\t           UNEMI           \n   ")
nombre = input("escriba su nombre: ")
apellid= input("ingrese su primer apellido : ")
apellidO =input("escriba su segundo apellido: ")
fechaDenacimiento = int (input("ingrese el año de nacimiento: "))
edad = 2024 - fechaDenacimiento
if edad >= 18 : 
    name = nombre[0] 
    ig = name
    apelliDo= apellidO[0] 
    apEllIdO = apelliDo 
    print(f"su correo institucional es {ig}{apellid}{apEllIdO}@unemi.edu.ec")
    longitud = 15  # Longitud de la contraseña
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"su contraseña es {contraseña}")
else : 
    print(f"""hola {nombre} {apellid } tu edad es {edad} 
y no cumples con los requisitos para seguir con el proceso """)

