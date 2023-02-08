from random import randint
import clipboard
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

abc = "вБsШуЕCoЗBvА…МeJщXСKQWкqЧВЭЪ0ЬtЦЯmбAгд2:ж7иO.Yz+опр*jД8х ч9uёiьэХяdсЁ-Ръ," \
      "1шТ!лMgRNУыЖйU3ФтxИabcКНTПюyIZl=ЩkDLrмhц6wОЫGЮ_аF;Лn?EHfV45нзЙфpеГPS❤"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # Получение нужного доступа
        self.setWindowTitle("Coder V5.0")  # Название окна
        self.clear_but = QPushButton("Clear")
        self.clear_but.setCheckable(True)
        self.clear_but.clicked.connect(self.cleaning)
        self.button = QPushButton("Copy")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.copy_text)
        self.input_text = QLineEdit()  # Создание экземпляра поля ввода
        self.input_text.setPlaceholderText("Enter your text...")
        self.lablet = QLabel(
            '<h2 style="background-color: rgb(153, 153, 255);">Your message</h2>')  # Создание экземпляра поля вывода
        self.lablet.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.input_text.textChanged.connect(self.changed_text)  # Подключение действия изменения текста к функции
        layout = QVBoxLayout()  # Создание экземпляра коробки
        layout.addWidget(self.input_text)  # Вложение трёх полей в коробку
        layout.addWidget(self.lablet)
        layout.addWidget(self.clear_but)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setFixedSize(QSize(600, 240))  # Размеры окна
        self.setCentralWidget(container)  # Виджет в центре

    def cleaning(self):
        self.input_text.setText("")

    def copy_text(self):
        try:
            clipboard.copy(self.otext)
        except:
            return

    def changed_text(self, text):
        if text[0:5] == "DA YA":
            self.lablet.setText(self.decode(text))
        else:
            self.lablet.setText(self.encode(text))

    def decode(self, text):
        out_text = ""
        tx = text.replace("@", "")
        tx = tx.replace("DA YA", "")
        temp = ""
        for i in range(0, len(tx)):
            if i == 0 or i % 3 == 0 or i == len(tx) - 1:
                continue
            temp += tx[i]
        tx = temp
        key = tx[0:2]
        tx = tx.replace(key, "")
        while len(str(key)) < len(tx):
            key = str(int(key) ** 2)
        for i in range(len(tx)):
            for a in range(len(abc)):
                if tx[i] == abc[a]:
                    try:
                        out_text += abc[a + int(key[i])]
                    except IndexError:
                        out_text += abc[a - (142 - int(key[i]))]
        self.otext = out_text
        return out_text

    def encode(self, text):
        out_text = "DA YA "
        key = 0
        while int(key) % 10 == 0:
            key = str(randint(11, 99))
        out_text += key + " "
        while len(str(key)) < len(text):
            key = str(int(key) ** 2)
        for i in range(len(text)):
            for a in range(len(abc)):
                if text[i] == abc[a]:
                    out_text += abc[a - int(key[i])]
            if i % 2 != 0:
                out_text += " "
        if len(text) % 2 != 0:
            out_text += '@ '
        out_text += "DA YA"
        self.otext = out_text
        return out_text


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
