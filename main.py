import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtCore import QTimer

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self.auto_save)
        self.auto_save_timer.start(1000)  # Auto-save every 5 seconds

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 800, 600)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*.*)')
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.text_edit.setPlainText(text)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*.*)')
        if file_path:
            with open(file_path, 'w') as file:
                text = self.text_edit.toPlainText()
                file.write(text)

    def auto_save(self):
        # Auto-save the content of the text edit widget
        file_path = 'autosave.txt'  # You can use a different file path for auto-saving
        with open(file_path, 'w') as file:
            text = self.text_edit.toPlainText()
            file.write(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
