# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 300)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.firstBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.firstBox.setObjectName("firstBox")
        self.verticalLayout.addWidget(self.firstBox)
        self.biznesBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.biznesBox.setObjectName("biznesBox")
        self.verticalLayout.addWidget(self.biznesBox)
        self.economicBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.economicBox.setObjectName("economicBox")
        self.verticalLayout.addWidget(self.economicBox)
        self.resultLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Wybierz klasę lotu: "))
        self.firstBox.setText(_translate("Dialog", "Klasa pierwsza: 300zł"))
        self.biznesBox.setText(_translate("Dialog", "Klasa biznesowa: 600zł"))
        self.economicBox.setText(_translate("Dialog", "Klasa ekonomiczna: 20zł"))
