# Programa para calcular el Índice de Masa Corporal

#Mensaje de bienvenida
print("¡Bienvenido a la calculadora de IMC!") 

# Datos personales
nombre = input("Ingrese su nombre:") #string
apellido_paterno = input("ingrese su apellido paterno:") #string
apellido_materno = input("Ingrese su apellido materno:") #string
edad = int(input("Ingrese su edad:")) #int

# Datos físicos
peso = float(input("Ingrese su peso en kilogramos:")) #float 
estatura = float(input("Ingrese su estatura en metros:")) #float

# Cálculo del IMC
imc = round(peso / (estatura ** 2), 2) #redonde el resultado a 2 decimales

# Resultados
print("Hola, su IMC es:", imc)
