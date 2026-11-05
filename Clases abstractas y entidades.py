# ==========================================
# CLASES ABSTRACTAS Y ENTIDADES
# ==========================================
class EntidadBase(ABC):
    def __init__(self, identificador: str):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def obtener_detalle(self) -> str:
        pass


class Cliente(EntidadBase):
    def __init__(self, identificador: str, nombre: str, email: str, telefono: str):
        super().__init__(identificador)
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ErrorClienteInvalido("Client name is invalid (minimum 3 characters required).")
        self.__nombre = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ErrorClienteInvalido("Email address format is invalid.")
        self.__email = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit() or len(valor) < 7:
            raise ErrorClienteInvalido("Phone number must contain only digits and be at least 7 characters long.")
        self.__telefono = valor

    def obtener_detalle(self) -> str:
        return f"Customer [ID: {self._identificador}, Name: {self.__nombre}, Email: {self.__email}]"


class Servicio(EntidadBase, ABC):
    def __init__(self, identificador: str, descripcion: str, costo_base: float):
        super().__init__(identificador)
        self.descripcion = descripcion
        self.costo_base = costo_base

    @property
    def costo_base(self):
        return self.__costo_base

    @costo_base.setter
    def costo_base(self, valor):
        if valor < 0:
            raise ErrorServicioInvalido("Base cost cannot be negative.")
        self.__costo_base = valor

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def validar_parametros(self) -> bool:
        pass
