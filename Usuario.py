class Usuario:
    def __init__(self,rut=None,nombres=None,apellido_paterno=None,apellido_materno=None,genero=None,fecha_nacimiento=None,cargo=None,experiencia=None,horario=None):
        self._nombres = nombres
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._genero = genero
        self._fecha_nacimiento = fecha_nacimiento
        self._rut = rut
        self._cargo = cargo   
        self._experiencia = experiencia 
        self._horario = horario

    @property
    def experiencia(self):
        return self._experiencia
    
    @property
    def cargo(self):
        return self._cargo
    @property
    def nombres(self):
        return self._nombres
    
    @property
    def rut(self):
        return self._rut
    
    def get_rut(self):
        return self._rut
    
    def string(self):
        return f"{self._rut},{self._nombres},{self._apellido_paterno},{self._apellido_materno},{self._genero},{self._fecha_nacimiento},{self._cargo},{self._experiencia}"
    
    def __str__(self):
        return f""" {self._nombres} {self._apellido_paterno} {self._apellido_materno}
        Genero: {self._genero}
        Fecha de nacimiento: {self._fecha_nacimiento}
        Cargo: {self._cargo}
        Experiencia: {self._experiencia}"""