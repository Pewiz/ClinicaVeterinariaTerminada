from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import csv
from SalasHorario import SalasHorario
from ManejoArchivo import GestionArchivo
from datetime import datetime
from PyQt5.QtCore import Qt

class Ui_VentAsignarHorario(object):
    def __init__(self,usuario):
        self._usuario = usuario
        
    def setupUi(self, VentAsignarHorario):
        VentAsignarHorario.setObjectName("VentAsignarHorario")
        VentAsignarHorario.resize(830, 487)
        VentAsignarHorario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bannerSup = QtWidgets.QLabel(VentAsignarHorario)
        self.bannerSup.setGeometry(QtCore.QRect(0, 0, 830, 130))
        self.bannerSup.setStyleSheet("background-color: transparent;")
        self.bannerSup.setText("")
        self.bannerSup.setPixmap(QtGui.QPixmap("imagenes/bannerReserva.png"))
        
        
        
        self.nombreLabel = QtWidgets.QLabel(VentAsignarHorario)
        self.nombreLabel.setGeometry(QtCore.QRect(470, 145, 271, 31))
        self.nombreLabel.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.nombreLnE = QtWidgets.QLineEdit(VentAsignarHorario)
        self.nombreLnE.setGeometry(QtCore.QRect(565, 145, 240, 31))
        self.nombreLnE.setStyleSheet("background-color: rgb(207, 207, 207);\n""font: 75 12pt \"MS Shell Dlg 2\";")
        self.nombreLnE.setEnabled(False)
        
        self.experienciaLabel = QtWidgets.QLabel(VentAsignarHorario)
        self.experienciaLabel.setGeometry(QtCore.QRect(470, 185, 271, 31))
        self.experienciaLabel.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.experienciaLnE = QtWidgets.QLineEdit(VentAsignarHorario)
        self.experienciaLnE.setEnabled(False)
        self.experienciaLnE.setGeometry(QtCore.QRect(565, 185, 240, 31))
        self.experienciaLnE.setStyleSheet("background-color: rgb(207, 207, 207);\n""font: 75 12pt \"MS Shell Dlg 2\";")
        
        self.cargoLabel = QtWidgets.QLabel(VentAsignarHorario)
        self.cargoLabel.setGeometry(QtCore.QRect(470, 225, 271, 31))
        self.cargoLabel.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.cargoLnE = QtWidgets.QLineEdit(VentAsignarHorario)
        self.cargoLnE.setEnabled(False)
        self.cargoLnE.setGeometry(QtCore.QRect(565, 225, 240, 31))
        self.cargoLnE.setStyleSheet("background-color: rgb(207, 207, 207);\n""font: 75 12pt \"MS Shell Dlg 2\";")

        self.fechaABuscarLabel = QtWidgets.QLabel(VentAsignarHorario)
        self.fechaABuscarLabel.setGeometry(QtCore.QRect(470, 280, 271, 31))
        self.fechaABuscarLabel.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.fechaABuscar = QtWidgets.QDateEdit(VentAsignarHorario)
        self.fechaABuscar.setGeometry(QtCore.QRect(630, 274, 171, 45))
        fecha = datetime.now()
        self.fechaABuscar.setDateTime(QtCore.QDateTime(QtCore.QDate(fecha.year, fecha.month, fecha.day), QtCore.QTime(0, 0, 0)))
        self.fechaABuscar.setMinimumDate(QtCore.QDate(fecha.year, fecha.month, fecha.day))
        self.fechaABuscar.dateChanged.connect(self.cargarHorarios)
        
        self.tablaHorarioVet = QtWidgets.QTableWidget(VentAsignarHorario)
        self.tablaHorarioVet.setGeometry(QtCore.QRect(20, 145, 430, 322))
        self.tablaHorarioVet.horizontalHeader().setStretchLastSection(True)
        self.tablaHorarioVet.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaHorarioVet.setColumnCount(3)
        self.tablaHorarioVet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorarioVet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorarioVet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorarioVet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorarioVet.setHorizontalHeaderItem(2,item)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tablaHorarioVet.setFont(font)
        
        self.btnRegresar = QtWidgets.QPushButton(VentAsignarHorario)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 55, 55))
        self.btnRegresar.setIcon((QtGui.QIcon("imagenes/boton_regresar.png")))
        self.btnRegresar.setIconSize(QtCore.QSize(55, 55))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        
        
        self.btnRegresar.clicked.connect(VentAsignarHorario.close)
        self.btnSeleccHora = QtWidgets.QPushButton(VentAsignarHorario)
        self.btnSeleccHora.setGeometry(QtCore.QRect(570, 415, 161, 51))
        self.btnSeleccHora.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                         "border-style: solid;\n"
                                         "border-width: 1px;\n"
                                         "border-color: rgb(0, 51, 102);\n"
                                         "border-radius: 5px;")
        self.btnSeleccHora.clicked.connect(self.seleccionarHora)
        
        self.cargarHorarios()
                
        self.retranslateUi(VentAsignarHorario)
        QtCore.QMetaObject.connectSlotsByName(VentAsignarHorario)


    def retranslateUi(self, VentAsignarHorario):
        _translate = QtCore.QCoreApplication.translate
        nombre = self._usuario['nombres'] + " " + self._usuario['apellido_paterno'] + ""
        VentAsignarHorario.setWindowTitle(_translate("VentAsignarHorario", "Dialog"))
        self.nombreLabel.setText("Nombres:")
        self.cargoLabel.setText("Cargo:")
        self.experienciaLabel.setText("Experiencia:")
        self.fechaABuscarLabel.setText("Filtrar por Fecha:")
        self.nombreLnE.setText(_translate("VentAsignarHorario", nombre))
        self.cargoLnE.setText(_translate("VentAsignarHorario", self._usuario['cargo']))
        self.experienciaLnE.setText(_translate("VentAsignarHorario", self._usuario['experiencia']))
        item = self.tablaHorarioVet.horizontalHeaderItem(0)
        item.setText(_translate("VentAsignarHorario", "Sala"))
        item = self.tablaHorarioVet.horizontalHeaderItem(1)
        item.setText(_translate("VentAsignarHorario", "Horario"))
        item = self.tablaHorarioVet.horizontalHeaderItem(2)
        item.setText(_translate("VentAsignarHorario", "Fecha"))
        self.btnSeleccHora.setText(_translate("VentAsignarHorario", "Seleccionar Hora"))


        

    def cargarHorarios(self):
        self.tablaHorarioVet.clearContents()
        self.tablaHorarioVet.setRowCount(0)
        encabezados =  ["Sala","Horario","Fecha"]
        self.tablaHorarioVet.setHorizontalHeaderLabels(encabezados)

        salasEncontradas = self.horarioSalas()

        for sala in salasEncontradas:
            posicionFila = self.tablaHorarioVet.rowCount()
            self.tablaHorarioVet.insertRow(posicionFila)
            for columna in range(5):
                if columna == 2:
                    value = sala.numSala
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tablaHorarioVet.setItem(posicionFila, columna-2, item)
                elif columna == 3:
                    value = sala.horario
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tablaHorarioVet.setItem(posicionFila, columna-2, item)
                elif columna == 4:
                    value = sala.fecha
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tablaHorarioVet.setItem(posicionFila, columna-2, item)
        for fila in range(self.tablaHorarioVet.rowCount()):
            for columna in range(self.tablaHorarioVet.columnCount()):
                item = self.tablaHorarioVet.item(fila, columna)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tablaHorarioVet.setRowHeight(fila, 33)
            
        self.tablaHorarioVet.setColumnWidth(0, 50)
        self.tablaHorarioVet.setColumnWidth(1, 160)
        self.tablaHorarioVet.setColumnWidth(2, 50)

                        
    def seleccionarHora(self):
        fila = self.tablaHorarioVet.currentRow()
        if fila != -1:
            rut = str(self._usuario['rut'])
            numSala = self.tablaHorarioVet.item(fila, 0).text()
            horario = self.tablaHorarioVet.item(fila, 1).text()        
            fecha = self.tablaHorarioVet.item(fila, 2).text()
            horaVet = SalasHorario(id=rut,rut=None,sala=numSala,horario=horario,fecha=fecha,disp="False")
            
            GestionArchivo.insertar("ArchivosCSV/salas.csv",horaVet)
            self.alertBox("Horario Guardado correctamente","Horario Veterinario")
            self.cargarHorarios()
        else:
            self.alertBox("Debe seleccionar una hora","Alerta")

    def horariosVet(self,objeto):
        salasOcupadas = GestionArchivo.seleccionarTodo("ArchivosCSV/salas.csv")

        for sala in salasOcupadas:
            salaOcupada = SalasHorario(sala[0],sala[1],sala[2],sala[3],sala[4])

            if objeto.fecha == salaOcupada.fecha:
                if objeto.horario == salaOcupada.horario:
                    if objeto.numSala == salaOcupada.numSala:
                        return False
                
        return True
                    


    def horarioSalas(self):
        salas = GestionArchivo.seleccionarTodo("ArchivosCSV/horarioSalas.csv")
        fechaE = self.fechaABuscar.date().toString("dd/MM/yyyy")
        salasDisp = []
        for sala in salas:
            objetoSala = SalasHorario(sala[0],sala[1],sala[2],sala[3],fechaE)
            verificador = self.horariosVet(objetoSala)
            if verificador:
                salasDisp.append(objetoSala)

        return salasDisp

    def alertBox(self, Mensaje, Titulo):
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.exec_()

                    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_VentAsignarHorario()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
