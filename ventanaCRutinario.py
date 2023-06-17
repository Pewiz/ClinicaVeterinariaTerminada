from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
from uiReservaCtRutinario import Ui_MainWindow
import ventanaReserva
import ventanaHorarios

class ventanaCRutinario(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.hora = []
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.horario = ventanaHorarios.ventanaHorarios(0, self.cont)
        self.ventanaUi.ButtonHorarios.clicked.connect(lambda : self.cambio(self.horario))
        self.actualizarComboBoxMascota()
        self.ventanaUi.labelHorario.setText("El horario escogido se mostrará aqui...")
        self.hora = []

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
    
    # def retroceder(self):
    #     self.ventanaReserva.show()
    #     self.close()
    
    def actualizarLabel(self):
        self.ventanaUi.labelHorario.setText("Horario Escogido:\nFecha: " + self.hora[0] +"\nHorario: " + self.hora[1] + "\nSala N° " + self.hora[2])
    
    def cambio(self, ventana):
        ventana.actualizarHorario()
        ventana.show()
        self.hide()