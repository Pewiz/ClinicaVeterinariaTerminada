# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventIngresarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from Usuario import Usuario
from ManejoArchivo import GestionArchivo


class Ui_ventIngresarUsuario(object):
    def setupUi(self, ventIngresarUsuario):
        ventIngresarUsuario.setObjectName("ventIngresarUsuario")
        ventIngresarUsuario.resize(950, 680)
        ventIngresarUsuario.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        ventIngresarUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.apellidoPatLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.apellidoPatLnE.setGeometry(QtCore.QRect(190, 260, 181, 41))
        self.apellidoPatLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.apellidoPatLnE.setObjectName("apellidoPatLnE")
        self.nombresLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.nombresLnE.setGeometry(QtCore.QRect(190, 190, 181, 41))
        self.nombresLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.nombresLnE.setObjectName("nombresLnE")
        self.apellidoMatLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.apellidoMatLnE.setGeometry(QtCore.QRect(190, 330, 181, 41))
        self.apellidoMatLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.apellidoMatLnE.setObjectName("apellidoMatLnE")
        self.generoCombobox = QtWidgets.QComboBox(ventIngresarUsuario)
        self.generoCombobox.setGeometry(QtCore.QRect(190, 400, 181, 41))
        self.generoCombobox.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"color: rgb(0, 0, 0);")
        self.generoCombobox.setEditable(False)
        self.generoCombobox.setDuplicatesEnabled(False)
        self.generoCombobox.setObjectName("generoCombobox")
        self.generoCombobox.addItem("")
        self.generoCombobox.addItem("")
        self.generoCombobox.addItem("")
        self.btnIngresarUsuario = QtWidgets.QPushButton(ventIngresarUsuario)
        self.btnIngresarUsuario.setGeometry(QtCore.QRect(760, 590, 141, 41))
        self.btnIngresarUsuario.setAutoFillBackground(False)
        self.btnIngresarUsuario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")
        self.btnIngresarUsuario.setObjectName("btnIngresarUsuario")
        self.btnIngresarUsuario.clicked.connect(self.onActionBtnIngresar)
        self.fechaNacimientoDtEdit = QtWidgets.QDateEdit(ventIngresarUsuario)
        self.fechaNacimientoDtEdit.setGeometry(QtCore.QRect(190, 470, 181, 41))
        self.fechaNacimientoDtEdit.setObjectName("fechaNacimientoDtEdit")
        self.experienciaLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.experienciaLnE.setGeometry(QtCore.QRect(610, 330, 181, 41))
        self.experienciaLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.experienciaLnE.setObjectName("experienciaLnE")
        self.contraseaLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.contraseaLnE.setGeometry(QtCore.QRect(610, 400, 181, 41))
        self.contraseaLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.contraseaLnE.setObjectName("contraseaLnE")
        self.cargoComboBox = QtWidgets.QComboBox(ventIngresarUsuario)
        self.cargoComboBox.setGeometry(QtCore.QRect(610, 190, 181, 41))
        self.cargoComboBox.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.cargoComboBox.setEditable(False)
        self.cargoComboBox.setObjectName("cargoComboBox")
        self.cargoComboBox.addItem("")
        self.cargoComboBox.addItem("")
        self.cargoComboBox.addItem("")
        self.especialidadComboBox = QtWidgets.QComboBox(ventIngresarUsuario)
        self.especialidadComboBox.setGeometry(QtCore.QRect(610, 260, 181, 41))
        self.especialidadComboBox.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.especialidadComboBox.setEditable(False)
        self.especialidadComboBox.setObjectName("especialidadComboBox")
        self.especialidadComboBox.addItem("")
        self.especialidadComboBox.addItem("")
        self.especialidadComboBox.addItem("")
        self.especialidadComboBox.addItem("")
        self.especialidadComboBox.addItem("")
        self.especialidadComboBox.addItem("")
        self.rutLineE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.rutLineE.setGeometry(QtCore.QRect(610, 470, 111, 41))
        self.rutLineE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.rutLineE.setText("")
        self.rutLineE.setObjectName("rutLineE")
        self.rutLineE.setMaxLength(8)
        self.rutLineE.setValidator(QIntValidator())
        self.rutLineE.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.codigoVerificadorLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.codigoVerificadorLnE.setGeometry(QtCore.QRect(750, 470, 41, 41))
        self.codigoVerificadorLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.codigoVerificadorLnE.setText("")
        self.codigoVerificadorLnE.setObjectName("codigoVerificadorLnE")
        self.codigoVerificadorLnE.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9Kk]")))
        self.codigoVerificadorLnE.setMaxLength(1)
        self.label = QtWidgets.QLabel(ventIngresarUsuario)
        self.label.setGeometry(QtCore.QRect(730, 480, 20, 21))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label.setObjectName("label")
        self.bannerSuperior = QtWidgets.QLabel(ventIngresarUsuario)
        self.bannerSuperior.setEnabled(True)
        self.bannerSuperior.setGeometry(QtCore.QRect(0, 0, 950, 130))
        self.bannerSuperior.setText("")
        self.bannerSuperior.setPixmap(QtGui.QPixmap("imagenes/bannerClinica.png"))
        self.bannerSuperior.setStyleSheet("background-color: transparent;")
        self.bannerSuperior.setObjectName("bannerSuperior")
        self.btnRegresar = QtWidgets.QPushButton(ventIngresarUsuario)
        self.btnRegresar.setGeometry(QtCore.QRect(10, 50, 41, 31))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n"
