from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiMenuClinica import Ui_MainWindow
import ventanaReserva
import ventanaCRutinario
import ventanaQuirofano
import ventanaListaReserva

class ventanaMenuReserva(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.hora = []
        self.actualizarNombre()
        self.v = ventanaReserva.ventanaReserva()
        self.ventanaUi.botonAtras.clicked.connect(lambda: self.cambio(self.v))
        self.venCt = ventanaCRutinario.ventanaCRutinario(self.cont, self.hora)
        #self.venQ = ventanaQuirofano.ventanaQuirofano()
        self.venL = ventanaListaReserva.ventanaListaReserva(self.cont, False)
        self.ventanaUi.control_rutinario.clicked.connect(lambda: self.cambio(self.venCt))
        self.ventanaUi.Lista_reservas.clicked.connect(lambda: self.cambio(self.venL))

    def cambio(self, ventana):
        ventana.show()
        self.hide()

    def actualizarNombre(self):
        with open("clientes.csv") as r:
            reader = csv.reader(r)
            next(reader)
            i = 1
            for l in reader:
                if i == self.cont:
                    self.persona = l
                    break
                i += 1
        self.ventanaUi.label_2.setText("Bienvenido: " + self.persona[1])