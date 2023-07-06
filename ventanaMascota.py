from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
from uiVentDatosMasc import uiDatos
from Mascota import Mascota
from ManejoArchivo import GestionArchivo
import ventElecMasc
import ventanaLista


class ventanaMascota(QMainWindow):
    def __init__(self, rut, flag):
        super().__init__()
        self.rut = rut
        self.flag = flag
        self.ventanaUi = uiDatos()
        self.ventanaUi.setupUi(self)
        
        self.soloLetras = QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-ZáéíóúÁÉÍÓÚüÜ ]+"))
        self.ventanaUi.inputNombre.setValidator(self.soloLetras)
        self.ventanaUi.inputEspecie.setValidator(self.soloLetras)
        self.ventanaUi.inputRaza.setValidator(self.soloLetras)
        
        self.ventanaUi.btnAgregarMascota.clicked.connect(lambda: self.agregar(self.flag))
        self.ventanaUi.btnAtras.clicked.connect(lambda: self.atras(self.flag))
        
        
    def agregar(self, flagg):
        if self.ventanaUi.inputNombre.text() == "" or self.ventanaUi.inputEspecie.text() == "" or self.ventanaUi.inputRaza.text() == "" or self.ventanaUi.inputComboBoxSexo.currentIndex() < 1 or self.ventanaUi.inputComboBoxTamano.currentIndex() < 1 or self.ventanaUi.inputPeso.value() == 0 or self.ventanaUi.inputVolumen.value() == 0:
            qtw.QMessageBox.warning(self, "Hay campos sin rellenar", "Por favor, rellene sus datos correctamente.")
        else:
            nombre = self.ventanaUi.inputNombre.text()
            especie = self.ventanaUi.inputEspecie.text()
            raza = self.ventanaUi.inputRaza.text()
            fechaAux = self.ventanaUi.inputFechaNacimiento.date()
            fechaNacimiento = fechaAux.toString("dd/MM/yyyy")
            sexo = self.ventanaUi.inputComboBoxSexo.currentText()
            peso = self.ventanaUi.inputPeso.value()
            tamaño = self.ventanaUi.inputComboBoxTamano.currentText()
            volumen = self.ventanaUi.inputVolumen.value()
            self.mascota = Mascota(str(self.rut), str(nombre), str(especie), str(raza), str(fechaNacimiento), str(sexo), peso, str(tamaño), volumen)
            GestionArchivo.insertar("ArchivosCSV/mascotas.csv",self.mascota)
            self.atras(flagg)      
        
    def atras(self, fla):
        if fla == 0:
            vent = ventElecMasc.ventElec(self.rut)
            vent.show()
            self.hide()
        elif fla == 1:
            ventanaLista.ventanaLista().show()
            self.hide()