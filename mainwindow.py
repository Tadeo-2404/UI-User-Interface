from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from Particulas import Particula
from AdminParticulas import AdminParticulas
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.admin = AdminParticulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarInicio_btn.clicked.connect(self.agregarInicio)
        self.ui.agregarFinal_btn.clicked.connect(self.agregarFinal)
        self.ui.mostrarTodo_btn.clicked.connect(self.mostrarTodo)
    
    @Slot()
    def agregarInicio(self) :
        id = self.ui.input_id.value()
        origen_x = self.ui.input_origenX.value()
        origen_y = self.ui.input_origenY.value()
        destino_x = self.ui.input_destinoX.value()
        destino_y = self.ui.input_destinoY.value()
        velocidad = self.ui.input_velocidad.value()
        red = self.ui.input_red.value()
        green = self.ui.input_green.value()
        blue = self.ui.input_blue.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregarInicio(particula)

    @Slot()
    def agregarFinal(self) :
        id = self.ui.input_id.value()
        origen_x = self.ui.input_origenX.value()
        origen_y = self.ui.input_origenY.value()
        destino_x = self.ui.input_destinoX.value()
        destino_y = self.ui.input_destinoY.value()
        velocidad = self.ui.input_velocidad.value()
        red = self.ui.input_red.value()
        green = self.ui.input_green.value()
        blue = self.ui.input_blue.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregarFinal(particula)

    @Slot()
    def mostrarTodo(self) :
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.admin))



