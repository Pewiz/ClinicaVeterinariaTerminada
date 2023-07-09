# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HoraControlRutinario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('Imagenes/logo.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 540)
        MainWindow.setMinimumSize(QtCore.QSize(711, 540))
        MainWindow.setMaximumSize(QtCore.QSize(711, 540))
        font = QtGui.QFont()
        font.setPointSize(36)
        MainWindow.setFont(font)
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
        self.subMenu.setGeometry(QtCore.QRect(10, 100, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subMenu.setFont(font)
        self.subMenu.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-radius: 15px;\n"
"")
        self.subMenu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.subMenu.setObjectName("subMenu")
        self.FondoPerrito = QtWidgets.QLabel(self.frame)
        self.FondoPerrito.setGeometry(QtCore.QRect(390, 120, 321, 311))
        self.FondoPerrito.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FondoPerrito.setText("")
        self.FondoPerrito.setPixmap(QtGui.QPixmap("imagenes/Logo-removebg-preview.png"))
        self.FondoPerrito.setScaledContents(True)
        self.FondoPerrito.setObjectName("FondoPerrito")
        self.labelMascota = QtWidgets.QLabel(self.frame)
        self.labelMascota.setGeometry(QtCore.QRect(50, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelMascota.setFont(font)
        self.labelMascota.setStyleSheet("")
        self.labelMascota.setObjectName("labelMascota")
        self.labelHorario = QtWidgets.QLabel(self.frame)
        self.labelHorario.setGeometry(QtCore.QRect(190, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelHorario.setFont(font)
        self.labelHorario.setStyleSheet("")
        self.labelHorario.setObjectName("labelHorario")
        self.ButtonAtras = QtWidgets.QPushButton(self.frame)
        self.ButtonAtras.setGeometry(QtCore.QRect(10, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonAtras.setFont(font)
        self.ButtonAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonAtras.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: #4fa3a6;\n"
"}\n"
"QPushButton::hover {\n"
"    background: rgb(181, 181, 181) ;\n"
"}\n"
"")
        self.ButtonAtras.setObjectName("ButtonAtras")
        self.ButtonAgendarHora = QtWidgets.QPushButton(self.frame)
        self.ButtonAgendarHora.setGeometry(QtCore.QRect(520, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonAgendarHora.setFont(font)
        self.ButtonAgendarHora.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonAgendarHora.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: #4fa3a6;\n"
"}\n"
"QPushButton::hover {\n"
"    background: rgb(181, 181, 181) ;\n"
"}\n"
"")
        self.ButtonAgendarHora.setObjectName("ButtonAgendarHora")
        self.MascotaComboBox = QtWidgets.QComboBox(self.frame)
        self.MascotaComboBox.setGeometry(QtCore.QRect(30, 200, 101, 31))
        self.MascotaComboBox.setStyleSheet("border: 3px solid #4fa3a6 ;")
        self.MascotaComboBox.setObjectName("MascotaComboBox")
        self.MascotaComboBox.addItem("")
        self.Titulo = QtWidgets.QLabel(self.frame)
        self.Titulo.setGeometry(QtCore.QRect(0, 0, 711, 80))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("background: #4fa3a6;")
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.ButtonHorarios = QtWidgets.QPushButton(self.frame)
        self.ButtonHorarios.setGeometry(QtCore.QRect(190, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonHorarios.setFont(font)
        self.ButtonHorarios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonHorarios.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: #dfdfdf;\n"
"}\n"
"QPushButton::hover {\n"
"    background: rgb(189, 255, 253) ;\n"
"}\n"
"")
        self.ButtonHorarios.setObjectName("ButtonHorarios")
        self.subMenu_2 = QtWidgets.QLabel(self.frame)
        self.subMenu_2.setGeometry(QtCore.QRect(30, 270, 331, 141))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subMenu_2.setFont(font)
        self.subMenu_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.subMenu_2.setStyleSheet("border: 3px solid #4fa3a6 ;\n"
"border-radius: 15px;\n"
"")
        self.subMenu_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.subMenu_2.setObjectName("subMenu_2")
        self.FondoPerrito.raise_()
        self.subMenu.raise_()
        self.labelMascota.raise_()
        self.labelHorario.raise_()
        self.ButtonAtras.raise_()
        self.ButtonAgendarHora.raise_()
        self.MascotaComboBox.raise_()
        self.Titulo.raise_()
        self.ButtonHorarios.raise_()
        self.subMenu_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clinica CVI"))
        self.subMenu.setText(_translate("MainWindow", "          Complete los cuadros correctamente"))
        self.labelMascota.setText(_translate("MainWindow", "Mascota"))
        self.labelHorario.setText(_translate("MainWindow", "Elegir Horario"))
        self.ButtonAtras.setText(_translate("MainWindow", "Atras"))
        self.ButtonAgendarHora.setText(_translate("MainWindow", "Agendar Hora"))
        self.MascotaComboBox.setItemText(0, _translate("MainWindow", "Elegir"))
        self.Titulo.setText(_translate("MainWindow", "Agendar Hora C.Rutinario"))
        self.ButtonHorarios.setText(_translate("MainWindow", "Bloque Horarios"))
        self.subMenu_2.setText(_translate("MainWindow", "Fecha: tanto\n"
"Sala: Tanto.\n"
"Hora: tanto"))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
