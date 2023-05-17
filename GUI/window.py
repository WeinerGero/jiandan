import webbrowser
import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QFont

from algorythm import main

Form, Window = uic.loadUiType("interface.ui")

class MainWindow(QMainWindow, Form):
    icon_filenames = ['iconizer-settings.svg', 'iconizer-alert-circle.svg', 'iconizer-help-circle.svg', 'iconizer-x.svg', 'iconizer-play.svg']
    buttons_names = ['settingButton', 'reportButton', 'helpButton', 'exitButton', 'PushButtonStart']
    font = QFont()
    font.setPointSize(16)
    max_chars = 60

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        for i, icon_filename in enumerate(self.icon_filenames):
            # Load the icon from a file
            icon = QtGui.QIcon('icons/' + icon_filename)
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

        self.timer = None

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
        self.upload_choisePushButton_2.clicked.connect(lambda: self.choose_directory(self.uploadTextEdit_2))
        self.PushButtonStart.clicked.connect(self.start_reading)
        # self.uploadTextEdit.textChanged.connect(self.update_text)

    def start_progress_bar(self):
        # Reset the progress bar to 0
        self.progressBar.setValue(0)
        # Start the timer to increment the progress bar value every 100 ms
        self.timer = self.startTimer(1)

    def timerEvent(self, event):
        # Increment the progress bar value by 1
        value = self.progressBar.value() + 1
        self.progressBar.setValue(value)
        # Stop the timer when the progress bar is full
        if value == 100:
            self.killTimer(self.timer)

    def open_setting(self):
        # print("open setting")
        error_message = "В разработке"
        self.Error_textBrowser.setFont(self.font)
        self.Error_textBrowser.setText(error_message)

    def open_site(self, link):
        webbrowser.open_new(link)

    def exit(self):
        sys.exit()

    def choose_file(self, field):
        path_filename = QFileDialog.getOpenFileName(self, 'Choose File', '', '')
        field.setText(path_filename[0])

    def choose_directory(self, field):
        path_filename = QFileDialog.getExistingDirectory(self, 'Choose Directory', '')
        field.setText(path_filename)

    def start_reading(self):
        input_path = self.uploadTextEdit.toPlainText()
        output_path = self.uploadTextEdit_2.toPlainText()
        name_output_file = self.uploadTextEdit_3.toPlainText()

        if len(input_path) <= 1:
            # print('Введите путь файла')
            error_message = "Введите путь файла"
            self.Error_textBrowser.setFont(self.font)
            self.Error_textBrowser.setText(error_message)

        elif len(output_path) <= 1:
            # print('Введите путь папки')
            error_message = "Введите путь папки"
            self.Error_textBrowser.setFont(self.font)
            self.Error_textBrowser.setText(error_message)

        elif len(name_output_file) <= 1:
            # print('Введите название колоды')
            error_message = "Введите название колоды"
            self.Error_textBrowser.setFont(self.font)
            self.Error_textBrowser.setText(error_message)

        else:
            self.start_progress_bar()
            result = main(input_path, output_path, name_output_file)
            if result == 0:
                # print('Файл не найден')
                error_message = "Файл не найден"
                self.Error_textBrowser.setFont(self.font)
                self.Error_textBrowser.setText(error_message)
                self.killTimer(self.timer)
            elif result == 1:
                # print('Файл не подходит, загрузите pdf')
                error_message = "Файл не подходит, загрузите pdf"
                self.Error_textBrowser.setFont(self.font)
                self.Error_textBrowser.setText(error_message)
                self.killTimer(self.timer)
            elif result == 2:
                #print('Неправильный путь папки')
                error_message = "Неправильный путь папки"
                self.Error_textBrowser.setFont(self.font)
                self.Error_textBrowser.setText(error_message)
                self.killTimer(self.timer)
            else:
                error_message = ""
                self.Error_textBrowser.setText(error_message)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