"border: none;")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnRegresar.clicked.connect(ventIngresarUsuario.close)

        self.emailLnE = QtWidgets.QLineEdit(ventIngresarUsuario)
        self.emailLnE.setGeometry(QtCore.QRect(190, 540, 181, 41))
        self.emailLnE.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.emailLnE.setObjectName("emailLnE")

        self.retranslateUi(ventIngresarUsuario)
        self.generoCombobox.setCurrentIndex(0)
        self.cargoComboBox.setCurrentIndex(0)
        self.especialidadComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ventIngresarUsuario)


        
    def retranslateUi(self, ventIngresarUsuario):
        _translate = QtCore.QCoreApplication.translate
        ventIngresarUsuario.setWindowTitle(_translate("ventIngresarUsuario", "Clinica CVI"))
        self.apellidoPatLnE.setPlaceholderText(_translate("ventIngresarUsuario", "Ingresar Apellido paterno"))
        self.nombresLnE.setPlaceholderText(_translate("ventIngresarUsuario", "Ingresar Nombres"))
        self.apellidoMatLnE.setPlaceholderText(_translate("ventIngresarUsuario", "Ingresar Apellido materno"))
        self.generoCombobox.setCurrentText(_translate("ventIngresarUsuario", "Genero"))
        self.generoCombobox.setPlaceholderText(_translate("ventIngresarUsuario", "Genero"))
        self.generoCombobox.setItemText(0, _translate("ventIngresarUsuario", "Genero"))
        self.generoCombobox.setItemText(1, _translate("ventIngresarUsuario", "Masculino"))
        self.generoCombobox.setItemText(2, _translate("ventIngresarUsuario", "Femenino"))
        self.btnIngresarUsuario.setText(_translate("ventIngresarUsuario", "Ingresar Usuario"))
        self.experienciaLnE.setPlaceholderText(_translate("ventIngresarUsuario", "Experiencia"))
        self.contraseaLnE.setPlaceholderText(_translate("ventIngresarUsuario", "Contraseña"))
        self.cargoComboBox.setCurrentText(_translate("ventIngresarUsuario", "Cargo"))
        self.cargoComboBox.setPlaceholderText(_translate("ventIngresarUsuario", "Cargo"))
        self.cargoComboBox.setItemText(0, _translate("ventIngresarUsuario", "Cargo"))
        self.cargoComboBox.setItemText(1, _translate("ventIngresarUsuario", "Veterinario"))
        self.cargoComboBox.setItemText(2, _translate("ventIngresarUsuario", "Secretaria"))
        self.especialidadComboBox.setCurrentText(_translate("ventIngresarUsuario", "Especialidad"))
        self.especialidadComboBox.setPlaceholderText(_translate("ventIngresarUsuario", "Especialidad"))
        self.especialidadComboBox.setItemText(0, _translate("ventIngresarUsuario", "Especialidad"))
        self.especialidadComboBox.setItemText(1, _translate("ventIngresarUsuario", "Neurologia"))
        self.especialidadComboBox.setItemText(2, _translate("ventIngresarUsuario", "Reproduccion"))
        self.especialidadComboBox.setItemText(3, _translate("ventIngresarUsuario", "Odontologia"))
        self.especialidadComboBox.setItemText(4, _translate("ventIngresarUsuario", "Oncologia"))
        self.especialidadComboBox.setItemText(5, _translate("ventIngresarUsuario", "Cardiologia"))
        self.rutLineE.setPlaceholderText(_translate("ventIngresarUsuario", "Rut sin puntos"))
        self.codigoVerificadorLnE.setPlaceholderText(_translate("ventIngresarUsuario", "0-9|k"))
        self.label.setText(_translate("ventIngresarUsuario", "-"))
        self.emailLnE.setPlaceholderText(_translate("ventIngresarUsuario", "Ingresar Email"))

    def alertBox(self, Mensaje, Titulo):
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.exec_()

    def onActionBtnIngresar(self):
        nombres = self.nombresLnE.text()
        apellidoPa = self.apellidoPatLnE.text()
        apellidoMa = self.apellidoMatLnE.text()
        genero = self.generoCombobox.currentText()
        fecha_nacimiento = self.fechaNacimientoDtEdit.date().toString("dd/MM/yyyy")
        rut = self.rutLineE.text()
        digito_verificador = self.codigoVerificadorLnE.text()
        cargo = self.cargoComboBox.currentText()
        especialidad = self.especialidadComboBox.currentText()
        experiencia = self.experienciaLnE.text()
        email = self.emailLnE.text()
        contrasea = self.contraseaLnE.text()
        # Convertir la k minuscula en mayuscula
        if digito_verificador == "k":
            digito_verificador = digito_verificador.replace("k", "K")
        # Pasar el rut al formato "xx.xxx.xxx-x"
        if len(rut) > 0:
            rutFormatted = "{:,}".format(int(rut)).replace(",", ".")
            rut_con_digito_verificador = rutFormatted + "-" + digito_verificador
        else:
            rut_con_digito_verificador = ""
        if "@" not in email:
            self.alertBox("Falta ingresar el '@' en el email", "Falta un dato")
        elif "." not in email:
            self.alertBox("Falta ingresar el '.' en el email", "Falta un dato")
        # El .strip es para verificar que tenga datos
        elif nombres.strip() == "":
            self.alertBox("Falta ingresar el nombre", "Falta un dato")
        elif apellidoPa.strip() == "":
            self.alertBox("Falta ingresar el apellido", "Falta un dato")
        elif len(self.rutLineE.text()) != 8:
            self.alertBox("Faltan numeros en el rut", "Falta un dato")
        elif len(self.codigoVerificadorLnE.text()) != 1:
            self.alertBox("Falta ingresar el digito verificador", "Falta un dato")
        elif experiencia.strip() == "":
            self.alertBox("Falta ingresar la experiencia", "Falta un dato")
        elif email.strip() == "":
            self.alertBox("Falta ingresar el email", "Falta un dato")
        elif contrasea.strip() == "":
            self.alertBox("Falta ingresar la contraseña", "Falta un dato")
        else:
            if cargo == "Veterinario":
                cargo = especialidad
            trabajador = Usuario(rut=rut_con_digito_verificador,nombres=nombres, apellido_paterno=apellidoPa, apellido_materno=apellidoMa, genero=genero, fecha_nacimiento=fecha_nacimiento, cargo=cargo, experiencia=experiencia,email=email,contrasea=contrasea,horario=None)
            GestionArchivo.insertar("veterinarios.csv",trabajador)
            self.alertBox("El usuario: "+nombres+" "+apellidoPa+" "+apellidoMa+" ha sido ingresado", "Se ha ingresado el cliente")
            
            # Limpiar LineEdit
            self.nombresLnE.setText("")
            self.apellidoPatLnE.setText("")
            self.apellidoMatLnE.setText("")
            self.fechaNacimientoDtEdit.setDate(QtCore.QDate.fromString("01/01/2000", "dd/MM/yyyy"))
            self.rutLineE.setText("")
            self.codigoVerificadorLnE.setText("")
            self.emailLnE.setText("")
            self.contraseaLnE.setText("")
            self.experienciaLnE.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_ventIngresarUsuario()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
