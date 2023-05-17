from sys import argv, exit
from GUI.window import MainWindow
from PyQt6 import QtWidgets


def main():
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
