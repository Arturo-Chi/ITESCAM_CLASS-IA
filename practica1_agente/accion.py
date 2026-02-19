class Action:
    tipo: str
    intensidad: int
    delay: int

    def __init__(self, tipo: str,  intensidad: int = 0, delay: int = 0):
        self.intensidad = intensidad
        self.delay = delay
        self.tipo = tipo

    def execute(self):
        print(f"""=============== 
Acción: {self.tipo} |
Ajustando Intensidad al: {self.intensidad}% |
Retraso: {self.delay} minutos
===============""")

"""
apagar (intensidad en 0%)
ajustar a x%
encender al 100%
apagar tras 5 minutos.

"""
