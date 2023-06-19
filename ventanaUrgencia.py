import csv
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from uiUrgencia import Ui_MainWindow
import os
import PyQt5.QtWidgets as qtw
from datetime import datetime
import ventanaReserva


class ventanaUrgencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaAux = Ui_MainWindow()
        self.ventanaAux.setupUi(self)
        self.ventanaAux.Guardar_registro.clicked.connect(self.cargarDatos)
        self.ventanaAux.botonAtras.clicked.connect(self.atras)
      

    def cargarDatos(self):
        nombre_mascota = self.ventanaAux.Nombre_mascota.text()
        dueno = self.ventanaAux.Dueno_edit.text()
        telefono = self.ventanaAux.telefono_edit.text()
        domicilio = self.ventanaAux.domicilio_edit.text()
        Gravedad = self.ventanaAux.Gravedad_box.currentText()

        archivo_existe = os.path.exists("Urgencias.csv")

        fecha_actual = datetime.now().strftime("%d/%m/%Y")  

        with open("Urgencias.csv", 'a', newline='') as file:
            writer = csv.writer(file)

            if not archivo_existe:
                writer.writerow(["nombre", "dueno", "telefono", "domicilio", "Gravedad", "Fecha"])

            writer.writerow([nombre_mascota, dueno, telefono, domicilio, Gravedad, fecha_actual])
            qtw.QMessageBox.warning(self, "Guardar Registro", "Registro Guardado Exitosamente")
            self.ventanaAux.domicilio_edit.clear()
            self.ventanaAux.Nombre_mascota.clear()
            self.ventanaAux.Dueno_edit.clear()
            self.ventanaAux.telefono_edit.clear()
            
    def ambulancia(self):
        Gravedad = self.ventanaAux.Gravedad_box
        if Gravedad >= 3:
            self.ventanaAux.AmbulanciacheckBox.setEnabled(True)
        else:
            self.ventanaAux.AmbulanciacheckBox.setEnabled(False)
    
    def atras(self):
        self.ventanaReserva = ventanaReserva.ventanaReserva()
        self.ventanaReserva.show()
        self.hide()