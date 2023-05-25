import random
import sys

def iniciar():
    global partidas, ganadas, perdidas, empatadas
    partidas = 0
    ganadas = 0
    perdidas = 0
    empatadas = 0

def menu():
    print("--- INDICA EL NUMERO DE LA OPCION SELECCIONADA ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("0. SALIR")

    opcion = input('--> ')
    if opcion not in ['1','2','3','0']:
        print('Selecciona una opcion valida\n')
        opcion_usuario = None
    else:
        if opcion == '1':
            opcion_usuario = 'Piedra'
        if opcion == '2':
            opcion_usuario = 'Papel'
        if opcion == '3':
            opcion_usuario = 'Tijera'
        if opcion == '4':
            print('HASTA PRONTO !!')
            sys.exit()
    return opcion_usuario

def elige_maquina():
    lista_opciones = ['Piedra', 'Papel', 'Tijera']
    opcion_maquina = random.choice(lista_opciones)
    return opcion_maquina

def comprobar(opcion_usuario, opcion_maquina):
    global partidas, ganadas, perdidas, empatadas
    partidas += 1
    print('\n')
    if(opcion_usuario == opcion_maquina):
        print('-- Hemos empatado --')
        empatadas += 1
    elif(opcion_usuario == 'Piedra' and opcion_maquina == 'Tijera'):
        print('-- Has ganado --')
        ganadas += 1
    elif(opcion_usuario == 'Papel' and opcion_maquina == 'Piedra'):
        print('-- Has ganado --')
        ganadas += 1
    elif(opcion_usuario == 'Tijera' and opcion_maquina == 'Papel'):
        print('-- Has ganado --')
        ganadas += 1
    else:
        print('-- Has perdido --')
        perdidas += 1

    print('\n')
    print('*'*20)
    print(f'Mi opcion fue {opcion_maquina}')
    print(f'Tu opcion fue {opcion_usuario}')
    print(f'Llevamos {partidas} partidas')
    print(f'Tienes {ganadas} ganadas')
    print(f'Tienes {perdidas} perdidas')
    print(f'Tienes {empatadas} empatadas')
    print('*'*20)
    print('\n')

def main():
    iniciar()
    opcion_usuario = menu()
    while True:
        if opcion_usuario != None:
            opcion_maquina = elige_maquina()
            comprobar(opcion_usuario,opcion_maquina)
        opcion_usuario = menu()

if __name__ == '__main__':
    main()