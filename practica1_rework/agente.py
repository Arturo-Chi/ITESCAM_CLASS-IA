from practica2.motor_inferencia import Motor
from practica1_rework.accion import Accion
from practica1_rework.percepcion import Percepcion

class Agente:
    motor: Motor


    def decidir(p: Percepcion):
        return Accion