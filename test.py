import webbrowser
import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt6.QtGui import QFont

Form, Window = uic.loadUiType("GUI/interface.ui")

class MainWindow(QMainWindow, Form):
    icon_filenames = ['iconizer-settings.svg', 'iconizer-alert-circle.svg', 'iconizer-help-circle.svg', 'iconizer-x.svg', 'iconizer-play.svg']
    buttons_names = ['settingButton', 'reportButton', 'helpButton', 'exitButton', 'PushButtonStart']
    font = QFont()
    font.setPointSize(16)
    max_chars =60

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        for i, icon_filename in enumerate(self.icon_filenames):
            # Load the icon from a file
            icon = QtGui.QIcon('GUI/icons/' + icon_filename)
            # Find the widget by its object name
            widget = getattr(self, self.buttons_names[i])
            # Set the icon on the widget
            widget.setIcon(icon)

        self.add_functions()

        self.uploadTextEdit.setFont(self.font)
        self.uploadTextEdit.textChanged.connect(lambda: self.on_text_changed(self.uploadTextEdit))
        self.uploadTextEdit.setPlaceholderText('Укажите путь до pdf файла')

        self.uploadTextEdit_2.setFont(self.font)
        self.uploadTextEdit_2.textChanged.connect(lambda: self.on_text_changed(self.uploadTextEdit_2))
        self.uploadTextEdit_2.setPlaceholderText('Укажите папку')

        self.uploadTextEdit_3.setFont(self.font)
        self.uploadTextEdit_3.textChanged.connect(lambda: self.on_text_changed(self.uploadTextEdit_3))
        self.uploadTextEdit_3.setPlaceholderText('Введите название')

    def on_text_changed(self, field):
        font = field.currentFont()
        font.setPointSize(16)
        field.setCurrentFont(font)

    def add_functions(self):
        self.settingButton.clicked.connect(self.open_setting)
        self.reportButton.clicked.connect(lambda: self.open_site("https://github.com/WeinerGero/jiandan/issues"))
        self.helpButton.clicked.connect(lambda: self.open_site("https://github.com/WeinerGero/jiandan"))
        self.exitButton.clicked.connect(self.exit)
        self.upload_choisePushButton.clicked.connect(lambda: self.choose_file(self.uploadTextEdit))
        self.upload_choisePushButton_2.clicked.connect(lambda: self.choose_file(self.uploadTextEdit_2))
        # self.uploadTextEdit.textChanged.connect(self.update_text)

    def open_setting(self):
        print("open setting")

    def open_site(self, link):
        webbrowser.open_new(link)

    def exit(self):
        sys.exit()

    def choose_file(self, field):
        text = QFileDialog.getOpenFileName(self, 'Open File', '', '')
        if len(text[0]) >= 60:
            # res[0] = f'...{res[0][:-50]}'
            print(text[0])
        field.setText(text[0])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())