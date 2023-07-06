# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentVerHorarioVet.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_VentVerHorario(object):
    def __init__(self,usuario,fila,ventanaOrigen):
        self._usuario = usuario
        self._fila = fila
        self._ventanaOrigen = ventanaOrigen

    def setupUi(self, VentVerHorario):
        VentVerHorario.setObjectName("VentVerHorario")
        VentVerHorario.resize(950, 680)
        VentVerHorario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bannerSup = QtWidgets.QLabel(VentVerHorario)
        self.bannerSup.setGeometry(QtCore.QRect(0, 0, 950, 130))
        self.bannerSup.setStyleSheet("background-color: transparent;")
        self.bannerSup.setText("")
        self.bannerSup.setPixmap(QtGui.QPixmap("imagenes/bannerClinica.png"))
        self.bannerSup.setObjectName("bannerSup")
        self.rutLnE = QtWidgets.QLineEdit(VentVerHorario)
        self.rutLnE.setEnabled(False)
        self.rutLnE.setGeometry(QtCore.QRect(40, 170, 161, 31))
        self.rutLnE.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.rutLnE.setText("")
        self.rutLnE.setObjectName("rutLnE")
        self.nombreLnE = QtWidgets.QLineEdit(VentVerHorario)
        self.nombreLnE.setEnabled(False)
        self.nombreLnE.setGeometry(QtCore.QRect(230, 170, 311, 31))
        self.nombreLnE.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.nombreLnE.setText("")
        self.nombreLnE.setFrame(True)
        self.nombreLnE.setObjectName("nombreLnE")
        self.fechaABuscar = QtWidgets.QDateEdit(VentVerHorario)
        self.fechaABuscar.setGeometry(QtCore.QRect(570, 170, 171, 31))
        self.fechaABuscar.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 5, 28), QtCore.QTime(0, 0, 0)))
        self.fechaABuscar.setMinimumDate(QtCore.QDate(2023, 5, 28))
        self.fechaABuscar.setCalendarPopup(True)
        self.fechaABuscar.setTimeSpec(QtCore.Qt.LocalTime)
        self.fechaABuscar.setObjectName("fechaABuscar")
        self.tablaHorasVet = QtWidgets.QTableWidget(VentVerHorario)
        self.tablaHorasVet.setEnabled(True)
        self.tablaHorasVet.setGeometry(QtCore.QRect(40, 230, 661, 411))
        self.tablaHorasVet.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaHorasVet.setObjectName("tablaHorasVet")
        self.tablaHorasVet.setColumnCount(5)
        self.tablaHorasVet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorasVet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorasVet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorasVet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorasVet.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorasVet.setHorizontalHeaderItem(4, item)
        self.tablaHorasVet.horizontalHeader().setStretchLastSection(True)
        self.btnRegresar = QtWidgets.QPushButton(VentVerHorario)
        self.btnRegresar.setGeometry(QtCore.QRect(10, 50, 41, 31))
        self.btnRegresar.setStyleSheet("background-color: transparent;")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnRegresar.clicked.connect(VentVerHorario.close)
        self.btnRevisarHorario = QtWidgets.QPushButton(VentVerHorario)
        self.btnRevisarHorario.setGeometry(QtCore.QRect(740, 230, 121, 51))
        self.btnRevisarHorario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnRevisarHorario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")
        self.btnRevisarHorario.setObjectName("btnRevisarHorario")
        self.btnRevisarHorario.clicked.connect(lambda: self.cargarUsuarioCSV())
        self.btnEliminarHorario = QtWidgets.QPushButton(VentVerHorario)
        self.btnEliminarHorario.setGeometry(QtCore.QRect(740, 310, 121, 51))
        self.btnEliminarHorario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnEliminarHorario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")
        self.btnEliminarHorario.setObjectName("btnEliminarHorario")

        self.retranslateUi(VentVerHorario)
        QtCore.QMetaObject.connectSlotsByName(VentVerHorario)
        

    def retranslateUi(self, VentVerHorario):
        _translate = QtCore.QCoreApplication.translate
        nombre = self._usuario.nombres + " "+ self._usuario.apellidoPa+""
        VentVerHorario.setWindowTitle(_translate("VentVerHorario", "Dialog"))
        self.rutLnE.setText(_translate("VentAsignarHorario", self._usuario.rut))
        self.nombreLnE.setText(_translate("VentAsignarHorario", nombre))
        item = self.tablaHorasVet.horizontalHeaderItem(0)
        item.setText(_translate("VentVerHorario", "Rut Veterinario"))
        item = self.tablaHorasVet.horizontalHeaderItem(1)
        item.setText(_translate("VentVerHorario", "Rut Cliente"))
        item = self.tablaHorasVet.horizontalHeaderItem(2)
        item.setText(_translate("VentVerHorario", "Sala"))
        item = self.tablaHorasVet.horizontalHeaderItem(3)
        item.setText(_translate("VentVerHorario", "Horario"))
        item = self.tablaHorasVet.horizontalHeaderItem(4)
        item.setText(_translate("VentVerHorario", "Fecha"))
        self.btnRevisarHorario.setText(_translate("VentVerHorario", "Revisar Horario"))
        self.btnEliminarHorario.setText(_translate("VentVerHorario", "Eliminar Hora"))

    def cargarUsuarioCSV(self):
        self.tablaHorasVet.clearContents()
        self.tablaHorasVet.setRowCount(0)

        with open('ArchivosCSV/salas.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            encabezados = next(reader)
            self.tablaHorasVet.setHorizontalHeaderLabels(encabezados)
            
            for fila in reader:
                if fila[0] == self.rutLnE.text() and fila[4] == self.fechaABuscar.date().toString("dd/MM/yyyy"):
                   posicionFila = self.tablaHorasVet.rowCount()
                   self.tablaHorasVet.insertRow(posicionFila)
                   for columna, value in enumerate(fila):
                      item = QtWidgets.QTableWidgetItem(value)
                      self.tablaHorasVet.setItem(posicionFila, columna, item)
                    
        self.tablaHorasVet.resizeColumnsToContents()
        self.tablaHorasVet.resizeRowsToContents()
