#from ManejoArchivo import GestionArchivo
import os
from Mascota import Mascota
class Cliente:
    clientes = []
    def __init__(self, rut=None,nombres=None, apellido_paterno=None, apellido_materno=None, genero=None, fecha_nacimiento=None, email=None, telefono=None, domicilio=None):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio
        self.mascotas = []
        self.historial = []
    
    @property
    def id(self):
        return self.id_cliente

    def set_id(self, id_cliente):
        self.id_cliente = id_cliente

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
        return f"{self.rut},{self.nombres},{self.apellido_paterno},{self.apellido_materno},{self.genero},{self.fecha_nacimiento},{self.email},{self.telefono},{self.domicilio}"
    
    @classmethod
    def ingresoCliente(cls):
        os.system("cls")
        print("Ingresando Cliente Nuevo".center(50,"-"))
        NombreNuevo=(input("\nIngrese Nombres: "))
        ApellidoPNuevo=(input("Ingrese apellido paterno: "))
        ApellidoMNuevo=(input("Ingrese apellido materno: "))
        GeneroNuevo=(input("Ingrese Genero: "))
        FechaNacimientoNuevo=(input("Ingrese Fecha Nacimiento: "))
        booleano = True
        while booleano:
            RutNuevo=(input("Ingrese Rut (21454138-6): "))
            booleano = Cliente.verificarRut(RutNuevo)        
        CorreoNuevo=(input("Ingrese Correo Electronico: "))
        TelefonoNuevo=(input("Ingrese Telefono: "))
        DomicilioNuevo=(input("Ingrese Domicilio: "))
        MascotasCantidad = int(input("Cuantos Mascotas tiene?: "))
        cliente = Cliente(RutNuevo,NombreNuevo,ApellidoPNuevo,ApellidoMNuevo,GeneroNuevo,FechaNacimientoNuevo,CorreoNuevo,TelefonoNuevo,DomicilioNuevo)
        for i in range(MascotasCantidad): 
            os.system("cls")
            print(f"Ingresando Mascota [{i+1}]".center(50,"-"))          
            cliente.añadirMascota(Mascota.ingresarMascota(RutNuevo))            
        return cliente

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
        
