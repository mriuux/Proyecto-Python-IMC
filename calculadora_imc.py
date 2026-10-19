# Programa para calcular el Índice de Masa Corporal

#Mensaje de bienvenida
print("¡Bienvenido a la calculadora de IMC!") 

# Datos personales
nombre = input("Ingrese su nombre: ").strip().title() #string #.title: Deja todas las palabras con la primera letra en mayúscula y las demás en minúsculas. #.capitalize: Deja la primera letra en mayúscula, las demás en minúsculas.
while nombre == "":
    print("Error: el nombre no puede estar vacío.")
    nombre = input("Ingrese su nombre: ").strip().title() #.strip: Elimina los espacios en blanco al final y al inicio de la cadena.

apellido_paterno = input("Ingrese su apellido paterno: ").strip().title() #string
while apellido_paterno == "":
    print("Error: eñ apellido paterno no puede estar vacío.")
    apellido_paterno = input("Ingrese su apellido paterno: ").strip().title()

apellido_materno = input("Ingrese su apellido materno: ").strip().title() #string
while apellido_materno == "":
    print("Error: el apellido materno no puede estar vacío.")
    apellido_materno = input("Ingrese su apellido materno: ").strip().title()

#Validación de la edad
edad = input("Ingrese su edad: ").strip() #string
while not edad.isdigit() or int(edad) <=0:
    print("Error: ingrese una edad válida con números enteros positivos.")
    edad = input("Ingrese su edad: ").strip()
edad = int(edad) #int: convierte la cadena de texto a un npumero entero.

# Datos físicos
#Validación del peso
peso = input("Ingrese su peso en kilogramos: ").strip() #strig
while peso == "":
    print("Error: el peso no puede estar vacío.")
    peso = input("Ingrese su peso en kilogramos: ").strip()

try:
    peso = float(peso) #float: convierte la cadena de texto a un número decimal.
    while peso <= 0:
        print("Error: ingrese un peso válido mayor a 0.")
        peso = float(input("Ingrse su peso en lilogramos: "))
except ValueError:
    print("Error: debe ingresar un valor numérico para el peso.")
    peso = float(input("Ingrese su peso en kilogramos: "))

#Validación de la estatura
estatura = input("Ingrese su estatura en metros: ").strip() #string
while estatura == "":
    print("Error: la estatura no puede estar vacía.")
    estatura = input("Ingrese su estatura en metros: ").strip()

try:
    estatura = float(estatura) #float: convierte la cadena de texto a un número decimal.
    while estatura <= 0:
        print("Error: ingrese una estatura válida mayor a 0.")
        estatura = float(input("Ingrese su estatura en metros: "))
except ValueError:
    print("Error: debe ingresar un valor numérico para la estatura.")
    estatura = float(input("Ingrese su estatura en metros: "))

# Cálculo del IMC
imc = round(peso / (estatura ** 2), 2) #redonde el resultado a 2 decimales

# Resultados
print("\n========== REPORTE DE RESULTADOS ==========") #\n: salto de línea
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}") #f: variables directas en el texto con las llaves {}
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f} kg/m²") #:.2f: redondea el resultado a 2 decimales.
print("===========================================")