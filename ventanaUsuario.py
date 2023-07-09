import csv
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
from uiVentUsuario import uiVentUsuario
from ClaseUsuario import Usuario
from ManejoArchivo import GestionArchivo
import ventElecMasc


class ventanaUsuario(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ventanaUi = uiVentUsuario()
        self.ventanaUi.setupUi(self)
        
        self.soloInt = QtGui.QIntValidator()
        self.ventanaUi.lineEdit_3.setValidator(self.soloInt)
        self.ventanaUi.lineEdit_7.setValidator(self.soloInt)
        self.digVerificador = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9Kk]"), self)
        self.ventanaUi.lineEdit_6.setValidator(self.digVerificador)
        self.soloLetras = QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-ZáéíóúÁÉÍÓÚüÜ ]+"))
        self.ventanaUi.lineEdit.setValidator(self.soloLetras)
        self.ventanaUi.lineEdit_2.setValidator(self.soloLetras)
        self.ventanaUi.lineEdit_5.setValidator(self.soloLetras)
        
        self.rt = None
        self.ventan = ventElecMasc.ventElec(self.rt)
        self.ventanaUi.btnAgMas.clicked.connect(lambda: self.agregar())
        
        self.ventanaUi.BtnAtras.clicked.connect(self.volver)
        
        
    def agregar(self):
        if self.ventanaUi.lineEdit.text() == "" or self.ventanaUi.lineEdit_2.text() == "" or len(self.ventanaUi.lineEdit_3.text()) < 7 or '@' not in self.ventanaUi.lineEdit_4.text() or '.' not in self.ventanaUi.lineEdit_4.text() or self.ventanaUi.lineEdit_5.text() == "" or self.ventanaUi.lineEdit_password.text() == "" or self.ventanaUi.lineEdit_6.text() == "" or len(self.ventanaUi.lineEdit_7.text()) != 9 or self.ventanaUi.lineEdit_8.text() == "" or self.ventanaUi.comboBox.currentIndex() < 1 or self.ventanaUi.comboBoxCargo.currentIndex()  < 1:
            qtw.QMessageBox.warning(self, "Hay campos sin rellenar", "Por favor, rellene sus datos correctamente.")
        else:
            with open('ArchivosCSV/usuarios.csv', 'r', encoding="latin-1") as r:
                l = csv.reader(r, delimiter=",")
                next(l)
                for lis in l:
                    if lis[0] == (self.ventanaUi.lineEdit_3.text() + "-" + self.ventanaUi.lineEdit_6.text()):
                        qtw.QMessageBox.warning(self, "ERROR", "El rut ingresado ya existe.\nPorfavor, ingrese un rut nuevo, o en su defecto, ingrese un rut valido.")
                        return
            rut = (self.ventanaUi.lineEdit_3.text() + "-" + self.ventanaUi.lineEdit_6.text())
            self.ventan.rut = (self.ventanaUi.lineEdit_3.text() + "-" + self.ventanaUi.lineEdit_6.text())
            nombres = self.ventanaUi.lineEdit.text()
            apellidoPaterno = self.ventanaUi.lineEdit_2.text()
            apellidoMaterno = self.ventanaUi.lineEdit_5.text()
            genero = self.ventanaUi.comboBox.currentText()
            password = self.ventanaUi.lineEdit_password.text()
            cargo = self.ventanaUi.comboBoxCargo.currentText()
            experiencia = self.ventanaUi.spinBox.text() + " meses"
            fechaAux = self.ventanaUi.dateEdit.date()
            fechaNacimiento = fechaAux.toString("dd/MM/yyyy")
            email = self.ventanaUi.lineEdit_4.text()
            telefono = self.ventanaUi.lineEdit_7.text()
            domicilio = self.ventanaUi.lineEdit_8.text()
            self.usuario = Usuario(str(rut), str(nombres), str(apellidoPaterno), str(apellidoMaterno), str(genero), str(fechaNacimiento), str(email), str(telefono), str(domicilio), str(cargo), str(experiencia), str(password))
            GestionArchivo.insertar("ArchivosCSV/usuarios.csv",self.usuario)
            self.volver()  
        
    def volver(self):
        self.close()