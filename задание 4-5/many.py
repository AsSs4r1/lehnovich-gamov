import sys
import sqlite3
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog, QMessageBox
from PyQt5.QtGui import QColor
from addEditCoffeeForm import AddEditCoffeeForm  # Обратите внимание на импорт класса формы

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Coffee Database')
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.add_button = QPushButton('Добавить кофе')
        self.add_button.clicked.connect(self.open_add_edit_form)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

        # Подключение к базе данных
        self.conn = sqlite3.connect('coffee.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS coffee (
                id INTEGER PRIMARY KEY,
                name TEXT,
                type TEXT
            )
        ''')
        self.conn.commit()

    def open_add_edit_form(self):
        self.add_edit_form = AddEditCoffeeForm(self)
        self.add_edit_form.show()

    def closeEvent(self, event):
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
