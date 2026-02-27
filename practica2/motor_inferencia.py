from typing import List
from regla import Regla
from accion import Accion
from percepcion import Percepcion

class Motor:
    
    reglas: List[Regla]

    def __init__(self):
        self.reglas = []

    def add_regla(self, r: Regla)-> None:
        self.reglas.append(r)

    def load_rules(self, rules: List[Regla])-> None:
        self.reglas = rules.copy()

    def evaluar(self, p:Percepcion):
        for regla in self.reglas:
            if regla.evaluar(p):
                regla.ejecutar(p) #Esta retornando una acción
        
        return Accion("MANTENER", 0, 0)

        
