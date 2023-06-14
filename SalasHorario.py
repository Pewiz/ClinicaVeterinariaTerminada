from ManejoArchivo import GestionArchivo
class SalasHorario:
    def __init__(self,id=None,rut=None,sala=None,horario=None,fecha=None,disp=None):
        self._id = id
        self._rut = rut
        self._sala = sala
        self._horario = horario
        self._fecha = fecha
        self.disp = disp

    @property
    def id(self):
        return self._id
    
    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self,rut):
        self._rut = rut
    
    @property
    def numSala(self):
        return self._sala
    
    @property
    def horario(self):
        return self._horario

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self,fecha):
        self._fecha = fecha
    
    def string(self):
        return f"{self._id},{self._rut},{self._sala},{self._horario},{self._fecha},{self.disp}"
    
    @classmethod
    def verificarFecha(cls,objeto,fechaEnc):
        salasAgendadas = GestionArchivo.seleccionarTodo("salasAgendadas.csv")
        for salaAgendada in salasAgendadas:
            try:
                objetoEnc = SalasHorario(id=salaAgendada[0],rut=None,sala=salaAgendada[2],horario=salaAgendada[3],fecha=salaAgendada[4])
                if objetoEnc.fecha == fechaEnc:
                    if objeto.horario == objetoEnc.horario:
                        return False
            except Exception:
                return True
        return True

    @classmethod
    def mostrarHorario(cls,rut,salas):
        while True:
            i=0
            fecha = input("Ingresa fecha que deseas agendar(00/00/00): ")
            salasEncontradas = []
            for sala in salas:
                objetoSala = SalasHorario(id=sala[0],sala=sala[1],horario=sala[2],fecha=None)

                boolean = cls.verificarFecha(objetoSala,fecha)
                
                if objetoSala.id == rut and boolean:
                    print(f"Codigo Sala [{i+1}]\n{objetoSala}\n")
                    salasEncontradas.append(objetoSala)
                    i+=1          
            if i==0:
                print("Horas no disponibles en la fecha seleccionada")
                salir = int(input("Ingresa 1 si deseas salir: "))
                if salir == 1:
                    return False
            else:
                break
        opcionSala = int(input("Ingresa el codigo de la sala que deseas: "))
        salasEncontradas[opcionSala-1].fecha = fecha
        return salasEncontradas[opcionSala-1]
    
    
    @classmethod
    def horarioTerreno(cls,rut,salas):
        i=0
        
        for sala in salas:
            if sala.id == rut:
                print(f"Hora Terreno [{i+1}]\n{sala.horario}\n")
            i+=1
        opcionSala = int(input("Que Horario deseas?: "))
        return salas[opcionSala-1]
    
    def __str__(self):
        return f"""ID[{self._id}]
        Rut cliente: {self._rut}
        Sala: {self._sala}
        Fecha: {self._fecha}
        Hora: {self._horario}"""
        
        