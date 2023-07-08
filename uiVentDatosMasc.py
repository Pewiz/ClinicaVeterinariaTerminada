# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaDatosMascotas.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class uiDatos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 540)
        MainWindow.setMinimumSize(QtCore.QSize(709, 540))
        MainWindow.setMaximumSize(QtCore.QSize(709, 540))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 711, 511))
        self.frame.setMinimumSize(QtCore.QSize(711, 511))
        self.frame.setMaximumSize(QtCore.QSize(711, 511))
        self.frame.setSizeIncrement(QtCore.QSize(10000, 10000))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.subMenu = QtWidgets.QLabel(self.frame)
        self.subMenu.setGeometry(QtCore.QRect(10, 90, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.subMenu.setFont(font)
        self.subMenu.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                   "border-radius: 15px;\n"
                                   "")
        self.subMenu.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.subMenu.setObjectName("subMenu")
        self.Titulo = QtWidgets.QLabel(self.frame)
        self.Titulo.setGeometry(QtCore.QRect(0, 0, 711, 80))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.FondoPerrito = QtWidgets.QLabel(self.frame)
        self.FondoPerrito.setGeometry(QtCore.QRect(390, 120, 321, 311))
        self.FondoPerrito.setText("")
        self.FondoPerrito.setPixmap(QtGui.QPixmap(
            "imagenes\Logo-removebg-preview.png"))
        self.FondoPerrito.setScaledContents(True)
        self.FondoPerrito.setObjectName("FondoPerrito")
        self.labelNombre = QtWidgets.QLabel(self.frame)
        self.labelNombre.setGeometry(QtCore.QRect(65, 141, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelNombre.setFont(font)
        self.labelNombre.setStyleSheet("")
        self.labelNombre.setObjectName("labelNombre")
        self.labelEspecie = QtWidgets.QLabel(self.frame)
        self.labelEspecie.setGeometry(QtCore.QRect(254, 141, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelEspecie.setFont(font)
        self.labelEspecie.setStyleSheet("")
        self.labelEspecie.setObjectName("labelEspecie")
        self.labelRaza = QtWidgets.QLabel(self.frame)
        self.labelRaza.setGeometry(QtCore.QRect(72, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelRaza.setFont(font)
        self.labelRaza.setStyleSheet("")
        self.labelRaza.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRaza.setObjectName("labelRaza")
        self.labelSexo = QtWidgets.QLabel(self.frame)
        self.labelSexo.setGeometry(QtCore.QRect(261, 210, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelSexo.setFont(font)
        self.labelSexo.setStyleSheet("")
        self.labelSexo.setObjectName("labelSexo")
        self.inputComboBoxSexo = QtWidgets.QComboBox(self.frame)
        self.inputComboBoxSexo.setGeometry(QtCore.QRect(252, 242, 69, 22))
        self.inputComboBoxSexo.setObjectName("inputComboBoxSexo")
        self.inputComboBoxSexo.addItem("")
        self.inputComboBoxSexo.addItem("")
        self.inputComboBoxSexo.addItem("")
        self.labelFechaNacimiento = QtWidgets.QLabel(self.frame)
        self.labelFechaNacimiento.setGeometry(QtCore.QRect(10, 280, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelFechaNacimiento.setFont(font)
        self.labelFechaNacimiento.setStyleSheet("")
        self.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
        self.inputFechaNacimiento = QtWidgets.QDateEdit(self.frame)
        self.inputFechaNacimiento.setGeometry(QtCore.QRect(40, 310, 131, 31))
        self.inputFechaNacimiento.setObjectName("inputFechaNacimiento")
        self.labelPeso = QtWidgets.QLabel(self.frame)
        self.labelPeso.setGeometry(QtCore.QRect(232, 280, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelPeso.setFont(font)
        self.labelPeso.setStyleSheet("")
        self.labelPeso.setObjectName("labelPeso")
        self.inputPeso = QtWidgets.QSpinBox(self.frame)
        self.inputPeso.setGeometry(QtCore.QRect(283, 292, 42, 22))
        self.inputPeso.setObjectName("inputPeso")
        self.labelSize = QtWidgets.QLabel(self.frame)
        self.labelSize.setGeometry(QtCore.QRect(50, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelSize.setFont(font)
        self.labelSize.setStyleSheet("")
        self.labelSize.setObjectName("labelSize")
        self.btnAtras = QtWidgets.QPushButton(self.frame)
        self.btnAtras.setGeometry(QtCore.QRect(10, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAtras.setFont(font)
        self.btnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAtras.setStyleSheet("border-radius: 13px;\n"
                                    "background-color: rgb(79, 163, 166);")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAgregarMascota = QtWidgets.QPushButton(self.frame)
        self.btnAgregarMascota.setGeometry(QtCore.QRect(520, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregarMascota.setFont(font)
        self.btnAgregarMascota.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgregarMascota.setStyleSheet("border-radius: 13px;\n"
                                             "background-color: rgb(79, 163, 166);")
        self.btnAgregarMascota.setObjectName("btnAgregarMascota")
        self.inputNombre = QtWidgets.QLineEdit(self.frame)
        self.inputNombre.setGeometry(QtCore.QRect(20, 177, 171, 31))
        self.inputNombre.setStyleSheet("border-color: rgb(30, 146, 148);")
        self.inputNombre.setObjectName("inputNombre")
        self.inputEspecie = QtWidgets.QLineEdit(self.frame)
        self.inputEspecie.setGeometry(QtCore.QRect(210, 178, 171, 31))
        self.inputEspecie.setStyleSheet("border-color: rgb(30, 146, 148);")
        self.inputEspecie.setObjectName("inputEspecie")
        self.inputRaza = QtWidgets.QLineEdit(self.frame)
        self.inputRaza.setGeometry(QtCore.QRect(20, 240, 171, 31))
        self.inputRaza.setStyleSheet("border-color: rgb(30, 146, 148);")
        self.inputRaza.setObjectName("inputRaza")
        self.inputComboBoxTamano = QtWidgets.QComboBox(self.frame)
        self.inputComboBoxTamano.setGeometry(QtCore.QRect(50, 390, 69, 22))
        self.inputComboBoxTamano.setObjectName("inputComboBoxTamano")
        self.inputComboBoxTamano.addItem("")
        self.inputComboBoxTamano.addItem("")
        self.inputComboBoxTamano.addItem("")
        self.inputComboBoxTamano.addItem("")
        self.inputComboBoxTamano.addItem("")
        self.inputComboBoxTamano.addItem("")
        self.labelVolumen = QtWidgets.QLabel(self.frame)
        self.labelVolumen.setGeometry(QtCore.QRect(200, 340, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelVolumen.setFont(font)
        self.labelVolumen.setStyleSheet("")
        self.labelVolumen.setObjectName("labelVolumen")
        self.inputVolumen = QtWidgets.QSpinBox(self.frame)
        self.inputVolumen.setGeometry(QtCore.QRect(294, 352, 41, 21))
        self.inputVolumen.setObjectName("inputVolumen")
        self.labelKg = QtWidgets.QLabel(self.frame)
        self.labelKg.setGeometry(QtCore.QRect(332, 281, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelKg.setFont(font)
        self.labelKg.setStyleSheet("")
        self.labelKg.setObjectName("labelKg")
        self.FondoPerrito.raise_()
        self.subMenu.raise_()
        self.Titulo.raise_()
        self.labelNombre.raise_()
        self.labelEspecie.raise_()
        self.labelRaza.raise_()
        self.labelSexo.raise_()
        self.inputComboBoxSexo.raise_()
        self.labelFechaNacimiento.raise_()
        self.inputFechaNacimiento.raise_()
        self.labelPeso.raise_()
        self.inputPeso.raise_()
        self.labelSize.raise_()
        self.btnAtras.raise_()
        self.btnAgregarMascota.raise_()
        self.inputNombre.raise_()
        self.inputEspecie.raise_()
        self.inputRaza.raise_()
        self.inputComboBoxTamano.raise_()
        self.labelVolumen.raise_()
        self.inputVolumen.raise_()
        self.labelKg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subMenu.setText(_translate("MainWindow", "                     Datos de la mascota"))
        self.Titulo.setText(_translate("MainWindow", "Datos mascotas"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre"))
        self.labelEspecie.setText(_translate("MainWindow", "Especie"))
        self.labelRaza.setText(_translate("MainWindow", "Raza"))
        self.labelSexo.setText(_translate("MainWindow", "Sexo"))
        self.inputComboBoxSexo.setItemText(
            0, _translate("MainWindow", "Elegir"))
        self.inputComboBoxSexo.setItemText(
            1, _translate("MainWindow", "Macho"))
        self.inputComboBoxSexo.setItemText(
            2, _translate("MainWindow", "Hembra"))
        self.labelFechaNacimiento.setText(
            _translate("MainWindow", "Fecha de nacimiento"))
        self.labelPeso.setText(_translate("MainWindow", "Peso"))
        self.labelSize.setText(_translate("MainWindow", "Tamaño"))
        self.btnAtras.setText(_translate("MainWindow", "Atras"))
        self.btnAgregarMascota.setText(
            _translate("MainWindow", "Agregar mascota"))
        self.inputComboBoxTamano.setItemText(
            0, _translate("MainWindow", "Elegir"))
        self.inputComboBoxTamano.setItemText(
            1, _translate("MainWindow", "Muy Pequeño"))
        self.inputComboBoxTamano.setItemText(
            2, _translate("MainWindow", "Pequeño"))
        self.inputComboBoxTamano.setItemText(
            3, _translate("MainWindow", "Mediano"))
        self.inputComboBoxTamano.setItemText(
            4, _translate("MainWindow", "Grande"))
        self.inputComboBoxTamano.setItemText(
            5, _translate("MainWindow", "Muy Grande"))
        self.labelVolumen.setText(_translate("MainWindow", "Volumen"))
        self.labelKg.setText(_translate("MainWindow", "Kg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiDatos()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
