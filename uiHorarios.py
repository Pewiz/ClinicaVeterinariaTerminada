# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Horarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class uiVent(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(697, 509)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(697, 509))
        mainWindow.setMaximumSize(QtCore.QSize(697, 509))
        mainWindow.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
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
        self.label_9.setGeometry(QtCore.QRect(270, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 61, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imagenes/Atras.png"))
        self.label_3.setObjectName("label_3")
        self.btnAtras = QtWidgets.QPushButton(self.frame_2)
        self.btnAtras.setGeometry(QtCore.QRect(50, 50, 31, 31))
        self.btnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAtras.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnAtras.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.btnAtras.setText("")
        self.btnAtras.setObjectName("btnAtras")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(410, 120, 291, 301))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("imagenes/Logo-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.btnElegir = QtWidgets.QPushButton(self.frame)
        self.btnElegir.setEnabled(True)
        self.btnElegir.setGeometry(QtCore.QRect(530, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.btnElegir.setFont(font)
        self.btnElegir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnElegir.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-radius: 5px;")
        self.btnElegir.setCheckable(False)
        self.btnElegir.setObjectName("btnElegir")
        self.listaHorario = QtWidgets.QTableWidget(self.frame)
        self.listaHorario.setGeometry(QtCore.QRect(10, 100, 507, 391))
        self.listaHorario.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listaHorario.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listaHorario.setObjectName("tableWidget")
        self.listaHorario.setColumnCount(5)
        self.listaHorario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listaHorario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaHorario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaHorario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaHorario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaHorario.setHorizontalHeaderItem(4, item)
        self.listaHorario.horizontalHeader().setDefaultSectionSize(101)
        self.listaHorario.horizontalHeader().setMinimumSectionSize(39)
        self.listaHorario.verticalHeader().setVisible(False)
        self.fechaL = QtWidgets.QLabel(self.frame)
        self.fechaL.setGeometry(QtCore.QRect(570, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.fechaL.setFont(font)
        self.fechaL.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.fechaL.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.fechaL.setObjectName("label_10")
        self.FechaHoy = QtWidgets.QDateEdit(self.centralwidget)
        self.FechaHoy.setGeometry(QtCore.QRect(550, 150, 110, 22))
        self.FechaHoy.setMaximumDate(QtCore.QDate(2024, 12, 31))
        self.FechaHoy.setMinimumDate(QtCore.QDate(2023, 6, 13))
        self.FechaHoy.setCalendarPopup(True)
        self.FechaHoy.setObjectName("dateEdit")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clinica CVI"))
        self.label_9.setText(_translate("mainWindow", "Horarios"))
        self.btnElegir.setText(_translate("mainWindow", "Elegir Horario"))
        item = self.listaHorario.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Hora"))
        item = self.listaHorario.horizontalHeaderItem(1)
        item = self.listaHorario.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Sala"))
        item = self.listaHorario.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Persona a Cargo"))
        item = self.listaHorario.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "Disponibilidad"))
        self.fechaL.setText(_translate("mainWindow", "Fecha:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = uiVent()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())