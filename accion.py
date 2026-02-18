class Action:
    tipo: str
    intensidad: int
    delay: int

    def __init__(self, intensidad: int = 0, delay: int = 0):
        self.intensidad = intensidad
        self.delay = delay        

    def execute(self):
        print(f"Intensidad: {self.intensidad} Retraso: {self.delay}")


