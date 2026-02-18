"""
Docstring for ITESCAM_CLASS-IA.agente
Para realizar imports de otros archivos que podamos llegar a utilizar usamos:

--importar una clase específica:
from [nombre archivo] import [nombre clase]
from percepcion import Perception

--importar todo el archivo:
import [nombre Archivo]

Ninguno debe llevar la extensión del archivo

"""



from percepcion import Perception
from accion import Action

class AgentIlumination:
    
    def chooseAction(p: Perception):
        return Action()
    
    """Para devolver la instancia de una clase, no se usa "new" en Pytho
      Solo se usa el nombre de la clase con los parámetros: 

      return Action();      -> Así
    
    """
    
 



#class Accion:
# 
# tipo: str
# intensidad: int
# delay: int
#
# def __init__(self, tipo: str, intensidad: int = 0, delay: int = 0 ):
#  self.tipo = tipo
#  self.intensidad = intensidad
#  self.delay = delay
#
# def ejecutar():
#  print("Hola Mundo")
#  
#  
#  
#class Percepcion:
# luz_natural: int
# presencia: bool
# hora_tipo: str
# intensidad_actual: int
#
# def __init__(self, luz_natural: int, presencia: bool, hora_tipo: str, intensidad_actual: int):
#  print("Hola mundo2")
#