print('DIME DOS NÚMEROS Y TE DIGO LOS IMPARES QUE HAY ENTRE ELLOS')

numero1 = int(input("NUMERO 1: "))
numero2 = int(input("NUMERO 2: "))

for impares in range(numero1, numero2+1):
    if impares%2 != 0:
        print(impares)