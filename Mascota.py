from ManejoArchivo import GestionArchivo
class Mascota:
    def __init__(self,id=None,nombre=None,especie=None,raza=None,fecha_nacimiento=None,sexo=None,peso=None,tamanho=None,volumen=None):
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
        self._peso = peso
        self._tamanho = tamanho
        self._volumen = volumen
        self._ficha_medica = []

    @property
    def rut(self):
        return self._id
    
    @rut.setter
    def rut(self,nuevo_id):
        self._id = nuevo_id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self,nueva_especie):
        self._especie = nueva_especie

    @property
    def raza(self):
        return self._raza
    
    @raza.setter
    def raza(self,nueva_raza):
        self._raza = nueva_raza
    
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,nueva_fecha):
        self._fecha_nacimiento = nueva_fecha

    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self,nuevo_sexo):
        self._sexo = nuevo_sexo

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self,nuevo_peso):
        self._peso = nuevo_peso

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self,nuevo_tamanho):
        self._tamanho = nuevo_tamanho
    
    @property
    def volumen(self):
        return self._volumen
    
    @volumen.setter
    def volumen(self,nuevo_volumen):
        self._volumen = nuevo_volumen

    def string(self):
        return f"{self._id},{self._nombre},{self._especie},{self._raza},{self._fecha_nacimiento},{self._sexo},{self._peso},{self._tamanho},{self._volumen}"

    @classmethod
    def ingresarMascota(cls,rut):
        nombre = input("\nNombre de la mascota: ")
        especie = input("Nombre de la especie: ")
        raza = input("Que raza es: ")
        fecha_nacimiento = input("Fecha de nacimiento: ")
        sexo = input("Sexo: ")
        peso = input("Peso: ")
        tamanho = input("Tamanho (aprox): ")
        volumen = input("Volumen de la mascota: ")
        mascota = Mascota(rut,nombre,especie,raza,fecha_nacimiento,sexo,peso,tamanho,volumen)
        GestionArchivo.insertar("mascotas.csv",mascota)
        return mascota


    def __str__(self):
        return f"""
        Animal [{self._id}]
        Nombre: {self._nombre}
        Especie: {self._especie}
        Raza: {self._raza}
        Fecha Nacimiento: {self._fecha_nacimiento}
        Sexo: {self._sexo}
        Peso: {self._peso}kg
        Tamanho: {self._tamanho}
        Volumen: {self._volumen}m3"""
    
if __name__ == "__main__":
    PerroJuan = Mascota(1,"Juan","Perro","Pudul","10/11/2006","Macho","5kg",1.33,33,1)

    print(PerroJuan)