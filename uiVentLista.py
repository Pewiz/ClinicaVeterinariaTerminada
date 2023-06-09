from PyQt5 import QtCore, QtGui, QtWidgets


class uiVentLista(object):
    def setupUi(self, mainWindow):
        mainWindow.setWindowIcon(QtGui.QIcon('Imagenes/logo.png'))
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 485)
        mainWindow.setMinimumSize(QtCore.QSize(700, 485))
        mainWindow.setMaximumSize(QtCore.QSize(700, 485))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
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
        self.label.setGeometry(QtCore.QRect(30, 90, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                 "border-radius: 5px;")
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
        self.label_9.setGeometry(QtCore.QRect(180, 40, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_9.setObjectName("label_9")
        self.btnAtras = QtWidgets.QPushButton(self.frame_2)
        self.btnAtras.setGeometry(QtCore.QRect(30, 35, 50, 50))
        self.btnAtras.setStyleSheet("\n"
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
        self.btnAtras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/boton_regresar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAtras.setIcon(icon)
        self.btnAtras.setIconSize(QtCore.QSize(50, 50))
        self.btnAtras.setObjectName("btnAtras")
        self.BtnVerDatos = QtWidgets.QPushButton(self.frame)
        self.BtnVerDatos.setEnabled(False)
        self.BtnVerDatos.setGeometry(QtCore.QRect(20, 440, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BtnVerDatos.setFont(font)
        self.BtnVerDatos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnVerDatos.setStyleSheet("background-color: rgb(0, 191, 99);\n"
                                       "border-radius: 5px;")
        self.BtnVerDatos.setCheckable(False)
        self.BtnVerDatos.setObjectName("BtnVerDatos")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(420, 120, 291, 301))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(
            "imagenes\Logo-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.btnAvanzar = QtWidgets.QPushButton(self.frame)
        self.btnAvanzar.setEnabled(True)
        self.btnAvanzar.setGeometry(QtCore.QRect(520, 440, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.btnAvanzar.setFont(font)
        self.btnAvanzar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAvanzar.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 5px;")
        self.btnAvanzar.setCheckable(False)
        self.btnAvanzar.setObjectName("btnAvanzar")
        self.BtnEditar = QtWidgets.QPushButton(self.frame)
        self.BtnEditar.setEnabled(False)
        self.BtnEditar.setGeometry(QtCore.QRect(160, 440, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BtnEditar.setFont(font)
        self.BtnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEditar.setStyleSheet("background-color: rgb(255, 222, 89);\n"
                                     "border-radius: 5px;")
        self.BtnEditar.setCheckable(False)
        self.BtnEditar.setObjectName("BtnEditar")
        self.BtnEliminar = QtWidgets.QPushButton(self.frame)
        self.BtnEliminar.setEnabled(False)
        self.BtnEliminar.setGeometry(QtCore.QRect(300, 440, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        self.BtnEliminar.setFont(font)
        self.BtnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEliminar.setStyleSheet("background-color: rgb(255, 49, 49);\n"
                                       "border-radius: 5px;")
        self.BtnEliminar.setCheckable(False)
        self.BtnEliminar.setObjectName("BtnEliminar")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 401, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(270, 400, 151, 31))
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName("lineEdit")
        self.btnAgregarM = QtWidgets.QPushButton(self.frame)
        self.btnAgregarM.setEnabled(True)
        self.btnAgregarM.setGeometry(QtCore.QRect(520, 390, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.btnAgregarM.setFont(font)
        self.btnAgregarM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgregarM.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                       "border-radius: 5px;")
        self.btnAgregarM.setCheckable(False)
        self.btnAgregarM.setObjectName("btnAgregarM")
        self.frame_2.raise_()
        self.label.raise_()
        self.BtnVerDatos.raise_()
        self.label_logo.raise_()
        self.btnAvanzar.raise_()
        self.BtnEditar.raise_()
        self.BtnEliminar.raise_()
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.btnAgregarM.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clinica CVI"))
        self.label.setText(_translate("mainWindow", "Clientes Agregados"))
        self.label_9.setText(_translate("mainWindow", "      Lista Clientes"))
        self.BtnVerDatos.setText(_translate("mainWindow", "Ver Datos"))
        self.btnAvanzar.setText(_translate("mainWindow", "Lista mascota"))
        self.BtnEditar.setText(_translate("mainWindow", "Editar"))
        self.BtnEliminar.setText(_translate("mainWindow", "Eliminar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Rut"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Nombres"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Apellido Paterno"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Apellido Materno"))
        self.label_2.setText(_translate(
            "mainWindow", "Buscar Rut (Sin digito Verificador):"))
        self.btnAgregarM.setText(_translate("mainWindow", "Agregar mascota"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = uiVentLista()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
