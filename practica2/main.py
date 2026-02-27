from percepcion import Percepcion
from regla import Regla
from accion import Accion
from motor_inferencia import Motor
from agente import Agente

percepcion = Percepcion(12, True, -12, "diurna")
print(percepcion.esValida())



regla1 = Regla(
    nombre="Primera prueba",
    condicion= lambda p: (not p.presencia and p.intensidad >0),
    accion= lambda p: Accion("Apagar", 0, 0)
)
regla2 = Regla(
    nombre="Primera prueba",
    condicion= lambda p: (not p.presencia and p.intensidad >0),
    accion= lambda p: Accion("Apagar", 0, 0)
)
regla3 = Regla(
    nombre="Primera prueba",
    condicion= lambda p: (not p.presencia and p.intensidad >0),
    accion= lambda p: Accion("Apagar", 0, 0)
)

print("La prueba", regla1.evaluar(percepcion))


print("Esta es la 3era prueba:")
motor = Motor()
motor.add_regla(regla1)
print(motor.evaluar(percepcion))



print("Prueba con el agente")
agente = Agente()
agente.decidir(percepcion)
#TODO: Hacer que se muestre el mensaje de error