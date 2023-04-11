import csv
import os
from Usuario import Usuario
from Urgencia import Urgencia
from ManejoArchivo import GestionArchivo

class Urgencias:
    
    def __init__(self):
        self.lista_prioridad = []
    
    def menu(self):
        while True:
            self.limpiar_pantalla()

            print("""
            Seleccione una opción:

            1. Ingreso de paciente
            2. Mostrar urgencias
            3. Salir

            """)
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.orden_atencion()

            elif opcion == "2":
                self.verUrgencias()

            elif opcion == "3":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida, intente nuevamente.")
    
    def orden_atencion(self):
        self.limpiar_pantalla()

        gravedades_permitidas = ["1", "2", "3", "4", "5"]
        gravedad = input("""
        Indique gravedad (solo el número):
        E.S.I 1 (leve)
        E.S.I 2 (leve)
        E.S.I 3 (mediana)
        E.S.I 4 (severa)
        E.S.I 5 (extrema)
        ................

        """)
        if gravedad not in gravedades_permitidas:
            print("Gravedad no válida, intente ingresando el número de la gravedad")
            return
        
        archivo = f"Archivos de urgencias/ESI_{gravedad}.csv"
        rutVet = Usuario(rut="24448886-2")
        listas = GestionArchivo.seleccionar("veterinarios.csv",rutVet)
        for lista in listas:
            veterinario_urgencia = Usuario(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],horario=None)
        ingresados = Urgencia.ingresarUrgencia(veterinario_urgencia)

        rut = ingresados[0].get_rut()
        nombre_paciente = ingresados[1].nombre
        nombre_dueño = ingresados[0].get_nombres()
        especie = ingresados[1].especie

        with open(archivo, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([rut,nombre_paciente, nombre_dueño, especie])
            self.lista_prioridad.append((rut,nombre_paciente, nombre_dueño, especie, gravedad))
        
        print(f"Paciente {nombre_paciente} ingresado en la lista de urgencias con gravedad E.S.I {gravedad}.")

    def verUrgencias(self):
        for gravedad in range(1, 6):
            archivo = f"Archivos de urgencias/ESI_{gravedad}.csv"
            with open(archivo, mode="r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                if len(rows) > 0:
                    print(f"Urgencias E.S.I {gravedad}:")
                    for row in rows:
                        if len(row) >= 3:
                            print(f"rut: {row[0]}   {row[1]}, ({row[3]}) - Dueño: {row[2]}")
                else:
                    print(f"No hay urgencias en ESI {gravedad}.")
                print()
        a = input("Presione enter para volver...")
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')




