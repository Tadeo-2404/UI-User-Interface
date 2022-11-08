from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
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

        self.ui.actionAbrir.triggered.connect(self.abrirArchivoJSON)
        self.ui.actionGuardar.triggered.connect(self.guardarArchivoJSON)

        self.ui.btn_mostrar.clicked.connect(self.mostrarTabla)
        self.ui.btn_buscar.clicked.connect(self.buscarParticula)

        self.ui.btn_dibujar.clicked.connect(self.dibujar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    @Slot()
    def dibujar(self):
        lapiz = QPen()
        lapiz.setWidth(2)

        for particula in self.admin:
            rojo = particula.getRed
            green = particula.getGreen
            blue = particula.getBlue
            destino_x = particula.getDestinoX
            destino_y = particula.getDestinoY
            origen_x = particula.getOrigenX
            origen_y = particula.getOrigenY
            color = QColor(rojo, green, blue)
            lapiz.setColor(color)
            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, lapiz)

    @Slot()
    def limpiar(self):
        print('Limpiar')

    @Slot()
    def buscarParticula(self):
        id = self.ui.input_buscar.text()
        encontrado = False
        for particula in self.admin:
            if(id == str(particula.getID)):
                self.ui.table.clear()
                id = QTableWidgetItem(str(particula.getID))
                origen_x = QTableWidgetItem(str(particula.getOrigenX))
                origen_y = QTableWidgetItem(str(particula.getOrigenY))
                destino_x = QTableWidgetItem(str(particula.getDestinoX))
                destino_y = QTableWidgetItem(str(particula.getDestinoY))
                velocidad = QTableWidgetItem(str(particula.getVelocidad))
                red = QTableWidgetItem(str(particula.getRed))
                green = QTableWidgetItem(str(particula.getGreen))
                blue = QTableWidgetItem(str(particula.getBlue))
                distancia = QTableWidgetItem(str(particula.getDistancia))
                self.ui.table.setItem(0, 0, id)
                self.ui.table.setItem(0, 1, origen_x)
                self.ui.table.setItem(0, 2, origen_y)
                self.ui.table.setItem(0, 3, destino_x)
                self.ui.table.setItem(0, 4, destino_y)
                self.ui.table.setItem(0, 5, velocidad)
                self.ui.table.setItem(0, 6, red)
                self.ui.table.setItem(0, 7, green)
                self.ui.table.setItem(0, 8, blue)
                self.ui.table.setItem(0, 9, distancia)
                encontrado = True
            if(not encontrado):
                QMessageBox.warning(
                    self, 
                    'Atencion',
                    'Particula no encontrada'
                )

    @Slot()
    def mostrarTabla(self):
        self.ui.table.setColumnCount(10)
        headers = ["ID", "OrigenX", "OrigenY", "DestinoX", "DestinoY", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers)
        self.ui.table.setRowCount((len(self.admin)))

        row = 0
        for particula in self.admin:
            id = QTableWidgetItem(str(particula.getID))
            origen_x = QTableWidgetItem(str(particula.getOrigenX))
            origen_y = QTableWidgetItem(str(particula.getOrigenY))
            destino_x = QTableWidgetItem(str(particula.getDestinoX))
            destino_y = QTableWidgetItem(str(particula.getDestinoY))
            velocidad = QTableWidgetItem(str(particula.getVelocidad))
            red = QTableWidgetItem(str(particula.getRed))
            green = QTableWidgetItem(str(particula.getGreen))
            blue = QTableWidgetItem(str(particula.getBlue))
            distancia = QTableWidgetItem(str(particula.getDistancia))

            self.ui.table.setItem(row, 0, id)
            self.ui.table.setItem(row, 1, origen_x)
            self.ui.table.setItem(row, 2, origen_y)
            self.ui.table.setItem(row, 3, destino_x)
            self.ui.table.setItem(row, 4, destino_y)
            self.ui.table.setItem(row, 5, velocidad)
            self.ui.table.setItem(row, 6, red)
            self.ui.table.setItem(row, 7, green)
            self.ui.table.setItem(row, 8, blue)
            self.ui.table.setItem(row, 9, distancia)
            row += 1

    @Slot()
    def abrirArchivoJSON(self):
        ubicacion = QFileDialog.getOpenFileName(
            self, 
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        self.admin.abrirArchivo(ubicacion)

    @Slot()
    def guardarArchivoJSON(self):
        ubicacion = QFileDialog.getSaveFileName(
            self, 
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        self.admin.guardarArchivo(ubicacion)
    
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



