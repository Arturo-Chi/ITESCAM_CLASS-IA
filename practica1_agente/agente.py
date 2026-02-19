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
    min_sinPresencia: int

    def __init__(self):
        self.min_sinPresencia = 0

    def chooseAction(self, p: Perception):
        if not p.presencia:
            self.min_sinPresencia+=1

            if self.min_sinPresencia < 5:
                return Action("Mantener", p.intensidad_actual, 5)

            return Action("Apagar", 0, 0)
        else:
            self.min_sinPresencia = 0

            if p.luz_natural > 500 and p.hora_tipo=="diurna":
                return Action("Apagar", 0, 0)  
            
            if p.luz_natural > 200 and p.luz_natural <= 500:
                if p.hora_tipo == "diurna" and p.intensidad_actual < 30:
                    return Action("Ajustar", 30, 0)  
                elif p.hora_tipo =="nocturna" and p.intensidad_actual < 50:
                    return Action("Ajustar", 50, 0)  

            if p.luz_natural > 50 and p.luz_natural <= 200:
                if p.hora_tipo == "diurna" and p.intensidad_actual < 60:
                    return Action("Ajustar", 60, 0)  
                
                elif p.hora_tipo =="nocturna" and p.intensidad_actual < 80:
                    return Action("Ajustar", 80, 0)  

            if p.luz_natural < 50 and p.intensidad_actual < 100:
                return Action("Encender", 100, 0) 

            return Action("MANTENER", p.intensidad_actual, 0) 
        

    



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