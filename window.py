from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QVBoxLayout, QGridLayout, QWidget)
from PyQt6.QtGui import QIcon
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dying Light 2 Save Manager")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)),"dying_light_2.ico")))
        self.setGeometry(100, 100, 800, 600)
    
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.content_panel = self.create_content_panel()

        self.layout.addWidget(self.content_panel)

        self.setLayout(self.layout)
        self.show()

    def create_layout(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        return layout

    def create_content_panel(window):
        text_widget = QTextEdit(window)
        text_widget.setReadOnly(True)
        text_widget.setStyleSheet(
        """      
            background: #0C0C0C;
            color: #CCCCCC;
            border: none;
            outline: none;
            font-family: "Cascadia Code";
            font-size: 13px;
        """)
        text_widget.setContentsMargins(0, 0, 0, 0)
        return text_widget

    def display_message(self, message):
        self.content_panel.append(message)