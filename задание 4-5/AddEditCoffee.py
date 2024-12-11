from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Добавить/Редактировать Кофе")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()
        
        self.name_label = QLabel('Название:')
        self.name_input = QLineEdit(self)

        self.type_label = QLabel('Тип:')
        self.type_input = QLineEdit(self)

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_coffee)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_coffee(self):
        name = self.name_input.text()
        _type = self.type_input.text()
        if name and _type:
            # Сохранение в базу данных (сделайте это, если базу данных и т.д. хотите использовать)
            QMessageBox.information(self, "Успех", "Кофе добавлен!")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
