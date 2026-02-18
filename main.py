from percepcion import Perception
from accion import Action
from agente import AgentIlumination

miAccion = Action(intensidad=23, delay=4)
miAccion.execute()




"""
Para usar funciones hay 3 formas:

self --- Método de instancia
Trabaja con atributos del objeto
Modifica el estado del objeto
Necesita recordar información entre llamadas

Si el método necesita acceder a un atributo entonces lleva self


@staticmethod
Se usa cuando el método:
No usa atributos del objeto
No modifica nada interno
Es solo una función auxiliar

Se llaman de la forma: [Clase].[nombreMetodo]()
no necesitan de una instancia de la clase


@classmethod --- Este usa la clase, no el objeto
Se usa cuando se quiere trabajar con la clase misma.
Recibe cls en lugar de self
Ejemplo típico son los método fábrica


RECORDAR SIEMPRE:::
Si el método depende del estado interno del objeto → usa self.
Si no depende de nada interno → @staticmethod.
Si crea objetos de la clase → @classmethod.

"""