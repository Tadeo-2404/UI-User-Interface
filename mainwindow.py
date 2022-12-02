from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QApplication
from algoritmos import distancia_euclidiana, get_puntos, puntos_mas_cercanos
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from Particulas import Particula
from PySide2.QtGui import QPen, QColor, QTransform
from AdminParticulas import Admin
import json
import sys
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.admin = Admin()
        self.scene =  QGraphicsScene()
        
        self.ui.agregarInicio_btn.clicked.connect(self.click_agregar_inicio)
        self.ui.agregarFinal_btn.clicked.connect(self.click_agregar_final)
        self.ui.mostrarTodo_btn.clicked.connect(self.click_mostrar)
        self.ui.btn_limpiar.clicked.connect(self.click_limpiar)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)
        self.ui.btn_mostrar.clicked.connect(self.mostrar_tabla)
        self.ui.btn_buscar.clicked.connect(self.buscar_id)
        self.ui.btn_limpiar.clicked.connect(self.borrar)
        self.ui.btn_dibujar.clicked.connect(self.dibujar)

        self.ui.graphicsView.setScene(self.scene)
        self.ui.btnSort_id.clicked.connect(self.ordenar_id)
        self.ui.btnSort_velocidad.clicked.connect(self.ordenar_velocidad)
        self.ui.btnSort_distancia.clicked.connect(self.ordenar_distancia)

        self.ui.actionAlgoritmos.triggered.connect(self.mostrar_puntos)
        self.ui.actionPuntos_Cercanos.triggered.connect(self.mostrar_puntos_cercanos)

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)

    @Slot()
    def click_agregar_inicio(self):
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
        self.admin.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
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
        self.admin.agregar_final(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.admin))

    @Slot()
    def click_limpiar(self):
        self.ui.plainTextEdit.clear()

    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'    
        )[0]
        if self.admin.abrir(ubicacion):
            QMessageBox.information(
                self,
                'Exito',
                'Se pudo abrir el archivo ' + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                'Error',
                'No se pudo abrir el archivo ' + ubicacion
            )

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.admin.guardar(ubicacion):
            QMessageBox.information(
                self,
                'Exito',
                'Se pudo crear el archivo ' + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                'Error',
                'No se pudo crear el archivo ' + ubicacion
            )
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.table.setColumnCount(10) #Define las columnas para la table
        headers = ["ID","Origen X","Origen Y","Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"] #Preparamos el nombre de las columnas para la table
        self.ui.table.setHorizontalHeaderLabels(headers) #Pasamos los nombres por parametro para cambiarlos
        self.ui.table.setRowCount(len(self.admin))

        row = 0
        for particula in self.admin.particulas: # Tenemos que hacer los objetos iterables crear metodo __next__
            id_widget = QTableWidgetItem(str(particula.id)) #Por cada vuelo colocaremos el nombre del vuelo
            origenx_widget = QTableWidgetItem(str(particula.origen_x))
            origeny_widget = QTableWidgetItem(str(particula.origen_y))
            destinox_widget = QTableWidgetItem(str(particula.destino_x))
            destinoy_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.table.setItem(row, 0 , id_widget)
            self.ui.table.setItem(row, 1 , origenx_widget)
            self.ui.table.setItem(row, 2 , origeny_widget)
            self.ui.table.setItem(row, 3 , destinox_widget)
            self.ui.table.setItem(row, 4 , destinoy_widget)
            self.ui.table.setItem(row, 5 , velocidad_widget)
            self.ui.table.setItem(row, 6 , red_widget)
            self.ui.table.setItem(row, 7 , green_widget)
            self.ui.table.setItem(row, 8 , blue_widget)
            self.ui.table.setItem(row, 9 , distancia_widget)
            

            row += 1
    
    @Slot()
    def buscar_id(self):
        id = self.ui.input_buscar.text()
        encontrado = False
        for particula in self.admin.particulas:
            if id == str(particula.id):
                encontrado = True
                self.ui.table.clear()
                self.ui.table.setColumnCount(10) 
                headers = ["ID","Origen X","Origen Y","Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.table.setHorizontalHeaderLabels(headers) 
                self.ui.table.setRowCount(1)
                
                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origen_x))
                origeny_widget = QTableWidgetItem(str(particula.origen_y))
                destinox_widget = QTableWidgetItem(str(particula.destino_x))
                destinoy_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.table.setItem(0, 0 , id_widget)
                self.ui.table.setItem(0, 1 , origenx_widget)
                self.ui.table.setItem(0, 2 , origeny_widget)
                self.ui.table.setItem(0, 3 , destinox_widget)
                self.ui.table.setItem(0, 4 , destinoy_widget)
                self.ui.table.setItem(0, 5 , velocidad_widget)
                self.ui.table.setItem(0, 6 , red_widget)
                self.ui.table.setItem(0, 7 , green_widget)
                self.ui.table.setItem(0, 8 , blue_widget)
                self.ui.table.setItem(0, 9 , distancia_widget)

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f"La particula con el identificador '{id}' no fue encontrado"
            )

    @Slot() 
    def borrar(self):
        print("Limpiar")
        self.scene.clear()

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.admin.particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r,g,b)
            pen.setColor(color)

            x_origen = particula.origen_x
            y_origen = particula.origen_y
            x_destino = particula.destino_x
            y_destino = particula.destino_y

            self.scene.addEllipse(x_origen, y_origen, 10, 10, pen)
            self.scene.addEllipse(x_destino, y_destino, 10, 10, pen)
            self.scene.addLine(x_origen + 5, y_origen + 5, x_destino + 5, y_destino + 5, pen)

        grafo = dict()

        for particula in self.admin:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)

            x_1 = particula.origen_x
            y_1 = particula.origen_y            
            x_2 = particula.destino_x
            y_2 = particula.destino_y
            
            distancia = distancia_euclidiana(x_1,y_1,x_2,y_2)

            key = str(origen)
            if key in grafo:
                grafo[key].append([str(destino),distancia])
            else:
                grafo[key] = [[str(destino),distancia]]

            key = str(destino)
            if key in grafo:
                grafo[key].append([str(origen),distancia])
            else:
                grafo[key] = [[str(origen),distancia]]

        with open('dict.json', 'w') as file:
            #Serialización de los datos en el archivo
            json.dump(grafo, file, indent=3)
        
        cadena=""
        for key, value in grafo.items():
            cadena += str(key)+"--> "+str(value)+"\n"

        print(cadena)
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(cadena)


    @Slot()
    def ordenar_id(self):
        self.admin.particulas.sort(key = lambda particula: particula.id)
        self.ui.plainTextEditSort.clear()
        self.ui.plainTextEditSort.insertPlainText(str(self.admin))
        
    @Slot()
    def ordenar_distancia(self):
        self.admin.particulas.sort(key = lambda particula: particula.distancia, reverse = True)
        self.ui.plainTextEditSort.clear()
        self.ui.plainTextEditSort.insertPlainText(str(self.admin))
            
    @Slot()
    def ordenar_velocidad(self):
        self.admin.particulas.sort(key = lambda particula: particula.velocidad)
        self.ui.plainTextEditSort.clear()
        self.ui.plainTextEditSort.insertPlainText(str(self.admin))

    @Slot()
    def mostrar_puntos(self):
        pen = QPen()
        pen.setWidth(2)
        self.puntos = get_puntos(self.admin)
        for p,r,g,b in self.puntos:
            color = QColor(r,g,b)
            pen.setColor(color)

            x = p[0]
            y = p[1]

            self.scene.addEllipse(x,y,10,10,pen)

    @Slot()
    def mostrar_puntos_cercanos(self):
        pen = QPen()
        pen.setWidth(2)
        resultado = puntos_mas_cercanos(self.puntos)
        for punto1,punto2,r,g,b in resultado:
            color = QColor(r,g,b)
            pen.setColor(color)
            
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]

            self.scene.addLine(x1+5,y1+5,x2+5,y2+5,pen)
    
