import os
from AtencionCliente import AgendarHora
from ClaseCliente import Cliente
from datetime import datetime
from Usuario import Usuario
from ManejoArchivo import GestionArchivo
from Mascota import Mascota
from Boleta import Boleta
class Urgencia(AgendarHora):
    def __init__(self, cliente=None, veterinario=None, mascota=None, tipo_atencion=None,fecha=None,gravedad=None):
        super().__init__(cliente, veterinario, mascota, tipo_atencion,fecha)
        self._gravedad = gravedad

    @property
    def gravedad(self):
        return self._gravedad
    
    @gravedad.setter
    def gravedad(self,nueva_gravedad):
        self._gravedad = nueva_gravedad

    @classmethod
    def ingresarUrgencia(cls,veterinario):
        os.system("cls")
        print("Opcion 1:Ingresar Mascota")
        print("Opcion 2:Solicitar Ambulancia")
        opcion= int(input(">>> "))

        if opcion == 1:
            ingresados = []
            os.system("cls")
            print("1. Cliente nuevo")
            print("2. Cliente frecuente")
            opcion2 = int(input(">>> "))
            mascotas = []
            if opcion2 == 1:
                cliente_seleccionado = Cliente.ingresoCliente()
                GestionArchivo.insertar("clientes.csv",cliente_seleccionado)
                rutCliente = cliente_seleccionado
                
            elif opcion2 == 2:
                buscar_rut = input("Ingrese rut(21454138-6): ")
                rutCliente = Cliente(rut=buscar_rut)
                listas = GestionArchivo.seleccionar("clientes.csv",rutCliente)
                for lista in listas:
                    cliente_seleccionado = Cliente(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8])
                    
            ingresados.append(cliente_seleccionado)
            listasMascotas = GestionArchivo.seleccionar("mascotas.csv",rutCliente)
            os.system("cls")
            print("Mascotas Encontradas".center(50,"-"))
            i=0
            for listaM in listasMascotas:
                mascotaM = Mascota(listaM[0],listaM[1],listaM[2],listaM[3],listaM[4],listaM[5],listaM[6],listaM[7],listaM[8])
                print(f"Mascota numero[{i+1}]") 
                print(mascotaM)
                i+=1
                mascotas.append(mascotaM)
                        
            id_mascota = int(input("Que mascota desea ingresar?: "))
            fecha = datetime.now()
            formato = fecha.strftime("%H:%M | %d-%m-%y")
            urgencia = Urgencia(cliente_seleccionado,veterinario,mascotas[id_mascota-1],"Urgencia",formato,"ROJO")
            ingresados.append(mascotas[id_mascota-1])
            os.system("cls")
            print(urgencia)
            os.system("pause")
            os.system("cls")
            opcdescuento = input("La mascota llego en ambulancia?  [SI = 1] [NO = 2]: ")
            if opcdescuento == 1:
                descuento = float(-0.15)
            else:
                descuento = 0
            boleta = Boleta(cliente_seleccionado.get_rut(),formato,descuento,25000)
            print(boleta)
            os.system("pause")
            GestionArchivo.insertar("facturas.csv",boleta)
            return ingresados
        elif opcion == 2:
            os.system("cls")
            domicilio = input("Ingrese domicilio a donde requiera la ambulancia: ")
            rut = input("Ingrese rut: ")
            fecha = datetime.now()
            formato = fecha.strftime("%H:%M | %d-%m-%y")
                
            cliente_ambulancia = Cliente(rut=rut,domicilio=domicilio)    
            ambulanciaUrgencia = Urgencia(cliente=cliente_ambulancia,veterinario=veterinario,tipo_atencion="Ambulancia",fecha=formato)
            os.system("cls")
            print(ambulanciaUrgencia)
            os.system("pause")

    def __str__(self):
        return f"""{super().__str__()}
        Gravedad: {self._gravedad}"""
    