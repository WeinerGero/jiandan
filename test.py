import typing
from main import main


import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog



# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Jiandan")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    def UiComponents(self):
        # creating a push button
        button = QPushButton("Выбрать", self)

        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)

        # adding action to a button
        button.clicked.connect(self.choose_file)

    def choose_file(self):
        res = QFileDialog.getOpenFileName(window, 'Open File', '', '')
        print(res)
        main(res[0])


# create pyqt5 app
App = QApplication([])

# create the instance of our Window
window = MainWindow()

# start the app
sys.exit(App.exec())
