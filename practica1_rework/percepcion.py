class Percepcion:

    luzNatural: int
    presencia: bool
    intensidadActual: int
    horaTipo: str


    def __init__(self, luz, presencia, intensidad, horaTipo):
        self.luzNatural = luz
        self.presencia = presencia
        self.intensidad = intensidad
        self.horaTipo = horaTipo


    def esValida() -> bool:
        return True

