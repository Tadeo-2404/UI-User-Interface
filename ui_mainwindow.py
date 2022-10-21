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
        MainWindow.resize(382, 336)
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
        self.input_destinoX = QSpinBox(self.particular_container)
        self.input_destinoX.setObjectName(u"input_destinoX")
        self.input_destinoX.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_destinoX.setMaximum(500)

        self.gridLayout.addWidget(self.input_destinoX, 0, 1, 1, 1)

        self.input_green = QSpinBox(self.particular_container)
        self.input_green.setObjectName(u"input_green")
        self.input_green.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_green.setMaximum(255)

        self.gridLayout.addWidget(self.input_green, 4, 1, 1, 1)

        self.label_3 = QLabel(self.particular_container)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.input_velocidad = QSpinBox(self.particular_container)
        self.input_velocidad.setObjectName(u"input_velocidad")
        self.input_velocidad.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.input_velocidad, 2, 1, 1, 1)

        self.label_2 = QLabel(self.particular_container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.particular_container)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"text-transform: uppercase;\n"
"")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.input_red = QSpinBox(self.particular_container)
        self.input_red.setObjectName(u"input_red")
        self.input_red.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_red.setMaximum(255)

        self.gridLayout.addWidget(self.input_red, 3, 1, 1, 1)

        self.label = QLabel(self.particular_container)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.input_blue = QSpinBox(self.particular_container)
        self.input_blue.setObjectName(u"input_blue")
        self.input_blue.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_blue.setMaximum(255)

        self.gridLayout.addWidget(self.input_blue, 5, 1, 1, 1)

        self.label_5 = QLabel(self.particular_container)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.input_destinoY = QSpinBox(self.particular_container)
        self.input_destinoY.setObjectName(u"input_destinoY")
        self.input_destinoY.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"border: none;")
        self.input_destinoY.setMaximum(500)

        self.gridLayout.addWidget(self.input_destinoY, 1, 1, 1, 1)

        self.label_6 = QLabel(self.particular_container)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"text-transform: uppercase;")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.particular_container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 382, 22))
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
    # retranslateUi

