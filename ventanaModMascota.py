from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
from uiVentModMasc import uiMod
from Mascota import Mascota
from ManejoArchivo import GestionArchivo
import ventListaMasc


class ventanaModifMascota(QMainWindow):
    def __init__(self, posicion, flag, rut):
        super().__init__()
        self.posicion = posicion
        self.flag = flag
        self.rut = rut
        self.ventanaUi = uiMod()
        self.ventanaUi.setupUi(self)
        
        self.soloLetras = QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-ZáéíóúÁÉÍÓÚüÜ ]+"))
        self.ventanaUi.inputNombre.setValidator(self.soloLetras)
        self.ventanaUi.inputEspecie.setValidator(self.soloLetras)
        self.ventanaUi.inputRaza.setValidator(self.soloLetras)
        
        self.ventanaUi.btnModificar.clicked.connect(lambda: self.agregar(self.flag))
        self.ventanaUi.btnCancelar.clicked.connect(lambda: self.atras(self.flag))
        
        
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
            GestionArchivo.modificar("ArchivosCSV/mascotas.csv", self.posicion, self.mascota)
            self.atras(flagg)      
        
    def atras(self, fla):
        vent = ventListaMasc.ventListaMascota(self.rut, fla)
        vent.actualizar()
        vent.show()
        self.close()