from PyQt5 import QtWidgets, QtCore


class ToDoApp(object):

    # Main window description

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 581)
        MainWindow.setStyleSheet("background-color: #2c2f33;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(10, 140, 120, 201))
        self.menu.setStyleSheet("background-color: #ffffff;")
        self.menu.setObjectName("menu")

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ToDoApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()