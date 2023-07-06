import csv
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
from uiVentListaUsuarios import uiVentLista
from ManejoArchivo import GestionArchivo
import ventanaAdministracionUsuario
import ventanaModificarUsuario
import ventanaCargaUsuario
import ventVerDatosU
import csv


class ventanaLista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.usuarioSelecc = -1
        self.ventanaModificarUsuario = None
        # tabla
        self.ui = uiVentLista()
        self.ui.setupUi(self)

        self.ui.btnAtras.clicked.connect(lambda: self.volver())
        self.vent = ventanaModificarUsuario.ventanaModificarUsuario(self.usuarioSelecc)
        self.ventV = ventVerDatosU.ventanaVerDatos(self.usuarioSelecc)
        self.ui.BtnEditar.clicked.connect(lambda: self.ventanaMod(self.vent))
        self.ui.BtnVerDatos.clicked.connect(
            lambda: self.ventanaVer(self.ventV))
        self.rt = ""
        self.tabla = self.ui.tableWidget

        with open('usuarios.csv') as f:
            lector = csv.reader(f)
            next(lector)
            self.usuarios = [row for row in lector]

        contFilas = len(self.usuarios)
        self.tabla.setRowCount(contFilas)
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderItem(4, qtw.QTableWidgetItem("Cargo"))
        self.tabla.setHorizontalHeaderItem(5, qtw.QTableWidgetItem("Experiencia"))

        for i, usuario in enumerate(self.usuarios):
            rut = qtw.QTableWidgetItem(usuario[0])
            self.tabla.setItem(i, 0, rut)

            nombre = qtw.QTableWidgetItem(usuario[1])
            self.tabla.setItem(i, 1, nombre)

            apellidoPaterno = qtw.QTableWidgetItem(usuario[2])
            self.tabla.setItem(i, 2, apellidoPaterno)

            apellidoMaterno = qtw.QTableWidgetItem(usuario[3])
            self.tabla.setItem(i, 3, apellidoMaterno)
            
            cargo = qtw.QTableWidgetItem(usuario[9])
            self.tabla.setItem(i, 4, cargo)
            
            experiencia = qtw.QTableWidgetItem(usuario[10])
            self.tabla.setItem(i, 5, experiencia)

        # buscador de rut
        self.onlyInt = QtGui.QIntValidator()
        self.ui.lineEdit.setValidator(self.onlyInt)
        self.ui.lineEdit.textChanged.connect(self.buscador)

        # seleccion de un usuario
        self.tabla.itemSelectionChanged.connect(self.seleccFila)

    def agregar(self, vent):
        self.ventAgMascota.rut = self.rt
        vent.show()
        self.hide()

    def volver(self):
        ventanaAdministracionUsuario.ventanaAdminUsuario().show()
        self.hide()

    def buscador(self, texto):
        for row in range(self.tabla.rowCount()):
            rut = self.tabla.item(row, 0).text()
            if texto in rut:
                self.tabla.setRowHidden(row, False)
            else:
                self.tabla.setRowHidden(row, True)

    def seleccFila(self):
        self.fila = self.tabla.selectedIndexes()
        if self.fila:
            self.ui.BtnVerDatos.setEnabled(True)
            self.ui.BtnEditar.setEnabled(True)
            self.ui.BtnEliminar.setEnabled(True)
            self.usuarioSelecc = self.tabla.currentRow()
            self.buscarRut()
        else:
            self.ui.BtnVerDatos.setEnabled(False)
            self.ui.BtnEditar.setEnabled(False)
            self.ui.BtnEliminar.setEnabled(False)

    def buscarRut(self):
        with open('usuarios.csv', 'r', encoding="ISO 8859-1") as r:
            l = csv.reader(r, delimiter=",")
            next(l)
            i = 0
            for lis in l:
                i = (i + 1)
                if i == (self.usuarioSelecc+1):
                    self.rt = lis[0]

    def eliminar(self):
        for i, usuario in enumerate(self.usuarios):
            if i == self.usuarioSelecc:
                self.rut = usuario[0]
        with open('mascotas.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                if l[0] == self.rut:
                    i = (i + 1)
        for h in range(i):
            k = 0
            j = self.buscar(k)
            GestionArchivo.eliminar("mascotas.csv", j)

        GestionArchivo.eliminar(
            "usuarios.csv", self.usuarioSelecc + 1)
        with open('usuarios.csv') as f:
            lector = csv.reader(f)
            usuarios = [row for row in lector]
        contFilas = len(usuarios)
        if contFilas == 1:
            ventanaAdministracionUsuario.ventanaAdmin().show()
            self.close()
        else:
            ventanaCargaUsuario.window().show()
            self.close()

    def ventanaMod(self, vent):
        self.vent.cont = self.usuarioSelecc
        vent.show()
        self.hide()

    def ventanaVer(self, vent):
        self.ventV.cont = self.usuarioSelecc
        vent.actualizar()
        vent.show()
        self.hide()
