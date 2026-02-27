from motor_inferencia import Motor
from accion import Accion
from percepcion import Percepcion
from typing import List
from regla import Regla


@staticmethod
def daRules() -> List[Regla]:
    return [

    ]


class Agente:
    motor: Motor

    def __init__(self,):
        self.motor = Motor()
        self.motor.load_rules(daRules())


    def decidir(self, p: Percepcion):
        self.motor.evaluar(p).ejecutar()