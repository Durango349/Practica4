# ==========================================
# SERVICIOS ESPECIALIZADOS (Polimorfismo)
# ==========================================
class ReservaSala(Servicio):
    def __init__(self, identificador: str, descripcion: str, costo_base: float, capacidad: int):
        super().__init__(identificador, descripcion, costo_base)
        self.capacidad = capacidad

    def validar_parametros(self) -> bool:
        if self.capacidad <= 0:
            raise ErrorServicioInvalido("Room capacity must be greater than zero.")
        return True

    def calcular_costo(self, descuento: float = 0.0, impuesto: float = 1.19) -> float:
        self.validar_parametros()
        costo_con_descuento = self.costo_base * (1 - descuento)
        return round(costo_con_descuento * impuesto, 2)

    def obtener_detalle(self) -> str:
        return f"Room Reservation: {self.descripcion} (Capacity: {self.capacidad} people)"


class AlquilerEquipo(Servicio):
    def __init__(self, identificador: str, descripcion: str, costo_base: float, dias: int):
        super().__init__(identificador, descripcion, costo_base)
        self.dias = dias

    def validar_parametros(self) -> bool:
        if self.dias <= 0:
            raise ErrorServicioInvalido("Rental days must be greater than zero.")
        return True

    def calcular_costo(self, seguro: float = 0.0) -> float:
        self.validar_parametros()
        return round((self.costo_base * self.dias) + seguro, 2)

    def obtener_detalle(self) -> str:
        return f"Equipment Rental: {self.descripcion} (Days: {self.dias})"


class AsesoriaEspecializada(Servicio):
    def __init__(self, identificador: str, descripcion: str, costo_base: float, horas: int):
        super().__init__(identificador, descripcion, costo_base)
        self.horas = horas

    def validar_parametros(self) -> bool:
        if self.horas <= 0:
            raise ErrorServicioInvalido("Consulting hours must be greater than zero.")
        return True

    def calcular_costo(self, bono_especial: float = 0.0) -> float:
        self.validar_parametros()
        return round((self.costo_base * self.horas) + bono_especial, 2)

    def obtener_detalle(self) -> str:
        return f"Specialized Consulting: {self.descripcion} (Hours: {self.horas})"
