from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiReserva import Ui_MainWindow
import ventanaCRutinario
import ventanaQuirofano

class ventanaReserva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.clientes = self.cargarClientes()
        self.ventanaCRutinario = ventanaCRutinario.ventanaCRutinario(0)
        self.ventanaQuirofano = ventanaQuirofano.ventanaQuirofano()
        self.ventanaUi.ButtonIngresar.clicked.connect(self.elegirPersona)

    def cargarClientes(self):
        with open('clientes.csv') as file:
            reader = csv.reader(file)
            next(reader)

            clientes = list(reader)

        return clientes

    def actualizarComboBox(self):
        self.ventanaUi.ComboBoxCliente.clear()
        self.ventanaUi.ComboBoxCliente.addItem("Elegir Cliente")

        for cliente in self.clientes:
            nombre_completo = f"{cliente[1]} {cliente[2]} {cliente[3]}"
            self.ventanaUi.ComboBoxCliente.addItem(nombre_completo)

    def elegirPersona(self):
        if self.ventanaUi.ComboBoxCliente.currentIndex() == 0:
            qtw.QMessageBox.warning(self, "ERROR", "Por favor elija un cliente antes de avanzar.\n>:c")
        else:
            persona = self.ventanaUi.ComboBoxCliente.currentIndex() - 1
            rut_cliente = self.clientes[persona][0]
            self.ventanaCRutinario.actualizarComboBoxMascota(rut_cliente)
            self.ventanaCRutinario.show()
            #self.ventanaQuirofano.show()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaReserva()
    ventanaP.actualizarComboBox()
    ventanaP.show()
    app.exec_()