import csv
from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QMainWindow
from uiVentModificarUsuario import uiVentModificarUsuario
from ManejoArchivo import GestionArchivo
from ClaseUsuario import Usuario
import ventanaListaUsuario


class ventanaModificarUsuario(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = uiVentModificarUsuario()
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
        
        self.ventanaUi.BtnAtras.clicked.connect(lambda: self.cancelar())
        self.ventanaUi.btnAgMas.clicked.connect(lambda: self.modificar())
        
        
    
    def cancelar(self):
        ventanaListaUsuario.ventanaLista().show()
        self.close()
        
    def modificar(self):
        if self.ventanaUi.lineEdit.text() == "" or self.ventanaUi.lineEdit_2.text() == "" or self.ventanaUi.lineEdit_3.text() == "" or self.ventanaUi.lineEdit_4.text() == "" or self.ventanaUi.lineEdit_5.text() == "" or self.ventanaUi.lineEdit_password.text() == "" or self.ventanaUi.lineEdit_6.text() == "" or self.ventanaUi.lineEdit_7.text() == "" or self.ventanaUi.lineEdit_8.text() == "" or self.ventanaUi.comboBox.currentIndex() < 1 or self.ventanaUi.comboBoxCargo.currentIndex()  < 1:
            qtw.QMessageBox.warning(self, "Hay campos sin rellenar", "Por favor, rellene sus datos correctamente.")
        else:
            with open('usuarios.csv', 'r', encoding="latin-1") as r:
                l = csv.reader(r, delimiter=",")
                next(l)
                i = 0
                for lis in l:
                    i = (i + 1)
                    if i == (self.cont+1):
                        if lis[0] != (self.ventanaUi.lineEdit_3.text() + "-" + self.ventanaUi.lineEdit_6.text()):
                            qtw.QMessageBox.warning(self, "ERROR", "El rut ingresado tiene que ser el mismo.\nPorfavor, ingrese el rut correcto, o si el rut esta mal escrito, vuelva atrás e ingrese el cliente nuevamente.")
                            return
            rut = (self.ventanaUi.lineEdit_3.text() + "-" + self.ventanaUi.lineEdit_6.text())
            nombres = self.ventanaUi.lineEdit.text()
            apellidoPaterno = self.ventanaUi.lineEdit_2.text()
            apellidoMaterno = self.ventanaUi.lineEdit_5.text()
            genero = self.ventanaUi.comboBox.currentText()
            fechaAux = self.ventanaUi.dateEdit.date()
            fechaNacimiento = fechaAux.toString("dd/MM/yyyy")
            password = self.ventanaUi.lineEdit_password.text()
            cargo = self.ventanaUi.comboBoxCargo.currentText()
            experiencia = self.ventanaUi.spinBox.text() + " meses"
            email = self.ventanaUi.lineEdit_4.text()
            telefono = self.ventanaUi.lineEdit_7.text()
            domicilio = self.ventanaUi.lineEdit_8.text()
            self.cliente = Usuario(str(rut), str(nombres), str(apellidoPaterno), str(apellidoMaterno), str(genero), str(fechaNacimiento), str(email), str(telefono), str(domicilio), str(cargo), str(experiencia), str(password))
            GestionArchivo.modificar("usuarios.csv",self.cont + 1, self.cliente)
            ventanaListaUsuario.ventanaLista().show()
            self.close()