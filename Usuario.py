class Usuario:
    def __init__(self,rut=None,nombres=None,apellido_paterno=None,apellido_materno=None,genero=None,fecha_nacimiento=None,cargo=None,experiencia=None,email=None,contrasea=None,horario=None):
        self._nombres = nombres
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._genero = genero
        self._fecha_nacimiento = fecha_nacimiento
        self._rut = rut
        self._cargo = cargo   
        self._experiencia = experiencia 
        self._email = email
        self._contrasea = contrasea
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
    def apellidoPa(self):
        return self._apellido_paterno
    
    @property
    def apellidoMa(self):
        return self._apellido_materno
    
    @property
    def genero(self):
        return self._genero
    
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @property
    def email(self):
        return self._email
    
    @property
    def rut(self):
        return self._rut
    
    @nombres.setter
    def nombres(self,nuevoN):
        self._nombres = nuevoN

    @apellidoPa.setter
    def apellidoPa(self,nuevoAP):
        self._apellido_paterno = nuevoAP

    @apellidoMa.setter
    def apellidoMa(self,nuevoAM):
        self._apellido_materno = nuevoAM
    
    @genero.setter
    def genero(self,nuevoGe):
        self._genero = nuevoGe
    
    @cargo.setter
    def cargo(self,nuevoCar):
        self._cargo = nuevoCar
    
    @experiencia.setter
    def experiencia(self,nuevoEx):
        self._experiencia = nuevoEx

    @email.setter
    def email(self,nuevoEma):
        self._email = nuevoEma
    
    def get_rut(self):
        return self._rut
    
    def string(self):
        return f"{self._rut},{self._nombres},{self._apellido_paterno},{self._apellido_materno},{self._genero},{self._fecha_nacimiento},{self._cargo},{self._experiencia},{self._email},{self._contrasea}"
    
    def __str__(self):
        return f""" {self._nombres} {self._apellido_paterno} {self._apellido_materno}
        Genero: {self._genero}
        Fecha de nacimiento: {self._fecha_nacimiento}
        Cargo: {self._cargo}
        Experiencia: {self._experiencia}"""