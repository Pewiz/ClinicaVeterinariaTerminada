import PyQt5.QtWidgets as qtw
import ventanaListaUsuario

class window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clinica CVI")
        self.setLayout(qtw.QVBoxLayout())
        self.hide()
        ventanaListaUsuario.ventanaLista().show()