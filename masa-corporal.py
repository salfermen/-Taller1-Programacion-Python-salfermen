print("Ingrese la estatura en metros: ")
M = float(input())

print("Ingrese su peso en kilogramos: ")
W = float(input())

print("Ingrese su edad: ")
E = int(input())

MC = W / (M * M)

if MC < 18.5:
    risk = "Estimado USUARIO usted tiene bajo peso conforme a los datos ingresados"
elif MC < 25:
    risk = "Estimado USUARIO usted tiene un peso normal conforme a los datos ingresados"
elif MC < 30:
    risk = "Estimado USUARIO usted tiene sobrepeso conforme a los datos ingresados"
else:
    risk = "Estimado USUARIO usted tiene obesidad conforme a los datos ingresados"

print("Su índice de masa corporal (IMC) es:", MC)
print("Su condición de riesgo es:", risk)
