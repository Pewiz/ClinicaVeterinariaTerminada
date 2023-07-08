from PyQt5 import QtCore, QtGui, QtWidgets


class uiAdmin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 410)
        MainWindow.setMinimumSize(QtCore.QSize(602, 410))
        MainWindow.setMaximumSize(QtCore.QSize(602, 410))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bannerSup = QtWidgets.QLabel(MainWindow)
        self.bannerSup.setGeometry(QtCore.QRect(0, 0, 602, 90))
        self.bannerSup.setStyleSheet("background-color: transparent;")
        self.bannerSup.setText("")
        self.bannerSup.setPixmap(QtGui.QPixmap("imagenes/banner_admin.png").scaled(602, 90))
        
        self.btnRegresar = QtWidgets.QPushButton(MainWindow)
        self.btnRegresar.setGeometry(QtCore.QRect(15, 15, 55, 55))
        self.btnRegresar.setIcon((QtGui.QIcon("imagenes/boton_regresar.png")))
        self.btnRegresar.setIconSize(QtCore.QSize(55, 55))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 701, 411))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, -30, 291, 371))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(
            "imagenes\Logo-removebg-preview.png"))
        self.label_3.setObjectName("label_3")
        self.AGREGARUSUARIO = QtWidgets.QPushButton(self.frame)
        self.AGREGARUSUARIO.setGeometry(QtCore.QRect(30, 110, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.AGREGARUSUARIO.setFont(font)
        self.AGREGARUSUARIO.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AGREGARUSUARIO.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                           "border-radius: 5px;")
        self.AGREGARUSUARIO.setObjectName("AGREGARUSUARIO")
        self.BUSCARUSUARIO = QtWidgets.QPushButton(self.frame)
        self.BUSCARUSUARIO.setGeometry(QtCore.QRect(390, 110, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BUSCARUSUARIO.setFont(font)
        self.BUSCARUSUARIO.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUSCARUSUARIO.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                          "border-radius: 5px;")
        self.BUSCARUSUARIO.setObjectName("BUSCARUSUARIO")
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clinica CVI"))
        self.AGREGARUSUARIO.setText(
            _translate("MainWindow", "Agregar usuario"))
        self.BUSCARUSUARIO.setText(
            _translate("MainWindow", "Buscar usuario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiAdmin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())