from PyQt5.QtWidgets import QMainWindow
from uiVentElecMasc import uiVentana
import ventanaMascota
import ventListaMasc

class ventElec(QMainWindow):
    def __init__(self, rut):
        super().__init__()
        self.rut = rut
        rt = None
        self.vent = uiVentana()
        self.vent.setupUi(self)
        self.ventan = ventListaMasc.ventListaMascota(rt, 0)
        self.vent.btnLista.clicked.connect(lambda: self.irALista(self.ventan))
        self.ventanaDatos = ventanaMascota.ventanaMascota(self.rut, 0)
        self.vent.btnAgMasc.clicked.connect(lambda: self.irADatos(self.ventanaDatos))

    def irALista(self, v):
        self.ventan.rut = self.rut
        v.actualizar()
        v.show()
        self.hide()
        
    def irADatos(self, ve):
        self.ventanaDatos.rut = self.rut
        ve.show()
        self.hide()
