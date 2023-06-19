import csv
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from uiUrgencia import Ui_MainWindow
import os
import PyQt5.QtWidgets as qtw
from datetime import datetime
import ventanaReserva
import ventanaRegistroUrgencia


class ventanaUrgencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaAux = Ui_MainWindow()
        self.ventanaAux.setupUi(self)
        self.ventanaAux.Gravedad_box.currentIndexChanged.connect(self.ambulancia)
        self.ventanaAux.Guardar_registro.clicked.connect(self.cargarDatos)
        self.ventanaAux.botonAtras.clicked.connect(self.atras)
        self.ventanaAux.Ver_registro.clicked.connect(self.cargarRegistro)
      

    def cargarDatos(self):
        nombre_mascota = self.ventanaAux.Nombre_mascota.text()
        dueno = self.ventanaAux.Dueno_edit.text()
        telefono = self.ventanaAux.telefono_edit.text()
        domicilio = self.ventanaAux.domicilio_edit.text()
        Gravedad = self.ventanaAux.Gravedad_box.currentText()
        if self.ventanaAux.AmbulanciacheckBox.isChecked():
            ambulancia = 'Si'
        else:
            ambulancia = 'No'

        archivo_existe = os.path.exists("Urgencias.csv")

        fecha_actual = datetime.now().strftime("%d/%m/%Y")  

        with open("Urgencias.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            
        if nombre_mascota.strip() == '' or dueno.strip() == '' or telefono.strip() == '' or domicilio.strip() == '':
            qtw.QMessageBox.warning(self, "Error", "No se permiten valores vacíos")
        else:
            if not archivo_existe:
                writer.writerow(["nombre", "dueno", "telefono", "domicilio", "Gravedad", "Fecha", "Ambulancia"])

                writer.writerow([nombre_mascota, dueno, telefono, domicilio, Gravedad, fecha_actual, ambulancia])
                qtw.QMessageBox.information(self, "Guardar Registro", "Registro Guardado Exitosamente")
                self.ventanaAux.domicilio_edit.clear()
                self.ventanaAux.Nombre_mascota.clear()
                self.ventanaAux.Dueno_edit.clear()
                self.ventanaAux.telefono_edit.clear()
            
    def ambulancia(self, indice):
        if indice >= 2:
            self.ventanaAux.AmbulanciacheckBox.setEnabled(True)
        else:
            self.ventanaAux.AmbulanciacheckBox.setEnabled(False)
    
    def cargarRegistro(self):
        archivo_existe = os.path.exists("Urgencias.csv")
        if archivo_existe:
            self.ventanaRegistro = ventanaRegistroUrgencia.ventanaRegistroUrgencia()
            self.ventanaRegistro.show()
            self.hide()
        else:
            qtw.QMessageBox.warning(self, "Error", "No existen registros")
    
    def atras(self):
        self.ventanaReserva = ventanaReserva.ventanaReserva()
        self.ventanaReserva.show()
        self.hide()