# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(429, 444)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.particular_container = QGroupBox(self.centralwidget)
        self.particular_container.setObjectName(u"particular_container")
        self.particular_container.setStyleSheet(u"background-color: rgb(187, 199, 195);\n"
"padding: 3px;")
        self.gridLayout = QGridLayout(self.particular_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_origenX = QLabel(self.particular_container)
        self.label_origenX.setObjectName(u"label_origenX")
        self.label_origenX.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.label_origenY = QLabel(self.particular_container)
        self.label_origenY.setObjectName(u"label_origenY")
        self.label_origenY.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.label_red = QLabel(self.particular_container)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setStyleSheet(u"text-transform: uppercase;\n"
"")

        self.gridLayout.addWidget(self.label_red, 6, 0, 1, 1)

        self.label_id = QLabel(self.particular_container)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.input_destinoY = QSpinBox(self.particular_container)
        self.input_destinoY.setObjectName(u"input_destinoY")
        self.input_destinoY.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_destinoY.setMaximum(500)

        self.gridLayout.addWidget(self.input_destinoY, 4, 1, 1, 1)

        self.input_origenY = QSpinBox(self.particular_container)
        self.input_origenY.setObjectName(u"input_origenY")
        self.input_origenY.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_origenY.setMaximum(500)

        self.gridLayout.addWidget(self.input_origenY, 2, 1, 1, 1)

        self.label_destinoX = QLabel(self.particular_container)
        self.label_destinoX.setObjectName(u"label_destinoX")
        self.label_destinoX.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.input_blue = QSpinBox(self.particular_container)
        self.input_blue.setObjectName(u"input_blue")
        self.input_blue.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_blue.setMaximum(255)

        self.gridLayout.addWidget(self.input_blue, 8, 1, 1, 1)

        self.agregarFinal_btn = QPushButton(self.particular_container)
        self.agregarFinal_btn.setObjectName(u"agregarFinal_btn")
        self.agregarFinal_btn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout.addWidget(self.agregarFinal_btn, 10, 0, 1, 2)

        self.label_green = QLabel(self.particular_container)
        self.label_green.setObjectName(u"label_green")
        self.label_green.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_green, 7, 0, 1, 1)

        self.input_velocidad = QSpinBox(self.particular_container)
        self.input_velocidad.setObjectName(u"input_velocidad")
        self.input_velocidad.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.input_velocidad, 5, 1, 1, 1)

        self.input_green = QSpinBox(self.particular_container)
        self.input_green.setObjectName(u"input_green")
        self.input_green.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_green.setMaximum(255)

        self.gridLayout.addWidget(self.input_green, 7, 1, 1, 1)

        self.agregarInicio_btn = QPushButton(self.particular_container)
        self.agregarInicio_btn.setObjectName(u"agregarInicio_btn")
        self.agregarInicio_btn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout.addWidget(self.agregarInicio_btn, 9, 0, 1, 2)

        self.label_destinoY = QLabel(self.particular_container)
        self.label_destinoY.setObjectName(u"label_destinoY")
        self.label_destinoY.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.input_id = QSpinBox(self.particular_container)
        self.input_id.setObjectName(u"input_id")
        self.input_id.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_id.setMaximum(500)

        self.gridLayout.addWidget(self.input_id, 0, 1, 1, 1)

        self.input_origenX = QSpinBox(self.particular_container)
        self.input_origenX.setObjectName(u"input_origenX")
        self.input_origenX.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_origenX.setMaximum(500)

        self.gridLayout.addWidget(self.input_origenX, 1, 1, 1, 1)

        self.input_red = QSpinBox(self.particular_container)
        self.input_red.setObjectName(u"input_red")
        self.input_red.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_red.setMaximum(255)

        self.gridLayout.addWidget(self.input_red, 6, 1, 1, 1)

        self.label_velocidad = QLabel(self.particular_container)
        self.label_velocidad.setObjectName(u"label_velocidad")
        self.label_velocidad.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.input_destinoX = QSpinBox(self.particular_container)
        self.input_destinoX.setObjectName(u"input_destinoX")
        self.input_destinoX.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_destinoX.setMaximum(500)

        self.gridLayout.addWidget(self.input_destinoX, 3, 1, 1, 1)

        self.label_blue = QLabel(self.particular_container)
        self.label_blue.setObjectName(u"label_blue")
        self.label_blue.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_blue, 8, 0, 1, 1)

        self.mostrarTodo_btn = QPushButton(self.particular_container)
        self.mostrarTodo_btn.setObjectName(u"mostrarTodo_btn")
        self.mostrarTodo_btn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"text-transform: uppercase;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 0, 0);\n"
"\n"
"")

        self.gridLayout.addWidget(self.mostrarTodo_btn, 11, 0, 1, 2)


        self.gridLayout_2.addWidget(self.particular_container, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(167, 16777215))

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 429, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.particular_container.setTitle(QCoreApplication.translate("MainWindow", u"UI-Particulas", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.agregarFinal_btn.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.agregarInicio_btn.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.mostrarTodo_btn.setText(QCoreApplication.translate("MainWindow", u"Mostrar todo", None))
        self.plainTextEdit.setPlainText("")
    # retranslateUi

