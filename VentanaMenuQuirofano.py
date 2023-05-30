# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaMenuQuirofano.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from verHorasQuirofano import Ui_horasQuirofano
from PyQt5 import QtCore, QtGui, QtWidgets
from AgendarQuirofano import Ui_agendarQuirofano

class Ui_VentanaMenuQuirofano(object):
    def setupUi(self, VentanaMenuQuirofano):
        VentanaMenuQuirofano.setObjectName("VentanaMenuQuirofano")
        VentanaMenuQuirofano.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(VentanaMenuQuirofano)
        self.centralwidget.setObjectName("centralwidget")
        self.botonAgendar = QtWidgets.QPushButton(self.centralwidget)
        self.botonAgendar.setGeometry(QtCore.QRect(160, 150, 71, 61))
        self.botonAgendar.setObjectName("botonAgendar")
        self.botonAgendar.clicked.connect(self.abrirVentAgendar)
        self.botonVerHoras = QtWidgets.QPushButton(self.centralwidget)
        self.botonVerHoras.setGeometry(QtCore.QRect(330, 150, 71, 61))
        self.botonVerHoras.setObjectName("botonVerHoras")
        self.botonVerHoras.clicked.connect(self.abrirVentVerHoras)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 231, 71))
        self.label.setObjectName("label")
        self.botonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.botonAtras.setGeometry(QtCore.QRect(20, 300, 75, 23))
        self.botonAtras.setObjectName("botonAtras")
        self.botonAtras.clicked.connect(VentanaMenuQuirofano.close)
        VentanaMenuQuirofano.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaMenuQuirofano)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        VentanaMenuQuirofano.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaMenuQuirofano)
        self.statusbar.setObjectName("statusbar")
        VentanaMenuQuirofano.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaMenuQuirofano)
        QtCore.QMetaObject.connectSlotsByName(VentanaMenuQuirofano)

    def retranslateUi(self, VentanaMenuQuirofano):
        _translate = QtCore.QCoreApplication.translate
        VentanaMenuQuirofano.setWindowTitle(_translate("VentanaMenuQuirofano", "MainWindow"))
        self.botonAgendar.setText(_translate("VentanaMenuQuirofano", "Agendar"))
        self.botonVerHoras.setText(_translate("VentanaMenuQuirofano", "Ver Horas"))
        self.label.setText(_translate("VentanaMenuQuirofano", "<html><head/><body><p><span style=\" font-size:20pt;\">Menu Quirofano</span></p><p><br/></p></body></html>"))
        self.botonAtras.setText(_translate("VentanaMenuQuirofano", "Atras"))

    def abrirVentAgendar(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_agendarQuirofano()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    def abrirVentVerHoras(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_horasQuirofano()
        self.ui.setupUi(self.ventana)
        self.ventana.show()