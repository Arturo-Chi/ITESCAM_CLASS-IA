class Accion:
    tipo: str
    delay: int
    intensidad: int


    def __init__(self, tipo, delay, intensidad):
        self.tipo = tipo
        self.delay = delay
        self.intensidad = intensidad


    def ejecutar() -> None:
        print()
