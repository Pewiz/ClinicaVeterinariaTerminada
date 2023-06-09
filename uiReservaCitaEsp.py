# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agendar_hEspecialista.ui'
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
        MainWindow.resize(709, 540)
        MainWindow.setMinimumSize(QtCore.QSize(709, 540))
        MainWindow.setMaximumSize(QtCore.QSize(709, 540))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 741, 540))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 541))
        self.label.setStyleSheet("background: #FFFFFF;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 731, 80))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(32)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background: #4fa3a6;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(390, 110, 301, 271))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imagenes/Logo-removebg-preview.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(15, 120, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: #4fa3a6;\n"
"border-radius: 10;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(190, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(190, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.botonAtras = QtWidgets.QPushButton(self.widget)
        self.botonAtras.setGeometry(QtCore.QRect(30, 15, 50, 50))
        self.botonAtras.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"  \n"
"    \n"
"    border-radius: 20px;\n"
"\n"
"  \n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #74b6b6;\n"
"}\n"
"")
        self.botonAtras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/boton_regresar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QtCore.QSize(50, 50))
        self.botonAtras.setObjectName("botonAtras")
        self.mascota_box = QtWidgets.QComboBox(self.widget)
        self.mascota_box.setGeometry(QtCore.QRect(40, 210, 121, 22))
        self.mascota_box.setStyleSheet("border: 2px solid #4fa3a6 ;")
        self.mascota_box.setObjectName("mascota_box")
        self.mascota_box.addItem("")
        self.especialidad_box = QtWidgets.QComboBox(self.widget)
        self.especialidad_box.setGeometry(QtCore.QRect(190, 210, 121, 22))
        self.especialidad_box.setStyleSheet("border: 2px solid #4fa3a6 ;")
        self.especialidad_box.setObjectName("especialidad_box")
        self.especialidad_box.addItem("")
        self.especialidad_box.addItem("")
        self.especialidad_box.addItem("")
        self.especialidad_box.addItem("")
        self.especialidad_box.addItem("")
        self.especialidad_box.addItem("")
        self.seleccionar_bloquebtn = QtWidgets.QPushButton(self.widget)
        self.seleccionar_bloquebtn.setGeometry(QtCore.QRect(185, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.seleccionar_bloquebtn.setFont(font)
        self.seleccionar_bloquebtn.setStyleSheet("QPushButton {\n"
"    background: #4fa3a6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #74b6b6;\n"
"}\n"
"")
        self.seleccionar_bloquebtn.setObjectName("seleccionar_bloquebtn")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 370, 321, 111))
        self.label_9.setStyleSheet("border: 2px solid #4fa3a6 ;\n"
"border-radius: 15px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.agregar_hora_3 = QtWidgets.QPushButton(self.widget)
        self.agregar_hora_3.setGeometry(QtCore.QRect(510, 460, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.agregar_hora_3.setFont(font)
        self.agregar_hora_3.setStyleSheet("QPushButton {\n"
"    background: #4fa3a6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #74b6b6;\n"
"}\n"
"")
        self.agregar_hora_3.setObjectName("agregar_hora_3")
        self.labelEncargado = QtWidgets.QLabel(self.widget)
        self.labelEncargado.setGeometry(QtCore.QRect(26, 281, 141, 31))
        self.labelEncargado.setStyleSheet("border: 2px solid #4fa3a6 ;\n"
"border-radius: 15px;")
        self.labelEncargado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEncargado.setObjectName("labelEncargado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clinica CVI"))
        self.label_2.setText(_translate("MainWindow", "Agendar Hora Especialista"))
        self.label_4.setText(_translate("MainWindow", "Agenda tu Hora"))
        self.label_5.setText(_translate("MainWindow", "Mascota:"))
        self.label_6.setText(_translate("MainWindow", "Especialidad:"))
        self.label_7.setText(_translate("MainWindow", "Especialista:"))
        self.label_8.setText(_translate("MainWindow", "Horario:"))
        self.mascota_box.setItemText(0, _translate("MainWindow", "Elegir"))
        self.especialidad_box.setItemText(0, _translate("MainWindow", "Elegir"))
        self.especialidad_box.setItemText(1, _translate("MainWindow", "Neurologo"))
        self.especialidad_box.setItemText(2, _translate("MainWindow", "Reproduccion"))
        self.especialidad_box.setItemText(3, _translate("MainWindow", "Odontologia"))
        self.especialidad_box.setItemText(4, _translate("MainWindow", "Oncologo"))
        self.especialidad_box.setItemText(5, _translate("MainWindow", "Cardiologia"))
        self.seleccionar_bloquebtn.setText(_translate("MainWindow", "Seleccionar Bloque"))
        self.label_9.setText(_translate("MainWindow", "Tu Horario seleccionado se mostrará aqui"))
        self.agregar_hora_3.setText(_translate("MainWindow", "Agendar Hora"))
        self.labelEncargado.setText(_translate("MainWindow", "Encargado aparece aqui..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
