import csv
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
from uiUrgencia import Ui_MainWindow
import os
from datetime import datetime
import ventanaReserva
import ventanaListaUrgencias


class ventanaUrgencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaAux = Ui_MainWindow()
        self.ventanaAux.setupUi(self)
        self.ventanaAux.Guardar_registro.clicked.connect(self.cargarDatos)
        self.ventanaAux.Ver_registro.clicked.connect(self.lista)
        self.ventanaAux.botonAtras.clicked.connect(self.atras)
        self.soloLetras = QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-ZáéíóúÁÉÍÓÚüÜ ]+"))
        self.soloInt = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+"))
        self.restricDirec = QtGui.QRegExpValidator(QtCore.QRegExp("[^,]+"))
        self.ventanaAux.Nombre_mascota.setValidator(self.soloLetras)
        self.ventanaAux.Dueno_edit.setValidator(self.soloLetras)
        self.ventanaAux.telefono_edit.setValidator(self.soloInt)
        self.ventanaAux.domicilio_edit.setValidator(self.restricDirec)
        self.ambulancia()
        self.ventanaAux.Gravedad_box.currentIndexChanged.connect(self.ambulancia)
      

    def cargarDatos(self):
        cuadrosTexto = [self.ventanaAux.Nombre_mascota, self.ventanaAux.Dueno_edit, self.ventanaAux.domicilio_edit]
        vacios = False
        for cuadro in cuadrosTexto:
            texto = cuadro.text()
            if texto == "" or texto.isspace():
                vacios = True
                break
        if(vacios):
            qtw.QMessageBox.warning(self, "ERROR", "Por favor complete los cuadros de texto antes de agregar.")
        else:
            nombre_mascota = self.ventanaAux.Nombre_mascota.text()
            dueno = self.ventanaAux.Dueno_edit.text()
            telefono = self.ventanaAux.telefono_edit.text()
            domicilio = self.ventanaAux.domicilio_edit.text()
            Gravedad = self.ventanaAux.Gravedad_box.currentText()

            archivo_existe = os.path.exists("ArchivosCSV/Urgencias.csv")

            fecha_actual = datetime.now().strftime("%d/%m/%Y")
            hora = datetime.now().strftime("%H:%M")

            with open("ArchivosCSV/Urgencias.csv", 'a', newline='') as file:
                writer = csv.writer(file)

                if not archivo_existe:
                    writer.writerow(["nombremasc", "dueno", "telefono", "domicilio", "gravedad", "fecha", "ambulancia", "hora"])
                if self.ventanaAux.AmbulanciacheckBox.isChecked():
                    ambulancia = "Si"
                else:
                    ambulancia = "No"
                writer.writerow([nombre_mascota, dueno, telefono, domicilio, Gravedad, fecha_actual, ambulancia, hora])
                msg = qtw.QMessageBox()
                msg.setWindowTitle("Guardar Registro")
                msg.setText("Registro guardado exitosamente.\nc:")
                msg.exec_()
                self.ventanaAux.domicilio_edit.clear()
                self.ventanaAux.Nombre_mascota.clear()
                self.ventanaAux.Dueno_edit.clear()
                self.ventanaAux.telefono_edit.clear()
                self.atras()
            
    def ambulancia(self):
        Gravedad = (self.ventanaAux.Gravedad_box.currentIndex() + 1)
        if Gravedad > 2:
            self.ventanaAux.AmbulanciacheckBox.setEnabled(True)
        else:
            self.ventanaAux.AmbulanciacheckBox.setChecked(False)
            self.ventanaAux.AmbulanciacheckBox.setEnabled(False)
    
    def atras(self):
        self.ventanaReserva = ventanaReserva.ventanaReserva()
        self.ventanaReserva.show()
        self.close()
    
    def lista(self):
        self.ventanaLista = ventanaListaUrgencias.ventanaListaUrgencias()
        self.ventanaLista.show()
        self.close()