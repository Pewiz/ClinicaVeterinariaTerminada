#from ManejoArchivo import GestionArchivo
import os
from Mascota import Mascota
class Usuario:
    usuarios = []
    def __init__(self, rut=None,nombres=None, apellido_paterno=None, apellido_materno=None, genero=None, fecha_nacimiento=None, email=None, telefono=None, domicilio=None, cargo=None, experiencia=None, password=None):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio
        self.cargo = cargo
        self.experiencia = experiencia
        self.password = password
    
    @property
    def id(self):
        return self.id_usuario

    def set_id(self, id_usuario):
        self.id_usuario = id_usuario

    def get_nombres(self):
        return self.nombres

    def set_nombres(self, nombres):
        self.nombres = nombres
    
    def get_apellido_materno(self):
        return self.apellido_materno
    
    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno
    
    def get_apellido_paterno(self):
        return self.apellido_paterno
    
    def set_apellido_paterno(self, apellido_paterno):
        self.apellido_paterno = apellido_paterno
        
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def get_rut(self):
        return self.rut

    def set_rut(self, rut):
        self._rut = rut

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_domicilio(self):
        return self.domicilio

    def set_domicilio(self, domicilio):
        self.domicilio = domicilio

    def get_mascotas(self):
        return self.mascotas

    def set_mascotas(self, mascotas):
        self.mascotas = mascotas

    def get_historial(self):
        return self._historial

    def set_historial(self, historial):
        self._historial = historial
        
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo
        
    def get_experiencia(self):
        return self._experiencia

    def set_experiencia(self, experiencia):
        self._experiencia = experiencia
        
    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
    
    def añadirMascota(self,mascota):
        self.mascotas.append(mascota)
    
    def mostrarMascotas(self):
        mascotas = ""
        for mascota in self.mascotas:
            mascotas += mascota.nombre +" "
        return mascotas
    
    @classmethod
    def verificarRut(cls,rut):
        if 9 <= len(rut) <=10:
            return False
        else:
            print("Ingrese Rut con el formato indicado")
            return True

    def string(self):
        return f"{self.rut},{self.nombres},{self.apellido_paterno},{self.apellido_materno},{self.genero},{self.fecha_nacimiento},{self.email},{self.telefono},{self.domicilio},{self.cargo},{self.experiencia},{self.password}"
    
    @classmethod
    def ingresoUsuario(cls):
        os.system("cls")
        print("Ingresando Usuario Nuevo".center(50,"-"))
        NombreNuevo=(input("\nIngrese Nombres: "))
        ApellidoPNuevo=(input("Ingrese apellido paterno: "))
        ApellidoMNuevo=(input("Ingrese apellido materno: "))
        GeneroNuevo=(input("Ingrese Genero: "))
        FechaNacimientoNuevo=(input("Ingrese Fecha Nacimiento: "))
        booleano = True
        while booleano:
            RutNuevo=(input("Ingrese Rut (21454138-6): "))
            booleano = Usuario.verificarRut(RutNuevo)        
        CorreoNuevo=(input("Ingrese Correo Electronico: "))
        TelefonoNuevo=(input("Ingrese Telefono: "))
        DomicilioNuevo=(input("Ingrese Domicilio: "))
        MascotasCantidad = int(input("Cuantos Mascotas tiene?: "))
        usuario = Usuario(RutNuevo,NombreNuevo,ApellidoPNuevo,ApellidoMNuevo,GeneroNuevo,FechaNacimientoNuevo,CorreoNuevo,TelefonoNuevo,DomicilioNuevo)
        for i in range(MascotasCantidad): 
            os.system("cls")
            print(f"Ingresando Mascota [{i+1}]".center(50,"-"))          
            usuario.añadirMascota(Mascota.ingresarMascota(RutNuevo))            
        return usuario

    def __str__(self):
        return f"""
        Nombre: {self.nombres} {self.apellido_paterno} {self.apellido_materno}
        Genero: {self.genero}
        Fecha nacimiento: {self.fecha_nacimiento}
        Rut: {self.rut}
        Contacto: {self.email} Domicilio: {self.domicilio} Telefono: {self.telefono}
        Mascotas: {self.mostrarMascotas()}
        Historial: {self.historial}
        """
        
