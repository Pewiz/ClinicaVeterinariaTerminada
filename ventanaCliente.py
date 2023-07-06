import csv
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
from uiVentCliente import uiVentCliente
from ClaseCliente import Cliente
from ManejoArchivo import GestionArchivo
import ventElecMasc
import VentAdminPrincipal


class ventanaCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ventanaUi = uiVentCliente()
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
        self.ventanaUi.btnAgMas.clicked.connect(lambda: self.agregar(self.ventan))
        
        self.ventanaUi.BtnAtras.clicked.connect(self.volver)
        
        
    def agregar(self, vent):
        if self.ventanaUi.lineEdit.text() == "" or self.ventanaUi.lineEdit_2.text() == "" or self.ventanaUi.lineEdit_3.text() == "" or self.ventanaUi.lineEdit_4.text() == "" or self.ventanaUi.lineEdit_5.text() == "" or self.ventanaUi.lineEdit_6.text() == "" or self.ventanaUi.lineEdit_7.text() == "" or self.ventanaUi.lineEdit_8.text() == "" or self.ventanaUi.comboBox.currentIndex() < 1:
            qtw.QMessageBox.warning(self, "Hay campos sin rellenar", "Por favor, rellene sus datos correctamente.")
        else:
            with open('ArchivosCSV/clientes.csv', 'r', encoding="utf-8") as r:
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
            fechaAux = self.ventanaUi.dateEdit.date()
            fechaNacimiento = fechaAux.toString("dd/MM/yyyy")
            email = self.ventanaUi.lineEdit_4.text()
            telefono = self.ventanaUi.lineEdit_7.text()
            domicilio = self.ventanaUi.lineEdit_8.text()
            self.cliente = Cliente(str(rut), str(nombres), str(apellidoPaterno), str(apellidoMaterno), str(genero), str(fechaNacimiento), str(email), str(telefono), str(domicilio))
            GestionArchivo.insertar("ArchivosCSV/clientes.csv",self.cliente)
            vent.show()
            self.close()        
        
    def volver(self):
        self.close()