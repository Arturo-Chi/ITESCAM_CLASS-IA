#class Percepcion:
# presencia: bool
# luminosidad_luz: float
# minutos_sin_presencia: int
#

class Agente:
 
 def decidir_accion(o: Percepcion):
  return Accion()


class Accion:
 
 tipo: str
 intensidad: int
 delay: int

 def __init__(self, tipo: str, intensidad: int = 0, delay: int = 0 ):
  self.tipo = tipo
  self.intensidad = intensidad
  self.delay = delay

 def ejecutar():
  print("Hola Mundo")
  
  
  
class Percepcion:
 luz_natural: int
 presencia: bool
 hora_tipo: str
 intensidad_actual: int

 def __init__(self, luz_natural: int, presencia: bool, hora_tipo: str, intensidad_actual: int):
  print("Hola mundo2")