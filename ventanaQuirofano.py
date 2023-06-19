from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
import sys
import csv
from uiReservaQuirofano import Ui_MainWindow
from ManejoArchivo import GestionArchivo
import ventanaMenuReserva
import ventanaHorarios

class ventanaQuirofano(QMainWindow):
    def __init__(self, cont, hora):
        super().__init__()
        self.cont = cont
        self.hora = hora
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.horario = ventanaHorarios.ventanaHorarios(1, self.cont)
        self.ventanaUi.ButtonHorarios.clicked.connect(lambda : self.cambio(self.horario))
        self.ventanaUi.ButtonAgendarHora.clicked.connect(lambda: self.agendar())
        self.ventanaUi.ButtonAtras.clicked.connect(lambda: self.volver(ventanaMenuReserva.ventanaMenuReserva(self.cont)))
        self.actualizarComboBoxMascota()
        self.actualizarLabel()

    def volver(self, ventana):
        ventana.show()
        self.hide()
    
    def actualizarComboBoxMascota(self):
        with open("clientes.csv") as r:
            reader = csv.reader(r)
            next(reader)
            i = 1
            for l in reader:
                if i == self.cont:
                    self.rutCliente = l[0]
                    self.nombreC = l[1]
                    break
                i += 1

        with open('mascotas.csv') as file:
            reader = csv.reader(file)
            next(reader)
            self.mascota = []
            for l in reader:
                if l[0] == self.rutCliente:
                    self.mascota.append(l)

        for mascota in self.mascota:
            self.ventanaUi.MascotaComboBox.addItem(mascota[1])
    
    # def retroceder(self):
    #     self.ventanaReserva.show()
    #     self.close()
    
    def actualizarLabel(self):
        if self.hora == []:
            self.ventanaUi.subMenu_2.setText("El horario escogido se mostrará aqui...")
        else:
            self.ventanaUi.subMenu_2.setText("Horario Escogido:\nFecha: " + self.hora[0] +"\nHorario: " + self.hora[1] + "\nSala N° " + self.hora[2])
    
    def agendar(self):
        if(self.hora == [] or self.ventanaUi.MascotaComboBox.currentIndex() == 0):
            qtw.QMessageBox.warning(self, "ERROR, Datos incompletos", "Por favor revise si ha escogido una mascota, o, si ha escogido un horario.")
        else:
            i = 1
            for l in self.mascota:
                if i == self.ventanaUi.MascotaComboBox.currentIndex():
                    nombreMascota = l[1]
                    break
                i += 1
            
            with open('salas.csv') as file:
                reader = csv.reader(file)
                next(reader)
                i = 0
                for l in reader:
                    if l[4] == self.hora[0] and l[3] == self.hora[1] and l[2] == self.hora[2]:
                        posFila = i
                        break
                    i += 1
            #se cambian los valores del csv de sala, la posicion 1 y 5 (se cambia el rut de cliente de null a self.rutCliente y de False a True)
            GestionArchivo.modificarLinea("salas.csv",posFila,1,self.rutCliente)
            GestionArchivo.modificarLinea("salas.csv",posFila,5,"True")
            
            #Y se inserta al csv de control las variables del nombre de la mascota y la fecha hora y sala
            reserva = [self.hora[0],nombreMascota,self.hora[1],self.hora[2]]
            with open("Quirofano.csv","a",newline="") as archivo:
                escritor = csv.writer(archivo,delimiter=",") 
                escritor.writerow(reserva)
            msg = qtw.QMessageBox()
            msg.setWindowTitle("Reserva Quirofano realizada con exito.")
            msg.setText("Felicidades señor " + self.nombreC + " su reserva ha sido realizada con exito.\nSi necesita saber mas detalles, dirigase hacia Lista de Reservas para cancelar, modificar o mostrar su reserva.")
            msg.exec_()
            self.volver(ventanaMenuReserva.ventanaMenuReserva(self.cont))
            
            
    
    def cambio(self, ventana):
        ventana.actualizarHorario()
        ventana.show()
        self.hide()