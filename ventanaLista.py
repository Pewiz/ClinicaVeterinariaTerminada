import csv
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
from uiVentLista import uiVentLista
from ManejoArchivo import GestionArchivo
import ventanaAdministracion
import ventanaModificar
import ventanaCarga
import ventListaMasc
import ventanaMascota
import ventVerDatosC


class ventanaLista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clienteSelecc = -1
        self.ventanaModificar = None
        #tabla
        self.ui = uiVentLista()
        self.ui.setupUi(self)
        
        self.ui.btnAvanzar.setEnabled(False)
        self.ui.btnAgregarM.setEnabled(False)
        self.ui.btnAtras.clicked.connect(lambda: self.volver())
        self.vent = ventanaModificar.ventanaModificar(self.clienteSelecc)
        self.ventV = ventVerDatosC.ventanaVerDatos(self.clienteSelecc)
        self.ui.BtnEditar.clicked.connect(lambda: self.ventanaMod(self.vent))
        self.ui.BtnVerDatos.clicked.connect(lambda: self.ventanaVer(self.ventV))
        self.ui.BtnEliminar.clicked.connect(lambda: self.eliminar())
        self.rt = ""
        self.ventan = ventListaMasc.ventListaMascota(self.rt, 1)
        self.ventAgMascota = ventanaMascota.ventanaMascota(self.rt, 1)
        self.ui.btnAvanzar.clicked.connect(lambda: self.avanzar(self.ventan))
        self.ui.btnAgregarM.clicked.connect(lambda: self.agregar(self.ventAgMascota))
        self.tabla = self.ui.tableWidget

        with open('TPAP-Clinica/clientes.csv') as f:
            lector = csv.reader(f)
            next(lector)
            self.clientes = [row for row in lector]

        contFilas = len(self.clientes)
        self.tabla.setRowCount(contFilas)

        for i, cliente in enumerate(self.clientes):
            rut = qtw.QTableWidgetItem(cliente[0])
            self.tabla.setItem(i, 0, rut)

            nombre = qtw.QTableWidgetItem(cliente[1])
            self.tabla.setItem(i, 1, nombre)

            apellidoPaterno = qtw.QTableWidgetItem(cliente[2])
            self.tabla.setItem(i, 2, apellidoPaterno)
            
            apellidoMaterno = qtw.QTableWidgetItem(cliente[3])
            self.tabla.setItem(i, 3, apellidoMaterno)

        #buscador de rut    
        self.onlyInt = QtGui.QIntValidator()
        self.ui.lineEdit.setValidator(self.onlyInt)
        self.ui.lineEdit.textChanged.connect(self.buscador)
        
        #seleccion de un cliente
        self.tabla.itemSelectionChanged.connect(self.seleccFila)
        
    def avanzar(self, vent):
        self.ventan.rut = self.rt
        vent.actualizar()
        vent.show()
        self.hide()

    def agregar(self, vent):
        self.ventAgMascota.rut = self.rt
        vent.show()
        self.hide()
        
    def volver(self):
        ventanaAdministracion.ventanaAdmin().show()
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
            self.ui.btnAvanzar.setEnabled(True)
            self.ui.btnAgregarM.setEnabled(True)
            self.clienteSelecc = self.tabla.currentRow()
            self.buscarRut()
        else:
            self.ui.btnAvanzar.setEnabled(False)
            self.ui.BtnVerDatos.setEnabled(False)
            self.ui.BtnEditar.setEnabled(False)
            self.ui.BtnEliminar.setEnabled(False)
            self.ui.btnAgregarM.setEnabled(False)
            
    def buscarRut(self):
        with open('TPAP-Clinica/clientes.csv', 'r', encoding="ISO 8859-1") as r:
                l = csv.reader(r, delimiter=",")
                next(l)
                i = 0
                for lis in l:
                    i = (i + 1)
                    if i == (self.clienteSelecc+1):
                        self.rt = lis[0]
            
    def eliminar(self):
        for i, cliente in enumerate(self.clientes):
            if i == self.clienteSelecc:
                self.rut = cliente[0]
        with open('TPAP-Clinica/mascotas.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                if l[0] == self.rut:
                    i = (i + 1)
        for h in range(i):
            k = 0
            j = self.buscar(k)
            GestionArchivo.eliminar("TPAP-Clinica/mascotas.csv", j)
            
        GestionArchivo.eliminar("TPAP-Clinica/clientes.csv", self.clienteSelecc + 1)
        with open('TPAP-Clinica/clientes.csv') as f:
            lector = csv.reader(f)
            clientes = [row for row in lector]
        contFilas = len(clientes)
        if contFilas == 1:
            ventanaAdministracion.ventanaAdmin().show()
            self.close()
        else:
            ventanaCarga.window().show()
            self.close()
    
    def buscar(self, pos):
        with open('TPAP-Clinica/mascotas.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            for l in lector:
                pos = (pos + 1)
                if l[0] == self.rut:
                    return pos
            
    
    def ventanaMod(self,vent):
        self.vent.cont = self.clienteSelecc
        vent.show()
        self.hide()

    def ventanaVer(self,vent):
        self.ventV.cont = self.clienteSelecc
        vent.actualizar()
        vent.show()
        self.hide()