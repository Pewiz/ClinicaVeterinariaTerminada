# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaElecMasc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class uiVentana(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(578, 418)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(578, 418))
        mainWindow.setMaximumSize(QtCore.QSize(578, 418))
        mainWindow.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 578, 418))
        self.frame.setMinimumSize(QtCore.QSize(578, 418))
        self.frame.setMaximumSize(QtCore.QSize(578, 418))
        self.frame.setSizeIncrement(QtCore.QSize(10000, 10000))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 100, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                 "border-radius: 5px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-10, -20, 721, 111))
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
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(120, 46, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 61, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(
            "imagenes\Atras.png"))
        self.label_3.setObjectName("label_3")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(130, 150, 281, 271))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(
            "imagenes\Logo-removebg-preview.png"))
        self.label_logo.setObjectName("label_logo")
        self.btnLista = QtWidgets.QPushButton(self.frame)
        self.btnLista.setEnabled(True)
        self.btnLista.setGeometry(QtCore.QRect(30, 210, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.btnLista.setFont(font)
        self.btnLista.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLista.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                    "border-radius: 5px;")
        self.btnLista.setCheckable(False)
        self.btnLista.setObjectName("btnLista")
        self.btnAgMasc = QtWidgets.QPushButton(self.frame)
        self.btnAgMasc.setEnabled(True)
        self.btnAgMasc.setGeometry(QtCore.QRect(340, 210, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.btnAgMasc.setFont(font)
        self.btnAgMasc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgMasc.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                     "border-radius: 5px;")
        self.btnAgMasc.setCheckable(False)
        self.btnAgMasc.setObjectName("btnAgMasc")
        self.label_logo.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.btnLista.raise_()
        self.btnAgMasc.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clinica CVI"))
        self.label.setText(_translate("mainWindow", "¿Que desea hacer?"))
        self.label_5.setText(_translate("mainWindow", "Mascotas"))
        self.btnLista.setText(_translate("mainWindow", "Lista mascota"))
        self.btnAgMasc.setText(_translate("mainWindow", "Agregar Mascota"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = uiVentana()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
