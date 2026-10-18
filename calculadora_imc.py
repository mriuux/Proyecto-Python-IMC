# Programa para calcular el Índice de Masa Corporal

#Mensaje de bienvenida
print("¡Bienvenido a la calculadora de IMC!") 

# Datos personales
nombre = input("Ingrese su nombre: ").title() #string #.title: Deja todas las palabras con la primera letra en mayúscula y las demás en minúsculas. #.capitalize: Deja la primera letra en mayúscula, las demás en minúsculas.
apellido_paterno = input("Ingrese su apellido paterno: ").title() #string 
apellido_materno = input("Ingrese su apellido materno: ").title() #string 
edad = int(input("Ingrese su edad: ")) # int

# Datos físicos
peso = float(input("Ingrese su peso en kilogramos: ")) #float 
estatura = float(input("Ingrese su estatura en metros: ")) #float

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