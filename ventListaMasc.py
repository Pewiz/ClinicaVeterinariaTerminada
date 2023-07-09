import csv
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
from uiVentListaMasc import uiVent
from ManejoArchivo import GestionArchivo
import ventElecMasc
import ventanaLista
import ventanaModMascota
import ventVerDatosM


class ventListaMascota(QMainWindow):
    def __init__(self, rut, flag):
        super().__init__()
        self.rut = rut
        self.flag = flag
        self.poss = 0
        self.mascotaSelecc = -1
        self.vent = uiVent()
        self.vent.setupUi(self)
        self.vent.btnAtras.clicked.connect(lambda: self.atras(self.flag))
        self.tablaMasc = self.vent.tableWidget
        self.vent.eliminar.clicked.connect(lambda: self.eliminar())
        self.vent.editar.clicked.connect(self.editar)
        self.ventVer = ventVerDatosM.ventanaVerDatos(
            self.poss, self.flag, self.rut)
        self.vent.verDatos.clicked.connect(lambda: self.verD(self.ventVer))
        self.tablaMasc.itemSelectionChanged.connect(self.seleccFila)

    def atras(self, fla):
        if fla == 0:
            vent = ventElecMasc.ventElec(self.rut)
            vent.show()
            self.hide()
        elif fla == 1:
            ventanaLista.ventanaLista().show()
            self.hide()

    def actualizar(self):
        masc = []
        with open('ArchivosCSV/mascotas.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            for l in lector:
                if l[0] == self.rut:
                    masc.append(l)

        contFilas = len(masc)
        self.tablaMasc.setRowCount(contFilas)
        for i, mascota in enumerate(masc):
            nombre = qtw.QTableWidgetItem(mascota[1])
            self.tablaMasc.setItem(i, 0, nombre)

            especie = qtw.QTableWidgetItem(mascota[2])
            self.tablaMasc.setItem(i, 1, especie)
            
            sexo = qtw.QTableWidgetItem(mascota[5])
            self.tablaMasc.setItem(i, 2, sexo)
            
            peso = qtw.QTableWidgetItem(mascota[6]+" Kg")
            self.tablaMasc.setItem(i, 3, peso)
        nombre = ""
        with open('ArchivosCSV/clientes.csv', 'r', encoding="latin1") as r:
            l = csv.reader(r, delimiter=",")
            next(l)
            for lis in l:
                if lis[0] == str(self.rut):
                    nombre = str(lis[1])
        self.vent.nCliente.setText(nombre)

    def seleccFila(self):
        self.fila = self.tablaMasc.selectedIndexes()
        if self.fila:
            self.vent.verDatos.setEnabled(True)
            self.vent.editar.setEnabled(True)
            self.vent.eliminar.setEnabled(True)
            self.mascotaSelecc = self.tablaMasc.currentRow()
        else:
            self.vent.verDatos.setEnabled(False)
            self.vent.editar.setEnabled(False)
            self.vent.eliminar.setEnabled(False)

    def eliminar(self):
        k = 0
        j = self.buscar(k)
        GestionArchivo.eliminar("ArchivosCSV/mascotas.csv", j)
        self.actualizar()

    def buscar(self, pos):
        with open('ArchivosCSV/mascotas.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                pos = (pos + 1)
                if l[0] == self.rut:
                    i = (i + 1)
                    if (i == self.mascotaSelecc+1):
                        return pos

    def editar(self):
        k = 0
        self.poss = self.buscar(k)
        self.vent.posicion = self.poss
        self.vent.flag = self.flag
        self.vent.rut = self.rut
        ventanaModMascota.ventanaModifMascota(self.poss, self.flag, self.rut).show()
        self.hide()

    def verD(self, vent):
        k = 0
        self.poss = self.buscar(k)
        self.ventVer.posicion = self.poss
        self.ventVer.flag = self.flag
        self.ventVer.rut = self.rut
        vent.actualizar()
        vent.show()
        self.hide()
