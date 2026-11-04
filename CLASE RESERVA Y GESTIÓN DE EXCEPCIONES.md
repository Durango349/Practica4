# ==========================================
# CLASE RESERVA Y GESTIÓN DE EXCEPCIONES
# ==========================================
class Reserva:
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pending"

    def confirmar(self) -> str:
        try:
            if self.estado == "Confirmed":
                raise ErrorReservaInvalido("Reservation has already been confirmed previously.")
            self.estado = "Confirmed"
            logging.info(f"Reservation {self.id_reserva} confirmed successfully.")
            return f"[SUCCESS] Reservation {self.id_reserva} confirmed for {self.cliente.nombre}."
        except ErrorReservaInvalido as e:
            logging.error(f"Error confirming reservation {self.id_reserva}: {e}")
            return f"[CONTROLLED ERROR] {e}"
        finally:
            pass

