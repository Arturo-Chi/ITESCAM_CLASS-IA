class Percepcion:

    luzNatural: int
    presencia: bool
    intensidadActual: int
    horaTipo: str


    def __init__(self, luz, presencia, intensidad, horaTipo: str):
        self.luzNatural = luz
        self.presencia = presencia
        self.intensidadActual = intensidad
        self.horaTipo = horaTipo.lower()


    def esValida(self) -> any:
        #Se manejan los casos negativos
        
        if self.luzNatural < 0 or not isinstance(self.luzNatural, int): return False
        if (not isinstance(self.presencia, bool)) or (self.presencia not in (True, False)): return False
        if self.horaTipo.lower() not in ("dirna", "nocturna"): 
            return False 
            raise {"error": "El tipo de hora no es válido"}
        
        if self.intensidadActual < 0 or self.intensidadActual > 100: return False
        if not isinstance(self.intensidadActual, int): return False



        return True

