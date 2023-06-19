from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
from uiReservaCtRutinario import Ui_MainWindow
import ventanaReserva
import ventanaHorarios

class ventanaCRutinario(QMainWindow):
    def __init__(self, cont, hora):
        super().__init__()
        self.cont = cont
        self.hora = hora
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.horario = ventanaHorarios.ventanaHorarios(0, self.cont)
        self.ventanaUi.ButtonHorarios.clicked.connect(lambda : self.cambio(self.horario))
        self.ventanaUi.ButtonAtras.clicked.connect(self.atras)
        self.actualizarComboBoxMascota()
        self.actualizarLabel()

    def actualizarComboBoxMascota(self):
        with open("clientes.csv") as r:
            reader = csv.reader(r)
            next(reader)
            i = 1
            for l in reader:
                if i == self.cont:
                    rutCliente = l[0]
                    break
                i += 1

        with open('mascotas.csv') as file:
            reader = csv.reader(file)
            next(reader)
            self.mascota = []
            for l in reader:
                if l[0] == rutCliente:
                    self.mascota.append(l)

        for mascota in self.mascota:
            self.ventanaUi.MascotaComboBox.addItem(mascota[1])
    
    def actualizarLabel(self):
        if self.hora == []:
            self.ventanaUi.subMenu_2.setText("El horario escogido se mostrará aqui...")
        else:
            self.ventanaUi.subMenu_2.setText("Horario Escogido:\nFecha: " + self.hora[0] +"\nHorario: " + self.hora[1] + "\nSala N° " + self.hora[2])
    
    def cambio(self, ventana):
        ventana.actualizarHorario()
        ventana.show()
        self.hide()
        
    def atras(self):
        self.ventanaReserva = ventanaReserva.ventanaReserva()
        self.ventanaReserva.show()
        self.hide()
