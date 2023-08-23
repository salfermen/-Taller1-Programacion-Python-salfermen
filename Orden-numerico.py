print("Bienvenido, ingrese el primer número:")
N1 = int(input())

print("Ingrese el segundo número:")
N2 = int(input())

print("Ingrese el tercer número:")
N3 = int(input())

print("Ingrese el cuarto número:")
N4 = int(input())

# Ordenar los números usando una lista
N = [N1, N2, N3, N4]
N.sort()

print("Números ordenados de menor a mayor:")
for num in N:
    print(num)
