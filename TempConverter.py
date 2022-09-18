# Preferences
# Projects
# Interpreter
# Remove: PyQt5, -sip, -stubs
# Add: PyQt5 Version 5.11.3

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Conversions import TempConverter


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("mainwindow.ui", self)
        self.build_ui()

    def build_ui(self):
        self.ui.btn_convert.clicked.connect(self.handle_click)
        conversions = ["Fahrenheit to Celsius", "Celsius to Fahrenheit"]
        self.ui.cmb_conv_type.addItems(conversions)

    def handle_click(self):
        temp = float(self.ui.le_input.text())
        if self.ui.cmb_conv_type.currentIndex() == 0:
            result = str(round(TempConverter.f_to_c(temp), 1)) + "C"
        if self.ui.cmb_conv_type.currentIndex() == 1:
            result = str(round(TempConverter.c_to_f(temp), 1)) + "F"
        self.ui.lbl_result.setText(result)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec())
