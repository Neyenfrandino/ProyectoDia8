# Aqui vamos a crear las funciones que administran el funcionamiento del programa, las instrucciones para elegir una
# area y para decidir si seguira tomando mas turnos o si va a finalizar el programa
# Aqui vamos a importar al otro modulo

import ProyectoDia8


while True:
    letra_usuario = input('''Escriba P para sacar un turno en perfumeria
                Escriba F para sacar un turno en la farmacia
                Escriba C para sacar un turno en cosmética: ''').upper()

    if letra_usuario == 'S':
        print('Muchas gracias por visitar FarmaVida :)')
        break

    ProyectoDia8.decorar_siguiente_turno(letra_usuario)

