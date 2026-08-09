# Clase padre
class Cliente:

    def __init__(self, identificador, nombre, email, telefono, direccion):

        if identificador == "":
            raise ValueError("El identificador es obligatorio")

        if nombre == "":
            raise ValueError("El nombre es obligatorio")

        if "@" not in email:
            raise ValueError("El email no es válido")

        if telefono == "":
            raise ValueError("El teléfono es obligatorio")

        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números")

        if direccion == "":
            raise ValueError("La dirección es obligatoria")

        self.__identificador = identificador
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__direccion = direccion


    def getIdentificador(self):
        return self.__identificador

    def getNombre(self):
        return self.__nombre

    def getEmail(self):
        return self.__email

    def getTelefono(self):
        return self.__telefono

    def getDireccion(self):
        return self.__direccion


    def obtener_datos(self):
        return (
            f"ID: {self.__identificador} | "
            f"Nombre: {self.__nombre} | "
            f"Email: {self.__email} | "
            f"Teléfono: {self.__telefono} | "
            f"Dirección: {self.__direccion}"
        )


    # Método especial solicitado en la pauta
    def __str__(self):
        return self.obtener_datos()


    # Dos clientes son iguales si tienen el mismo ID
    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self.__identificador == otro.getIdentificador()

        return False

# Clase hija (subclase)
# Cliente Regular

class ClienteRegular(Cliente):

    def __init__(
        self,
        identificador,
        nombre,
        email,
        telefono,
        direccion,
        puntos_acumulados
    ):

        super().__init__(
            identificador,
            nombre,
            email,
            telefono,
            direccion
        )

        if puntos_acumulados < 0:
            raise ValueError(
                "Los puntos acumulados no pueden ser negativos"
            )

        self.__puntos_acumulados = puntos_acumulados


    def getPuntosAcumulados(self):
        return self.__puntos_acumulados


    # Polimorfismo: sobrescritura de obtener_datos()
    def obtener_datos(self):
        return (
            f"{super().obtener_datos()} | "
            f"Tipo: Regular | "
            f"Puntos acumulados: {self.__puntos_acumulados}"
        )

# Clase hija (subclase)
# Cliente Premium

class ClientePremium(Cliente):

    def __init__(
        self,
        identificador,
        nombre,
        email,
        telefono,
        direccion,
        nivel_membresia,
        porcentaje_descuento
    ):

        super().__init__(
            identificador,
            nombre,
            email,
            telefono,
            direccion
        )

        if nivel_membresia == "":
            raise ValueError(
                "El nivel de membresía es obligatorio"
            )

        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise ValueError(
                "El porcentaje debe estar entre 0 y 100"
            )

        self.__nivel_membresia = nivel_membresia
        self.__porcentaje_descuento = porcentaje_descuento


    def getNivelMembresia(self):
        return self.__nivel_membresia

    def getPorcentajeDescuento(self):
        return self.__porcentaje_descuento


    # Polimorfismo
    def obtener_datos(self):
        return (
            f"{super().obtener_datos()} | "
            f"Tipo: Premium | "
            f"Nivel: {self.__nivel_membresia} | "
            f"Descuento: {self.__porcentaje_descuento}%"
        )

# Clase hija (subclase)
# Cliente Corporativo

class ClienteCorporativo(Cliente):

    def __init__(
        self,
        identificador,
        nombre,
        email,
        telefono,
        direccion,
        empresa,
        limite_credito
    ):

        super().__init__(
            identificador,
            nombre,
            email,
            telefono,
            direccion
        )

        if empresa == "":
            raise ValueError(
                "La empresa es obligatoria"
            )

        if limite_credito < 0:
            raise ValueError(
                "El límite de crédito no puede ser negativo"
            )

        self.__empresa = empresa
        self.__limite_credito = limite_credito


    def getEmpresa(self):
        return self.__empresa

    def getLimiteCredito(self):
        return self.__limite_credito


    # Polimorfismo
    def obtener_datos(self):
        return (
            f"{super().obtener_datos()} | "
            f"Tipo: Corporativo | "
            f"Empresa: {self.__empresa} | "
            f"Límite de crédito: ${self.__limite_credito}"
        )

