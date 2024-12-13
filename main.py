from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import os
from iterator import ImageIterator

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = None
        self.setWindowTitle("Image Viewer")
        self.setFixedSize(QSize(800, 600))
        self.set_welcome_menu()

    def set_welcome_menu(self) -> None:
        """
        Create welcome menu
        :return: None
        """
        self.path = None
        self.images = None

        button_open = QPushButton("Open file with images")
        button_open.setFixedSize(200, 50)
        button_open.setStyleSheet("background-color: lightblue; color: black;")
        button_open.clicked.connect(self.select_csv)

        layout_button = QVBoxLayout()
        layout_button.addStretch()
        layout_button.addWidget(button_open, alignment=Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout_button)
        self.setCentralWidget(container)

    def images_menu(self) -> None:
        """
        Create menu with images
        :return: None
        """
        self.label = QLabel()
        button_next_image = QPushButton("Next image")
        button_next_image.setFixedSize(110, 25)
        button_next_image.setStyleSheet("background-color: lightblue; color: black")
        button_close = QPushButton("Exit")
        button_close.setFixedSize(100, 25)
        button_close.setStyleSheet("background-color: lightblue; color: black")

        button_next_image.clicked.connect(self.next_image)
        button_close.clicked.connect(self.set_welcome_menu)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(button_next_image)
        button_layout.addWidget(button_close)

        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.next_image()

    def select_csv(self) -> None:
        """
        Menu to select CSV file
        :return: None
        """
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            ".",
            "CSV-like files (*.csv)"
        )
        if filename:
            if os.stat(filename).st_size == 0:
                QMessageBox.warning(self, "Error", "The selected file is empty. Please select another file.")
                return
            try:
                self.path = filename
                self.images_iterator()
                self.images_menu()
            except ValueError as v:
                print(f"An error occurred: {str(v)}")
                QMessageBox.warning(self, "Error", str(v))
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                QMessageBox.critical(self, "Error", f"An error occurred while reading the file: {str(e)}")

    def images_iterator(self) -> None:
        """
        Create images iterator
        :return: None
        """
        self.images = iter(ImageIterator(self.path))

    def next_image(self) -> None:
        """
        Wrapper for images iterator.
        :return: None
        """
        def get_pixmap():
            try:
                return QPixmap(next(self.images))
            except StopIteration:
                return QPixmap()

        pixmap = get_pixmap()
        if pixmap.isNull():
            return
        pixmap = pixmap.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)

def main():
    application = QApplication([])
    window = MainWindow()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
