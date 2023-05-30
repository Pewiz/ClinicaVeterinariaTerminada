# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaQuirofano.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, Qt



class Ui_agendarQuirofano(object):
    def setupUi(self, agendarQuirofano):
        agendarQuirofano.setObjectName("agendarQuirofano")
        agendarQuirofano.resize(600, 400)
        agendarQuirofano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(agendarQuirofano)
        self.centralwidget.setObjectName("centralwidget")
        self.botonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.botonAtras.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.botonAtras.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.botonAtras.setObjectName("botonAtras")
        self.botonAtras.clicked.connect(agendarQuirofano.close)
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(150, 0, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.comboTipo = QtWidgets.QComboBox(self.centralwidget)
        self.comboTipo.setGeometry(QtCore.QRect(350, 120, 131, 21))
        self.comboTipo.setStyleSheet("")
        self.comboTipo.setEditable(False)
        self.comboTipo.setCurrentText("")
        self.comboTipo.setObjectName("comboTipo")
        self.comboTipo.addItems(["Oncologica", "Oculares", "Intestinal", "Otros"])
        self.botonAgendar = QtWidgets.QPushButton(self.centralwidget)
        self.botonAgendar.setGeometry(QtCore.QRect(280, 300, 75, 23))
        self.botonAgendar.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.botonAgendar.setObjectName("botonAgendar")
        self.botonAgendar.clicked.connect(self.agendar)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 160, 61, 21))
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 120, 61, 21))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(350, 160, 131, 21))
        self.dateEdit.setObjectName("dateEdit")
        fecha_actual = QDate.currentDate()
        self.dateEdit.setMinimumDate(fecha_actual)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 200, 61, 21))
        self.label_6.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_6.setObjectName("label_6")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(350, 200, 131, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setMinimumTime(QTime(9, 0)) 
        self.timeEdit.setMaximumTime(QTime(16, 0))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 240, 61, 21))
        self.label_7.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_7.setObjectName("label_7")
        self.comboSala = QtWidgets.QComboBox(self.centralwidget)
        self.comboSala.setGeometry(QtCore.QRect(350, 240, 131, 21))
        self.comboSala.setStyleSheet("")
        self.comboSala.setEditable(False)
        self.comboSala.setCurrentText("")
        self.comboSala.setObjectName("comboSala")
        self.comboSala.addItems(["Sala 1", "Sala 2", "Sala 3"])
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 80, 61, 21))
        self.label_5.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_5.setObjectName("label_5")
        self.lineNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNombre.setGeometry(QtCore.QRect(350, 80, 131, 20))
        self.lineNombre.setObjectName("lineNombre")
        agendarQuirofano.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(agendarQuirofano)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        agendarQuirofano.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(agendarQuirofano)
        self.statusbar.setObjectName("statusbar")
        agendarQuirofano.setStatusBar(self.statusbar)

        self.retranslateUi(agendarQuirofano)
        QtCore.QMetaObject.connectSlotsByName(agendarQuirofano)

    def retranslateUi(self, agendarQuirofano):
        _translate = QtCore.QCoreApplication.translate
        agendarQuirofano.setWindowTitle(_translate("agendarQuirofano", "MainWindow"))
        self.botonAtras.setText(_translate("agendarQuirofano", "Atras"))
        self.titulo.setText(_translate("agendarQuirofano", "<html><head/><body><p>Agendar hora quirofano</p><p><br/></p></body></html>"))
        self.botonAgendar.setText(_translate("agendarQuirofano", "Agendar Hora"))
        self.label_3.setText(_translate("agendarQuirofano", "Fecha"))
        self.label_4.setText(_translate("agendarQuirofano", "Tipo"))
        self.label_6.setText(_translate("agendarQuirofano", "Hora"))
        self.label_7.setText(_translate("agendarQuirofano", "Sala"))
        self.label_5.setText(_translate("agendarQuirofano", "Nombre"))

    def agendar(self):
        tipo = self.comboTipo.currentText()
        fecha = self.dateEdit.date().toString(Qt.ISODate)
        hora = self.timeEdit.time().toString()
        sala = self.comboSala.currentText()
        nombre = self.lineNombre.text()

        archivo_existe = os.path.exists("Quirofano.csv")
        
        with open("Quirofano.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            if not archivo_existe:
                writer.writerow(["fecha", "nombre", "tipo", "hora", "sala"])
            
            writer.writerow([fecha, nombre, tipo, hora, sala])
            print("se ha agendado correctamente")
        