print('DIME DOS NÚMEROS Y TE DIGO LOS PARES QUE HAY ENTRE ELLOS EN REVERSA')

numero1 = int(input("NUMERO 1: "))
numero2 = int(input("NUMERO 2: "))

for pares in range(numero2, numero1-1, -1):
    if pares%2 == 0:
        print(pares)

