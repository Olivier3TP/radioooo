import sys
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.firstBox.toggled.connect(self.button_click)
        self.ui.biznesBox.toggled.connect(self.button_click)
        self.ui.economicBox.toggled.connect(self.button_click)
        self.show()

    def button_click(self):
        price = 0
        name = ""
        if self.ui.firstBox.isChecked():
            price = 300
            name = "pierwszej"
        elif self.ui.biznesBox.isChecked():
            price = 600
            name = "biznes"
        elif(self.ui.economicBox.isChecked()):
            price = 20
            name = "ekonomicznej"
        else:
            price = 0
            name = " "
        self.ui.resultLabel.setText(f'Cena za twój bilet w klasie {name} to: {price} zł')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())