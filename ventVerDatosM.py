import csv
from PyQt5.QtWidgets import QMainWindow
from uiVentVerDatosM import uiVerDatos
import ventListaMasc
import ventanaAdministracion


class ventanaVerDatos(QMainWindow):
    def __init__(self, posicion, flag, rut):
        super().__init__()
        self.posicion = posicion
        self.flag = flag
        self.rut = rut
        self.ventanaUi = uiVerDatos()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.btnLista.clicked.connect(lambda: self.atras(self.flag))
        self.ventanaUi.btnAdmin.clicked.connect(lambda: self.menuP())
        
    def actualizar(self):
        with open('ArchivosCSV/mascotas.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                i = (i+1)
                if i == (self.posicion):
                    mascota = l
        self.ventanaUi.labelRut.setText(str(mascota[0]))
        self.ventanaUi.labelNombre.setText(str(mascota[1]))
        self.ventanaUi.labelEspecie.setText(str(mascota[2]))
        self.ventanaUi.labelRaza.setText(str(mascota[3]))
        self.ventanaUi.labelFecha.setText(str(mascota[4]))
        self.ventanaUi.labelSexo.setText(str(mascota[5]))
        self.ventanaUi.labelPeso.setText(str(mascota[6]) + " Kg.")
        self.ventanaUi.labelTamano.setText(str(mascota[7]))
        self.ventanaUi.labelVolumen.setText(str(mascota[8]))
        
    
    def atras(self, fla):
        vent = ventListaMasc.ventListaMascota(self.rut, fla)
        vent.actualizar()
        vent.show()
        self.hide()
    
    def menuP(self):
        ventanaAdministracion.ventanaAdmin().show()
        self.close()
