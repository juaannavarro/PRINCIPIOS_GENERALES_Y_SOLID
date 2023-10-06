class Usuario:
    def __init__(self, dni, nombre, apellido, calle, telefono, mail, password, n_pedidos, dinero, alergias):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.calle = calle
        self.telefono = telefono
        self.mail = mail
        self.password = password
        self.n_pedidos = n_pedidos
        self.dinero = dinero
        self.alergias = alergias
        
    def __str__(self):
        return f"{self.dni} {self.nombre} {self.apellido} {self.calle} {self.telefono} {self.mail} {self.password} {self.n_pedidos} {self.dinero}"

    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "calle": self.calle,
            "telefono": self.telefono,
            "mail": self.mail,
            "password": self.password,
            "n_pedidos": self.n_pedidos,
            "dinero": self.dinero
        }