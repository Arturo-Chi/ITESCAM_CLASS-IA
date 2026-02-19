class Perception:
    luz_natural: int
    presencia: bool
    hora_tipo: str
    intensidad_actual: int

    min_sin_presencia: int

    def __init__(self, luzNatural, presencia, horaTipo, intensidadActual):
    
        if not isinstance(luzNatural, int):
            raise TypeError("El valor de luz natural no es numérico")

        if (luzNatural < 0):
            raise ValueError("El valor de luz natural no puede ser negativo")    
        
        if not isinstance(presencia, bool):
            raise TypeError("Presencia no es un valor aceptable")
        
        if not isinstance(horaTipo, str):
            raise TypeError("El tipo de hora no es un valor aceptable")
        
        if horaTipo not in ("diurna", "nocturna"):
            raise ValueError("El tipo de hora solo puede ser 'diurna' o 'nocturna' ")
        
        if not isinstance(intensidadActual, int):
            raise TypeError("La intensidad actual no es numérico")
        
        if (intensidadActual < 0 or intensidadActual > 100):
            raise ValueError("El rango de intensidad va de 0 a 100")

        
        self.luz_natural = luzNatural
        self.presencia = presencia
        self.hora_tipo = horaTipo
        self.intensidad_actual = intensidadActual

        



