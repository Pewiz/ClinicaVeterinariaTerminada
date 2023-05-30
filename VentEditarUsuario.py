# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventEditarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ManejoArchivo import GestionArchivo
from PyQt5.QtWidgets import QMessageBox
from VentAsignarHoraVet import Ui_VentAsignarHorario

class Ui_VentVerDatosUser(object):
    def __init__(self,usuario,fila,nombreVent):
        self._usuario = usuario
        self._fila = fila
        self.nombreVent = nombreVent

    def setupUi(self, VentVerDatosUser):
        VentVerDatosUser.setObjectName("VentVerDatosUser")
        VentVerDatosUser.resize(950, 680)
        VentVerDatosUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(VentVerDatosUser)
        self.label.setGeometry(QtCore.QRect(0, 0, 950, 130))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes/bannerClinica.png"))
        self.label.setObjectName("label")
        self.btnRegresar = QtWidgets.QPushButton(VentVerDatosUser)
        self.btnRegresar.setGeometry(QtCore.QRect(10, 50, 41, 31))
        self.btnRegresar.setStyleSheet("background-color: transparent;")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnRegresar.clicked.connect(VentVerDatosUser.close)
        self.nombresLnEdit = QtWidgets.QLineEdit(VentVerDatosUser)
        self.nombresLnEdit.setEnabled(False)
        self.nombresLnEdit.setGeometry(QtCore.QRect(230, 280, 211, 22))
        self.nombresLnEdit.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.nombresLnEdit.setObjectName("nombresLnEdit")
        self.nombresLnEdit.setText(str(self._usuario.nombres))
        self.label_2 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 151, 31))
        self.label_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.apellidoPaLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.apellidoPaLnE.setEnabled(False)
        self.apellidoPaLnE.setGeometry(QtCore.QRect(230, 340, 211, 22))
        self.apellidoPaLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.apellidoPaLnE.setText("")
        self.apellidoPaLnE.setObjectName("apellidoPaLnE")
        self.apellidoPaLnE.setText(self._usuario.apellidoPa)
        self.label_3 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 201, 31))
        self.label_3.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.apellidoMaLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.apellidoMaLnE.setEnabled(False)
        self.apellidoMaLnE.setGeometry(QtCore.QRect(230, 400, 211, 22))
        self.apellidoMaLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.apellidoMaLnE.setText("")
        self.apellidoMaLnE.setObjectName("apellidoMaLnE")
        self.apellidoMaLnE.setText(self._usuario.apellidoMa)
        self.label_4 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_4.setGeometry(QtCore.QRect(30, 390, 201, 31))
        self.label_4.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_4.setObjectName("label_4")
        self.rutLnEdit = QtWidgets.QLineEdit(VentVerDatosUser)
        self.rutLnEdit.setEnabled(False)
        self.rutLnEdit.setGeometry(QtCore.QRect(230, 220, 211, 22))
        self.rutLnEdit.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.rutLnEdit.setText("")
        self.rutLnEdit.setObjectName("rutLnEdit")
        self.rutLnEdit.setText(self._usuario.rut)
        self.label_5 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 201, 31))
        self.label_5.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_5.setObjectName("label_5")
        self.generoLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.generoLnE.setEnabled(False)
        self.generoLnE.setGeometry(QtCore.QRect(230, 460, 211, 22))
        self.generoLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.generoLnE.setText("")
        self.generoLnE.setObjectName("generoLnE")
        self.generoLnE.setText(self._usuario.genero)
        self.label_6 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 201, 31))
        self.label_6.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_7.setGeometry(QtCore.QRect(470, 210, 211, 31))
        self.label_7.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_7.setObjectName("label_7")
        self.fechaNacLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.fechaNacLnE.setEnabled(False)
        self.fechaNacLnE.setGeometry(QtCore.QRect(690, 220, 211, 22))
        self.fechaNacLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.fechaNacLnE.setText(self._usuario.fecha_nacimiento)
        self.fechaNacLnE.setObjectName("fechaNacLnE")
        self.label_8 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_8.setGeometry(QtCore.QRect(470, 270, 211, 31))
        self.label_8.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_8.setObjectName("label_8")
        self.cargoLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.cargoLnE.setEnabled(False)
        self.cargoLnE.setGeometry(QtCore.QRect(690, 280, 211, 22))
        self.cargoLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.cargoLnE.setText(self._usuario.cargo)
        self.cargoLnE.setObjectName("cargoLnE")
        self.label_9 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_9.setGeometry(QtCore.QRect(470, 330, 211, 31))
        self.label_9.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_9.setObjectName("label_9")
        self.experienciaLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.experienciaLnE.setEnabled(False)
        self.experienciaLnE.setGeometry(QtCore.QRect(690, 340, 211, 22))
        self.experienciaLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.experienciaLnE.setText(self._usuario.experiencia)
        self.experienciaLnE.setObjectName("experienciaLnE")
        self.label_10 = QtWidgets.QLabel(VentVerDatosUser)
        self.label_10.setGeometry(QtCore.QRect(470, 390, 211, 31))
        self.label_10.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_10.setObjectName("label_10")
        self.emailLnE = QtWidgets.QLineEdit(VentVerDatosUser)
        self.emailLnE.setEnabled(False)
        self.emailLnE.setGeometry(QtCore.QRect(690, 400, 211, 22))
        self.emailLnE.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.emailLnE.setText(self._usuario.email)
        self.emailLnE.setObjectName("emailLnE")
        self.btnGuardarCambios = QtWidgets.QPushButton(VentVerDatosUser)
        self.btnGuardarCambios.setGeometry(QtCore.QRect(790, 580, 111, 51))
        self.btnGuardarCambios.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.btnGuardarCambios.clicked.connect(self.onActionGuardarCambios)
        self.btnGuardarCambios.clicked.connect(VentVerDatosUser.close)
        self.btnEditarDatos = QtWidgets.QPushButton(VentVerDatosUser)
        self.btnEditarDatos.setGeometry(QtCore.QRect(630, 580, 111, 51))
        self.btnEditarDatos.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")
        self.btnEditarDatos.setObjectName("btnEditarDatos")
        self.btnEditarDatos.clicked.connect(self.onActionEditarDatos)
        self.btnAsignarHorario = QtWidgets.QPushButton(VentVerDatosUser)
        self.btnAsignarHorario.setGeometry(QtCore.QRect(470, 580, 111, 51))
        self.btnAsignarHorario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")
        self.btnAsignarHorario.setObjectName("btnAsignarHorario")
        self.btnAsignarHorario.clicked.connect(lambda: self.cambiarVent(Ui_VentAsignarHorario,self._usuario,))

        self.retranslateUi(VentVerDatosUser)
        QtCore.QMetaObject.connectSlotsByName(VentVerDatosUser)

    def retranslateUi(self, VentVerDatosUser):
        _translate = QtCore.QCoreApplication.translate
        VentVerDatosUser.setWindowTitle(_translate("VentVerDatosUser", "Dialog"))
        self.label_2.setText(_translate("VentVerDatosUser", "Nombres: "))
        self.label_3.setText(_translate("VentVerDatosUser", "Apellido Paterno:"))
        self.label_4.setText(_translate("VentVerDatosUser", "Apellido Materno:"))
        self.label_5.setText(_translate("VentVerDatosUser", "Rut:"))
        self.label_6.setText(_translate("VentVerDatosUser", "Genero:"))
        self.label_7.setText(_translate("VentVerDatosUser", "Fecha Nacimiento:"))
        self.label_8.setText(_translate("VentVerDatosUser", "Cargo:"))
        self.label_9.setText(_translate("VentVerDatosUser", "Experiencia:"))
        self.label_10.setText(_translate("VentVerDatosUser", "Email:"))
        self.btnGuardarCambios.setText(_translate("VentVerDatosUser", "Guardar Cambios"))
        self.btnEditarDatos.setText(_translate("VentVerDatosUser", "Editar Datos"))
        self.btnAsignarHorario.setText(_translate("VentVerDatosUser", "Asignar Horario"))
    
    def onActionEditarDatos(self):
        self.nombresLnEdit.setEnabled(True)
        self.apellidoPaLnE.setEnabled(True)
        self.apellidoMaLnE.setEnabled(True)
        self.generoLnE.setEnabled(True)
        self.cargoLnE.setEnabled(True)
        self.experienciaLnE.setEnabled(True)
        self.emailLnE.setEnabled(True)

    def alertBox(self, Mensaje, Titulo):
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.exec_()

    def cambiarVent(self,nombre_Vent,usuario):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent(usuario)
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()

    def cambiarVentNormal(self,nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()

    def onActionGuardarCambios(self):
        self._usuario.nombres = self.nombresLnEdit.text()
        self._usuario.apellidoPa = self.apellidoPaLnE.text()
        self._usuario.apellidoMa = self.apellidoMaLnE.text()
        self._usuario.genero = self.generoLnE.text()
        self._usuario.cargo = self.cargoLnE.text()
        self._usuario.experiencia = self.experienciaLnE.text()
        self._usuario.email = self.emailLnE.text()

        if "@" not in self._usuario.email:
            self.alertBox("Falta ingresar el '@' en el email", "Falta un dato")
        elif "." not in self._usuario.email:
            self.alertBox("Falta ingresar el '.' en el email", "Falta un dato")
        elif self._usuario.nombres.strip() == "":
            self.alertBox("Falta ingresar el nombre", "Falta un dato")
        elif self._usuario.apellidoPa.strip() == "":
            self.alertBox("Falta ingresar el apellido paterno", "Falta un dato")
        elif self._usuario.apellidoMa.strip() == "":
            self.alertBox("Falta ingresar el apellido materno", "Falta un dato")
        elif self._usuario.email.strip() == "":
            self.alertBox("Falta ingresar el email", "Falta un dato")
        elif self._usuario.genero.strip() == "":
            self.alertBox("Falta ingresar el genero", "Falta un dato")
        elif self._usuario.cargo.strip() == "":
            self.alertBox("Falta ingresar el cargo", "Falta un dato")
        elif self._usuario.experiencia.strip() == "":
            self.alertBox("Falta ingresar la experiencia", "Falta un dato")        
        else:
            GestionArchivo.modificar("veterinarios.csv",self._fila,self._usuario)
            self.nombresLnEdit.setEnabled(False)
            self.apellidoPaLnE.setEnabled(False)
            self.apellidoMaLnE.setEnabled(False)
            self.generoLnE.setEnabled(False)
            self.cargoLnE.setEnabled(False)
            self.experienciaLnE.setEnabled(False)
            self.emailLnE.setEnabled(False)
            self.alertBox("Cambios guardados correctamente","Guardado de Cambios")
            self.cambiarVentNormal(self.nombreVent)
        


