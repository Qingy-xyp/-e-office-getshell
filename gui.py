#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import dialog
from PyQt5.QtGui import QIcon




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainw = QMainWindow()
    ui = dialog.Ui_dialog()
    ui.setupUi(mainw)
    app.setWindowIcon(QIcon('1.png'))
    mainw.show()
    sys.exit(app.exec_())








