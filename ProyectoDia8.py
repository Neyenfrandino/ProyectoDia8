# Turnero : utilizamos generadores, importamos modulos, y utilizamos decoradores tambien
# En este modulo crearemos los generadores o el decorador
# Decorador para imprimir mensajes antes y después de la generación del turno
def decorar_siguiente_turno(rubro):
  print('Su turno es:')
  if rubro == 'P':
    print(next(turno_perfumeria))
  elif rubro == 'F':
      print(next(turno_farmacia))
  elif rubro == 'C':
      print(next(turno_cosmetica))
  print('Aguarde y será atendido :)')


def generador_turno_perfumeria():
    for turno in range(1, 100):
        yield f'P-{turno}'


def generador_turno_farmacia():
    for turno in range(1, 100):
        yield f'F-{turno}'



def generador_turno_cosmetica():
    for turno in range(1, 100):
        yield f'C-{turno}'

turno_farmacia = generador_turno_farmacia()
turno_perfumeria = generador_turno_perfumeria()
turno_cosmetica = generador_turno_cosmetica()
