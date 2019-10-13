#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('mainwindow.ui', self)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())