class Accion:
    tipo: str
    delay: int
    intensidad: int


    def __init__(self, tipo, delay, intensidad):
        self.tipo = tipo #ENCENDER, AJUSTAR, APAGAR, MANTENER
        self.delay = delay
        self.intensidad = intensidad


    def ejecutar(self) -> None:
        if self.delay == 5:
            print(f"ACCION: {self.tipo} DELAY: {self.delay} INTENSIDAD: {self.intensidad} DELAY: {self.delay}")
        else:
            print(f"ACCION: {self.tipo} DELAY: {self.delay} INTENSIDAD: {self.intensidad}")
