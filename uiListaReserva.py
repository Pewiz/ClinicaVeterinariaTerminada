# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListaReservas.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
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
        self.labelTitulo = QtWidgets.QLabel(self.frame_2)
        self.labelTitulo.setGeometry(QtCore.QRect(100, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(20)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.labelTitulo.setObjectName("labelTitulo")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 61, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imagenes/Atras.png"))
        self.label_3.setObjectName("label_3")
        self.botonAtras = QtWidgets.QPushButton(self.frame_2)
        self.botonAtras.setGeometry(QtCore.QRect(30, 35, 50, 50))
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
        self.labelNombre = QtWidgets.QLabel(self.frame_2)
        self.labelNombre.setGeometry(QtCore.QRect(410, 40, 265, 41))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(20)
        self.labelNombre.setFont(font)
        self.labelNombre.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.labelNombre.setObjectName("labelNombre")
        self.btnVer = QtWidgets.QPushButton(self.frame)
        self.btnVer.setEnabled(False)
        self.btnVer.setGeometry(QtCore.QRect(20, 460, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnVer.setFont(font)
        self.btnVer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVer.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: rgb(0, 191, 99);\n"
"}\n"
"QPushButton::hover {\n"
"    background: #4fa3a6 ;\n"
"}")
        self.btnVer.setCheckable(False)
        self.btnVer.setObjectName("btnVer")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(410, 120, 291, 301))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("imagenes/Logo-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.btnModificar = QtWidgets.QPushButton(self.frame)
        self.btnModificar.setEnabled(False)
        self.btnModificar.setGeometry(QtCore.QRect(160, 460, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnModificar.setFont(font)
        self.btnModificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificar.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: rgb(255, 222, 89);\n"
"}\n"
"QPushButton::hover {\n"
"    background: #ffde8c ;\n"
"}")
        self.btnModificar.setCheckable(False)
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtWidgets.QPushButton(self.frame)
        self.btnEliminar.setEnabled(False)
        self.btnEliminar.setGeometry(QtCore.QRect(360, 460, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(16)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminar.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: rgb(255, 49, 49);\n"
"}\n"
"QPushButton::hover {\n"
"    background: #ff9090 ;\n"
"}")
        self.btnEliminar.setCheckable(False)
        self.btnEliminar.setObjectName("btnEliminar")
        self.listaReservas = QtWidgets.QTableWidget(self.frame)
        self.listaReservas.setGeometry(QtCore.QRect(10, 100, 507, 271))
        self.listaReservas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listaReservas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listaReservas.setObjectName("listaReservas")
        self.listaReservas.setColumnCount(6)
        self.listaReservas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listaReservas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaReservas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaReservas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaReservas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaReservas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.listaReservas.setHorizontalHeaderItem(5, item)
        self.listaReservas.horizontalHeader().setDefaultSectionSize(84)
        self.listaReservas.horizontalHeader().setMinimumSectionSize(39)
        self.listaReservas.verticalHeader().setVisible(False)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.buscarNombre = QtWidgets.QLineEdit(self.frame)
        self.buscarNombre.setGeometry(QtCore.QRect(200, 400, 151, 31))
        self.buscarNombre.setMaxLength(324234322)
        self.buscarNombre.setObjectName("buscarNombre")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(540, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.btnBuscarF = QtWidgets.QPushButton(self.frame)
        self.btnBuscarF.setGeometry(QtCore.QRect(560, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnBuscarF.setFont(font)
        self.btnBuscarF.setStyleSheet("QPushButton {\n"
"    background: #4fa3a6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #74b6b6;\n"
"}\n"
"")
        self.btnBuscarF.setObjectName("btnBuscarF")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(560, 190, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clinica CVI"))
        self.labelTitulo.setText(_translate("mainWindow", "Lista Reservas del cliente:"))
        self.labelNombre.setText(_translate("mainWindow", "Nombre"))
        self.btnVer.setText(_translate("mainWindow", "Ver Reserva"))
        self.btnModificar.setText(_translate("mainWindow", "Modificar Reserva"))
        self.btnEliminar.setText(_translate("mainWindow", "Eliminar Reserva"))
        item = self.listaReservas.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Mascota"))
        item = self.listaReservas.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Tipo de Reserva"))
        item = self.listaReservas.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Fecha"))
        item = self.listaReservas.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Sala"))
        item = self.listaReservas.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "Hora"))
        item = self.listaReservas.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "Estado"))
        self.label_2.setText(_translate("mainWindow", "Buscar Nombre Mascota:"))
        self.label_4.setText(_translate("mainWindow", "Buscar por Fecha:"))
        self.btnBuscarF.setText(_translate("mainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
