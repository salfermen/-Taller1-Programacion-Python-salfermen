print("Bienvenido al juego de tennis")
A = int(input("Ingresa los juegos ganados por el equipo A: "))
B = int(input("Ingresa los juegos ganados por el equipo B: "))
Gb = A + 2
Ga = B + 2

if A > 6 or B > 6:
    print("La opción ingresada es invalida")
elif A == 5 and B == 5:
    print("Empate 5 a 5")
    # empate 5 a 5
elif A == 6 and B == 6:
    print("Empate 6 a 6")
    # empate 6 a 6
elif B >= 6 and B >= Gb:
    print("Ganó el equipo b")
    # Gano el b
elif A >= 6 and A >= Ga:
    print("Ganó el Equipo A")
    # Gano el a
elif 0 <= A <= 6 and 0 <= B <= 6:
    print("El juego aún no termina")
    # El juego no ha terminado
elif A == 5:
    # Código para la variable A igual a 5
    pass
else:
    print("La opción ingresada es invalida")
