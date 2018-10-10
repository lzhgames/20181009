# -*- coding: utf-8 -*-
# __author__ = 'Lu'
import sys
from PyQt5.QtWidgets import QWidget,QApplication
from myui import Ui_Form
import cgitb
cgitb.enable()

class mywin(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=='__main__':
    app=QApplication(sys.argv)
    myshow=mywin()
    myshow.show()
    sys.exit(app.exec_())