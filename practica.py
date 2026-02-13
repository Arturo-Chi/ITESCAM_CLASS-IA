from dataclasses import dataclass


@dataclass(frozen=True)
class Percepcion:
    presencia: bool
    luminosidad_lux: float
    minutos_sin_presencia: int


@dataclass(frozen=True)
class Accion:
    tipo: str  # "ENCENDER", "APAGAR", "MANTENER"

    def __post_init__(self):
        if self.tipo not in {"ENCENDER", "APAGAR", "MANTENER"}:
            raise ValueError(f"Acción inválida: {self.tipo}")


class AgenteIluminacion:
    """
    Agente basado en reglas SI–ENTONCES.
    - Crea Percepcion (con memoria mínima: minutos sin presencia)
    - Decide y devuelve una Accion
    - Actualiza el actuador interno (estado de la luz) al ejecutar la acción
    """

    def __init__(self, umbral_lux: float = 300.0, tiempo_apagado_min: int = 3):
        self.umbral_lux: float = float(umbral_lux)
        self.tiempo_apagado_min: int = int(tiempo_apagado_min)

        self._luz: str = "OFF"                 # estado actuador: "ON"/"OFF"
        self._min_sin_presencia: int = 0       # memoria mínima

    @property
    def luz(self) -> str:
        return self._luz

    @property
    def minutos_sin_presencia(self) -> int:
        return self._min_sin_presencia

    # -------- Validación --------
    def _validar_entradas(self, presencia, luminosidad_lux) -> float:
        if not isinstance(presencia, bool):
            raise ValueError("presencia debe ser bool (True/False).")

        try:
            lux = float(luminosidad_lux)
        except (TypeError, ValueError):
            raise ValueError("luminosidad_lux debe ser numérica (int/float).")

        if lux < 0 or lux > 100000:
            raise ValueError("luminosidad_lux fuera de rango razonable (0 a 100000).")

        return lux

    # -------- Construcción de Percepcion --------
    def percibir(self, presencia: bool, luminosidad_lux) -> Percepcion:
        lux = self._validar_entradas(presencia, luminosidad_lux)

        if presencia:
            self._min_sin_presencia = 0
        else:
            self._min_sin_presencia += 1

        return Percepcion(
            presencia=presencia,
            luminosidad_lux=lux,
            minutos_sin_presencia=self._min_sin_presencia
        )

    # -------- Decisión: devuelve Accion --------
    def decidir(self, p: Percepcion) -> Accion:
        # Prioridad 1: si hay presencia -> decidir por luminosidad
        if p.presencia:
            if p.luminosidad_lux < self.umbral_lux:
                return Accion("ENCENDER")
            else:
                return Accion("APAGAR")

        # Prioridad 2: si NO hay presencia -> decidir por contador
        if p.minutos_sin_presencia >= self.tiempo_apagado_min:
            return Accion("APAGAR")

        return Accion("MANTENER")

    # -------- Ejecuta la acción en el actuador interno --------
    def actuar(self, accion: Accion) -> None:
        if accion.tipo == "ENCENDER":
            self._luz = "ON"
        elif accion.tipo == "APAGAR":
            self._luz = "OFF"
        elif accion.tipo == "MANTENER":
            pass

    # Ciclo completo (útil para simulación):
    # percibe -> decide -> actúa, y DEVUELVE Accion (como pide tu práctica)
    def paso(self, presencia: bool, luminosidad_lux) -> Accion:
        p = self.percibir(presencia, luminosidad_lux)
        a = self.decidir(p)
        self.actuar(a)
        return a


# ---------- Simulación rápida de 3 escenarios ----------
def simular(nombre: str, ticks: list[tuple[bool, float]], agente: AgenteIluminacion) -> None:
    print(f"\n=== {nombre} ===")
    print("min | presencia | lux | sin_pres | accion     | luz")
    print("-" * 55)
    for minuto, (pres, lux) in enumerate(ticks, start=1):
        accion = agente.paso(pres, lux)
        print(f"{minuto:>3} | {str(pres):>8} | {lux:>3.0f} |"
              f" {agente.minutos_sin_presencia:>8} | {accion.tipo:<10} | {agente.luz}")


if __name__ == "__main__":
    agente = AgenteIluminacion(umbral_lux=300.0, tiempo_apagado_min=3)

    esc1 = [(True, 120), (True, 200), (True, 280)]
    simular("Escenario 1: presencia + poca luz (enciende)", esc1, agente)

    esc2 = [(True, 600), (True, 450), (True, 310)]
    simular("Escenario 2: presencia + luz suficiente (apaga)", esc2, agente)

    esc3 = [(False, 100), (False, 100), (False, 100), (False, 100)]
    simular("Escenario 3: sin presencia (apaga al minuto 3)", esc3, agente)
