# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class uiVentUsuario(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(700, 600))
        mainWindow.setMaximumSize(QtCore.QSize(700, 600))
        mainWindow.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 711, 600))
        self.frame.setMinimumSize(QtCore.QSize(711, 600))
        self.frame.setMaximumSize(QtCore.QSize(711, 600))
        self.frame.setSizeIncrement(QtCore.QSize(10000, 10000))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 171, 31))
        self.lineEdit.setStyleSheet("border-color: rgb(30, 146, 148);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 250, 131, 31))
        self.lineEdit_3.setMaxLength(8)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(250, 170, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(50, 330, 110, 22))
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(250, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setMaxLength(9)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(250, 340, 91, 21))
        self.label_cargo = QtWidgets.QLabel(self.frame)
        self.label_cargo.setGeometry(QtCore.QRect(230, 410, 91, 50))
        self.label_experiencia = QtWidgets.QLabel(self.frame)
        self.label_experiencia.setGeometry(QtCore.QRect(320, 410, 150, 50))
        self.label_meses = QtWidgets.QLabel(self.frame)
        self.label_meses.setGeometry(QtCore.QRect(375, 462, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_cargo.setFont(font)
        self.label_cargo.setObjectName("label_cargo")
        self.label_experiencia.setFont(font)
        self.label_experiencia.setObjectName("label_experiencia")
        self.label_meses.setFont(font)
        self.label_meses.setObjectName("label_meses")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(220, 370, 151, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
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
        self.label_9.setGeometry(QtCore.QRect(220, 40, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_9.setObjectName("label_9")
        self.BtnAtras = QtWidgets.QPushButton(self.frame)
        self.BtnAtras.setEnabled(True)
        self.BtnAtras.setGeometry(QtCore.QRect(30, 525, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.BtnAtras.setFont(font)
        self.BtnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAtras.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                    "border-radius: 5px;")
        self.BtnAtras.setCheckable(False)
        self.BtnAtras.setObjectName("BtnAtras")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(250, 200, 81, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBoxCargo = QtWidgets.QComboBox(self.frame)
        self.comboBoxCargo.setGeometry(QtCore.QRect(220, 460, 81, 31))
        self.comboBoxCargo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxCargo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBoxCargo.setObjectName("comboBoxCargo")
        self.comboBoxCargo.addItem("")
        self.comboBoxCargo.addItem("")
        self.comboBoxCargo.addItem("")
        self.comboBoxCargo.addItem("")
        self.comboBoxCargo.addItem("")
        self.comboBoxCargo.addItem("")
        self.comboBoxCargo.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(325, 460, 40, 31))
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.spinBox.setMaximum(999)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 120, 161, 31))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(400, 120, 291, 301))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(
            "imagenes\Logo-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.btnAgMas = QtWidgets.QPushButton(self.frame)
        self.btnAgMas.setEnabled(True)
        self.btnAgMas.setGeometry(QtCore.QRect(490, 525, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.btnAgMas.setFont(font)
        self.btnAgMas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgMas.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                    "border-radius: 5px;")
        self.btnAgMas.setCheckable(False)
        self.btnAgMas.setObjectName("btnAgMas")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 250, 31, 31))
        self.lineEdit_6.setMaxLength(1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(170, 250, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(20, 360, 191, 21))
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(20, 430, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 390, 161, 31))
        self.lineEdit_4.setMaxLength(32767)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_password.setGeometry(QtCore.QRect(30, 460, 161, 31))
        self.lineEdit_password.setMaxLength(32767)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 160, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 190, 161, 31))
        self.lineEdit_5.setMinimumSize(QtCore.QSize(161, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.frame_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.lineEdit_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.dateEdit.raise_()
        self.label_6.raise_()
        self.lineEdit_7.raise_()
        self.label_8.raise_()
        self.label_cargo.raise_()
        self.label_experiencia.raise_()
        self.label_meses.raise_()
        self.lineEdit_8.raise_()
        self.BtnAtras.raise_()
        self.comboBox.raise_()
        self.comboBoxCargo.raise_()
        self.spinBox.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.label_logo.raise_()
        self.btnAgMas.raise_()
        self.lineEdit_6.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_password.raise_()
        self.label_7.raise_()
        self.lineEdit_5.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        mainWindow.setTabOrder(self.lineEdit_2, self.BtnAtras)
        mainWindow.setTabOrder(self.BtnAtras, self.lineEdit_3)
        mainWindow.setTabOrder(self.lineEdit_3, self.dateEdit)
        mainWindow.setTabOrder(self.dateEdit, self.lineEdit_7)
        mainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clinica CVI"))
        self.label.setText(_translate("mainWindow", "Nombres"))
        self.label_3.setText(_translate("mainWindow", "Rut (Sin Puntos)"))
        self.label_4.setText(_translate("mainWindow", "Genero"))
        self.label_5.setText(_translate("mainWindow", "Fecha de nacimiento"))
        self.label_6.setText(_translate("mainWindow", "Telefono"))
        self.label_8.setText(_translate("mainWindow", "Domicilio"))
        self.label_cargo.setText(_translate("mainWindow", "Cargo"))
        self.label_experiencia.setText(_translate("mainWindow", "Experiencia"))
        self.label_meses.setText(_translate("mainWindow", "Meses"))
        self.label_9.setText(_translate("mainWindow", "Datos Usuario"))
        self.BtnAtras.setText(_translate("mainWindow", "Atras"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Elegir"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Masculino"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Femenino"))
        self.comboBoxCargo.setItemText(0, _translate("mainWindow", "Elegir"))
        self.comboBoxCargo.setItemText(1, _translate("mainWindow", "Neurología"))
        self.comboBoxCargo.setItemText(2, _translate("mainWindow", "Reproducción"))
        self.comboBoxCargo.setItemText(3, _translate("mainWindow", "Odontología"))
        self.comboBoxCargo.setItemText(4, _translate("mainWindow", "Oncología"))
        self.comboBoxCargo.setItemText(5, _translate("mainWindow", "Cargiología"))
        self.comboBoxCargo.setItemText(6, _translate("mainWindow", "Cirujano"))
        self.label_2.setText(_translate("mainWindow", "Apellido Paterno"))
        self.btnAgMas.setText(_translate("mainWindow", "Agregar Usuario"))
        self.label_11.setText(_translate("mainWindow", "-"))
        self.label_12.setText(_translate("mainWindow", "Correo Electronico"))
        self.label_13.setText(_translate("mainWindow", "Contraseña"))
        self.label_7.setText(_translate("mainWindow", "Apellido Materno"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = uiVentUsuario()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
