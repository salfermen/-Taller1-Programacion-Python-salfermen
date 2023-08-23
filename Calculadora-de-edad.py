from datetime import date

# Solicitar la fecha de nacimiento al usuario
print("Ingrese su año de nacimiento: ")
birthyear = int(input())
print("Ingrese el mes de nacimiento (1-12): ")
birthmonth = int(input())
print("Ingrese el día de nacimiento: ")
birthday = int(input())

# Crear el objeto date para la fecha de nacimiento
birth_date = date(birthyear, birthmonth, birthday)

# Obtener la fecha actual
current_date = date.today()

# Calcular la edad
edad = current_date.year - birth_date.year

# Verificar si el cumpleaños ya pasó este año
if (birthmonth > current_date.month) or (birthmonth == current_date.month and birthday > current_date.day):
    edad -= 1

# Mostrar la edad
print("Su edad es:", edad, "años")
