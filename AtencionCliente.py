#from operaciones import Operaciones
#from urgencias import Urgencias
import os 
from ManejoArchivo import GestionArchivo
from ClaseCliente import Cliente
#from Urgencia import Urgencia
from Usuario import Usuario
#from Consulta import Consulta


class AgendarHora:
    #clientes = []
    def __init__(self, cliente,veterinario, mascota, tipo_atencion,fecha):
        self.cliente = cliente
        self.veterinario = veterinario
        self.mascota = mascota
        self.tipo_atencion = tipo_atencion
        self.fecha = fecha

    @classmethod 
    def reservarHora(cls):        
        tipo_atencion = input("""Que tipo de consulta viene el paciente:
        1. Consultas
        2. Urgencias
        3. Operaciones
        Seleccione un numero...   
        """)
        
        if tipo_atencion == "1":                         
            i=0 
            mascotas = []
            for mascota in mascotas:
                print(f"Mascota numero[{i+1}]")               
                print(mascota)
                i+=1
            opcionMascota = int(input("Que mascota desea agendar?: "))
            #Consulta.realizarConsulta(cliente,mascotas[opcionMascota])                   
        elif tipo_atencion == "2":
            #urgencia = Urgencias()
            #urgencia.menu()
            pass
        
        elif tipo_atencion == "3":
            #operacion = Operaciones()
            #
            # operacion.mostrarMenuOP()
            pass

        elif tipo_atencion == "4":
                return
        
        else:
            print ("Ingrese una opcion valida")
        
    def __str__(self):
        return f"""Hora agendada {self.fecha}
        Tipo de Atencion: {self.tipo_atencion}
        Veterinario asignado: {self.veterinario}
        \nCliente: {self.cliente}
        Mascota: {self.mascota}"""
    
    


        

