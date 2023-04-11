import csv # para los archivos
import os #para cleanear la pantalla


class Operaciones:
    
    def reservarQuirofano(self):
        salas = input("Ingrese sala para reservar: ")
        personal_requerido = int(input("¿Cuanto personal requiere?: "))
        horario = input("Ingrese el horario (mañana, medio dia, tarde): ")

        reserva = [personal_requerido, salas, horario]

        with open("reservasQuirofano.csv", 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(reserva)
        
        self.limpiar_pantalla()    
    
    def verReservas(self):

        with open('reservasQuirofano.csv', 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            
            hay_reservas = False

            for reserva in lector_csv:
                if len(reserva) >= 2:
                    print(f"Cantidad de personal: {reserva[0]}, Sala: {reserva[1]}, Horario: {reserva[2]}")
                    hay_reservas = True

            if hay_reservas == False:
                print("No hay reservas.")
            
            a = input("Presione enter para volver...")        

    def mostrarMenuOP(self):
        
        while True:
            
            self.limpiar_pantalla()

            print("1. Hacer una reserva")
            print("2. Ver reservas")
            print("3. Volver al menu principal")
            opcion = input("Seleccione una opción: ")
            print()
            
            if opcion == "1":
                self.reservarQuirofano()
            elif opcion == "2":
                self.verReservas()
            elif opcion == "3":
                return
            else:
                print("Opción inválida. Intente nuevamente.")
            

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
