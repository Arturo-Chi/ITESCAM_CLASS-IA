class Perception:
    luz_natural: int
    presencia: bool
    hora_tipo: str
    intensidad_actual: int

    def __init__(self, luzNatural, presencia, horaTipo, intensidadActual):
        self.luz_natural = luzNatural
        self.presencia = presencia
        self.hora_tipo = horaTipo
        self.intensidad_actual = intensidadActual