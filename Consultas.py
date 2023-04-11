from AtencionCliente import AgendarHora
from SalasHorario import SalasHorario
from Usuario import Usuario
from ManejoArchivo import GestionArchivo
from Boleta import Boleta
from datetime import datetime
import os

class Consulta(AgendarHora):
    especialidades = ["Neurologia","Reproduccion","Odontologia","Oncologia","Cardiologia"]
    def __init__(self, cliente=None, veterinario=None, mascota=None, tipo_atencion=None, fecha=None,especialidad=None):
        super().__init__(cliente, veterinario, mascota, tipo_atencion, fecha)
        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self,nueva_especialidad):
        self._especialidad = nueva_especialidad

    @classmethod
    def consultaRutinaria(cls,veterinarios,salas,cliente,mascota,contador_mascotas):
        id=0
        os.system("cls")
        objetoVeterinario = []
        for lista in veterinarios:
            veterinario = Usuario(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],horario=None)
            print(f"Veterinario [{id+1}]\n{veterinario}")
            objetoVeterinario.append(veterinario)
            id+=1
        opcionVet = int(input("Que veterinario desea agendar?: "))
        os.system("cls")
        sala = SalasHorario.mostrarHorario(objetoVeterinario[opcionVet-1].rut,salas)
        if sala == False:
            return True
        sala.rut = cliente.get_rut()
        consultaAgendada = Consulta(cliente,objetoVeterinario[opcionVet-1],mascota,"Consulta Rutinaria",sala,especialidad=None)
        os.system("cls")
        GestionArchivo.insertar("salasAgendadas.csv",sala)
        print(consultaAgendada)
        os.system("pause")
        os.system("cls")
        fecha = datetime.now()
        formato = fecha.strftime("%H:%M | %d-%m-%y")
        #REVISAR BOLETA
        #boleta = Boleta(cliente.get_rut(),formato,descuento,25000)
        precio = 25000
        opcionBoleta = int(input("Desea agendar otra hora?  [SI = 1] [NO = 2]: "))
        if opcionBoleta == 1:
            return False 
            
        elif opcionBoleta == 2:
            precio *= contador_mascotas
            if contador_mascotas == 1:
                descuento=0
            else:
                descuento = 0.25
            boleta = Boleta(cliente.get_rut(),formato,descuento,precio)
            print(boleta)
            os.system("pause")
            GestionArchivo.insertar("facturas.csv",boleta)
            return True

    @classmethod
    def consultaEspecialista(cls,veterinarios,salas,cliente,mascota,contador_mascotas):
        i=0
        for especialidad in cls.especialidades:
            print(f"{i+1}. {especialidad}")
            i+=1
        opcionEsp = int(input("Que especialidad requiere: "))
        j=0
        objetosVeterinario = []
        for lista in veterinarios:
            veterinario = Usuario(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],horario=None)
            if veterinario.cargo == cls.especialidades[opcionEsp-1]:
                print(f"Veterinario [{j+1}]\n{veterinario}")
                objetosVeterinario.append(veterinario)
                j+=1

        opcionVet = int(input("Que veterinario desea agendar?: "))
        sala = SalasHorario.mostrarHorario(objetosVeterinario[opcionVet-1].rut,salas)
        if sala == False:
            return True
        consultaEspecial = Consulta(cliente,objetosVeterinario[opcionVet-1],mascota,"Consulta Especialista",sala,cls.especialidades[opcionEsp-1])
        os.system("cls")
        print(consultaEspecial)
        os.system("pause")
        fecha = datetime.now()
        formato = fecha.strftime("%H:%M | %d-%m-%y")
        precio = 25000
        opcionBoleta = int(input("Desea agendar otra hora?  [SI = 1] [NO = 2]: "))
        if opcionBoleta == 1:
            return False 
            
        elif opcionBoleta == 2:
            precio *= contador_mascotas
            if contador_mascotas == 1:
                descuento=0
            else:
                descuento = 0.25
            boleta = Boleta(cliente.get_rut(),formato,descuento,precio)
            print(boleta)
            os.system("pause")
            GestionArchivo.insertar("facturas.csv",boleta)
            return True
        
    @classmethod
    def consultaTerreno(cls,veterinarios,salas,cliente,mascota,contador_mascotas):
        os.system("cls")
        print("1. Veterinario Rural(Animales de granja)")
        print("2. Veterinario Domestico(Animales domesticos)")
        print("3. Veterinario Silvestre")
        opcionVet = int(input("Que veterinario deseas: "))
        fechaEle = input("Para que dia deseas agendar?(00/00/00): ")

        os.system("cls")
        sala = SalasHorario.horarioTerreno(veterinarios[opcionVet-1].rut,salas)
        sala.fecha = fechaEle
        consultaTerreno = Consulta(cliente,veterinarios[opcionVet-1],mascota,"Consulta en Terreno",sala,veterinarios[opcionVet-1].cargo)
        print(consultaTerreno)
        os.system("pause")
        os.system("cls")
        fecha = datetime.now()
        formato = fecha.strftime("%H:%M | %d-%m-%y")
        precio = 25000
        opcionBoleta = int(input("Desea agendar otra hora?  [SI = 1] [NO = 2]: "))
        if opcionBoleta == 1:
            return False 
            
        elif opcionBoleta == 2:
            precio *= contador_mascotas
            if contador_mascotas == 1:
                descuento=0
            else:
                descuento = 0.25
            boleta = Boleta(cliente.get_rut(),formato,descuento,precio)
            print(boleta)
            os.system("pause")
            GestionArchivo.insertar("facturas.csv",boleta)
            return True

    @classmethod
    def realizarConsulta(cls,cliente,mascota,contador_mascotas):
        os.system("cls")
        print("1. Consulta rutinaria")
        print("2. Consulta con Especialista")
        print("3. Consulta en terreno")
        opcion = int(input("Que tipo de consulta desea: "))
        if opcion == 1:
            #Cargar archivo csv            
            veterinarios = GestionArchivo.seleccionarTodo("veterinarios.csv")
            salas = GestionArchivo.seleccionarTodo("salas.csv")

            boolean = cls.consultaRutinaria(veterinarios,salas,cliente,mascota,contador_mascotas)
            if boolean:
                return True
        elif opcion == 2:
            veterinariosEsp = GestionArchivo.seleccionarTodo("veterinarios.csv")
            salasEsp = GestionArchivo.seleccionarTodo("salas.csv")
            boolean = cls.consultaEspecialista(veterinariosEsp,salasEsp,cliente,mascota,contador_mascotas)
            if boolean:
                return True
        
        elif opcion == 3:
            veterinario_Rural = Usuario("21295966-9","ElPipeCC","Castro","Casanova","Dudoso","14/05/2003","Veterinario Rural","10 años",horario=None)
            veterinario_Domestico = Usuario("20983940-7","LostDiego15o17","Jaune","Ramirez","Lolero","08/03/2002","Veterinario Domestico","Nuevo",horario=None)
            veterinario_Silvestre = Usuario("21454138-6","Finixk","Asencio","Sanhueza","Lolero","24/11/2003","Veterinario Silvestre","1 año",horario=None)
            veterinariosTerre = [veterinario_Rural,veterinario_Domestico,veterinario_Silvestre]

            horaTerreno1 = SalasHorario(veterinario_Rural.rut,cliente.get_rut(),"Terreno","17:00-18:40")
            horaTerreno2 = SalasHorario(veterinario_Domestico.rut,cliente.get_rut(),"Terreno","12:00-13:40")
            horaTerreno3 = SalasHorario(veterinario_Silvestre.rut,cliente.get_rut(),"Terreno","15:00-16:40")
            horasTerr = [horaTerreno1,horaTerreno2,horaTerreno3]
            boolean = Consulta.consultaTerreno(veterinariosTerre,horasTerr,cliente,mascota,contador_mascotas)
            if boolean:
                return True

    def __str__(self):
        return f"""{super().__str__()}
        Especialidad: {self._especialidad}"""    