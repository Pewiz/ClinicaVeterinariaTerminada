# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaVerDatosC.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class uiVerD(object):
    def setupUi(self, mainWindow):
        mainWindow.setWindowIcon(QtGui.QIcon('Imagenes/logo.png'))
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 509)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(700, 509))
        mainWindow.setMaximumSize(QtCore.QSize(700, 509))
        mainWindow.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 711, 511))
        self.frame.setMinimumSize(QtCore.QSize(711, 511))
        self.frame.setMaximumSize(QtCore.QSize(711, 511))
        self.frame.setSizeIncrement(QtCore.QSize(10000, 10000))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                 "border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-10, -20, 721, 101))
        self.frame_2.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 80, 120, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(70, 99, 331, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(270, 40, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(210, 110, 291, 301))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(
            "imagenes\Logo-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.btnAtras = QtWidgets.QPushButton(self.frame)
        self.btnAtras.setEnabled(True)
        self.btnAtras.setGeometry(QtCore.QRect(490, 440, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(14)
        self.btnAtras.setFont(font)
        self.btnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAtras.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                    "border-radius: 5px;")
        self.btnAtras.setCheckable(False)
        self.btnAtras.setObjectName("btnAtras")
        self.btnMenuPrincipal = QtWidgets.QPushButton(self.frame)
        self.btnMenuPrincipal.setEnabled(True)
        self.btnMenuPrincipal.setGeometry(QtCore.QRect(30, 440, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(14)
        self.btnMenuPrincipal.setFont(font)
        self.btnMenuPrincipal.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenuPrincipal.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                            "border-radius: 5px;")
        self.btnMenuPrincipal.setCheckable(False)
        self.btnMenuPrincipal.setObjectName("btnMenuPrincipal")
        self.labelNombreC = QtWidgets.QLabel(self.frame)
        self.labelNombreC.setGeometry(QtCore.QRect(30, 170, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelNombreC.setFont(font)
        self.labelNombreC.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelNombreC.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelNombreC.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNombreC.setObjectName("labelNombreC")
        self.labelRut = QtWidgets.QLabel(self.frame)
        self.labelRut.setGeometry(QtCore.QRect(81, 220, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelRut.setFont(font)
        self.labelRut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelRut.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelRut.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRut.setObjectName("labelRut")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(94, 136, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 225, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 275, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.labelGenero = QtWidgets.QLabel(self.frame)
        self.labelGenero.setGeometry(QtCore.QRect(100, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelGenero.setFont(font)
        self.labelGenero.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelGenero.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelGenero.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGenero.setObjectName("labelGenero")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(60, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.labelFecha = QtWidgets.QLabel(self.frame)
        self.labelFecha.setGeometry(QtCore.QRect(64, 352, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelFecha.setFont(font)
        self.labelFecha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelFecha.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelFecha.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFecha.setObjectName("labelFecha")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(400, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                    "border-radius: 10px;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(459, 137, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.labelDireccion = QtWidgets.QLabel(self.frame)
        self.labelDireccion.setGeometry(QtCore.QRect(350, 170, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelDireccion.setFont(font)
        self.labelDireccion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelDireccion.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelDireccion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDireccion.setObjectName("labelDireccion")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(462, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.labelCorreo = QtWidgets.QLabel(self.frame)
        self.labelCorreo.setGeometry(QtCore.QRect(350, 253, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelCorreo.setFont(font)
        self.labelCorreo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelCorreo.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelCorreo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCorreo.setObjectName("labelCorreo")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(393, 346, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.labelTelefono = QtWidgets.QLabel(self.frame)
        self.labelTelefono.setGeometry(QtCore.QRect(470, 340, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelTelefono.setFont(font)
        self.labelTelefono.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTelefono.setStyleSheet("border: 2px solid #4FA3A6;")
        self.labelTelefono.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTelefono.setObjectName("labelTelefono")
        self.label_logo.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.btnAtras.raise_()
        self.btnMenuPrincipal.raise_()
        self.labelNombreC.raise_()
        self.labelRut.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.labelGenero.raise_()
        self.label_10.raise_()
        self.labelFecha.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.labelDireccion.raise_()
        self.label_15.raise_()
        self.labelCorreo.raise_()
        self.label_17.raise_()
        self.labelTelefono.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clinica CVI"))
        self.label.setText(_translate("mainWindow", "Datos Personales"))
        self.label_9.setText(_translate("mainWindow", "Cliente"))
        self.btnAtras.setText(_translate(
            "mainWindow", "Volver a Lista Cliente"))
        self.btnMenuPrincipal.setText(_translate(
            "mainWindow", "Volver a Administración"))
        self.labelNombreC.setText(_translate("mainWindow", "Nombre Completo"))
        self.labelRut.setText(_translate("mainWindow", "12345678-9"))
        self.label_5.setText(_translate("mainWindow", "Nombre Completo:"))
        self.label_6.setText(_translate("mainWindow", "Rut:"))
        self.label_7.setText(_translate("mainWindow", "Genero:"))
        self.labelGenero.setText(_translate("mainWindow", "Genero"))
        self.label_10.setText(_translate("mainWindow", "Fecha Nacimiento"))
        self.labelFecha.setText(_translate("mainWindow", "dd/mm/yyyy"))
        self.label_12.setText(_translate("mainWindow", "Datos Contacto"))
        self.label_13.setText(_translate("mainWindow", "Dirección:"))
        self.labelDireccion.setText(_translate("mainWindow", "Dirección"))
        self.label_15.setText(_translate("mainWindow", "Correo Electronico:"))
        self.labelCorreo.setText(_translate(
            "mainWindow", "Correo Electronico"))
        self.label_17.setText(_translate("mainWindow", "Telefono:"))
        self.labelTelefono.setText(_translate("mainWindow", "123456789"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = uiVerD()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
