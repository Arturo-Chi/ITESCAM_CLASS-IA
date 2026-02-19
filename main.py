from percepcion import Perception
from accion import Action
from agente import AgentIlumination

#miAccion = Action(intensidad=23, delay=4)
#miAccion.execute()

#percepcion = Perception(300, True, "nocturna", 30)
#
#agente1 = AgentIlumination()
#accion = agente1.chooseAction(percepcion)
#accion.execute()


def simulacion(nombre, datos):
    print(nombre)
    agente = AgentIlumination()

    for minuto, estado in enumerate(datos, start=1):
        lux, presencia, hora, intensidad = estado
        p = Perception(lux, presencia, hora, intensidad)
        accion = agente.chooseAction(p)

        print(f"""
{nombre}
======================================
minuto: {minuto}
lux: {lux}
presencia: {presencia}
hora: {hora}
intensidad actual: {intensidad}

accion: {accion.tipo}
nuevaIntensidad: {accion.intensidad}
delay: {accion.delay}
======================================
""")


primero = [
    (600, True, "diurna", 70),
    (600, True, "diurna", 70),
    (600, True, "diurna", 70),
]


segundo = [
    (30, True, "nocturna", 40),
    (30, True, "nocturna", 40),
]

tercero = [
    (300, False, "diurna", 60),
    (300, False, "diurna", 60),
    (300, False, "diurna", 60),
    (300, False, "diurna", 60),
    (300, False, "diurna", 60),
    (300, False, "diurna", 60)
]
cuarto = [
    (501, False, "diurna", 60),
    (501, False, "diurna", 60),
    (501, False, "diurna", 60),
    (501, False, "diurna", 60),
    (501, True, "diurna", 60),
    (501, False, "diurna", 60),
    (501, False, "diurna", 60),
    (501, False, "diurna", 60),
    (501, True, "diurna", 60),
    (501, True, "diurna", 60),
    (501, True, "diurna", 60),
]

#simulacion("Luz alta diurna", primero)
#simulacion("Muy Baja Nocturna", segundo)
simulacion("Presencia Intermitente", cuarto)



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