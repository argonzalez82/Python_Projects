from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def Window():
    #command to connect pyqt with current OS
    app = QApplication(sys.argv)
    win = QMainWindow()

    #set the x,y positions and width, and height of windows
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("First PyQT Gui")

    #adding a label to window
    label = QtWidgets.QLabel(win)
    label.setText("First Dope Label")
    label.move(50, 50)



    #previous commands build the window in the background
    #win.show will display what is built.
    win.show()

    #exit command
    sys.exit(app.exec_())


Window()