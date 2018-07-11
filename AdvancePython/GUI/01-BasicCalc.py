from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 70, 501, 91))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 230, 501, 91))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 281, 71))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 321, 71))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 380, 531, 91))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 400, 251, 41))
        self.label_3.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 560, 251, 71))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 560, 251, 71))
        self.pushButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 560, 251, 71))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 560, 251, 71))
        self.pushButton_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter First Number"))
        self.label_2.setText(_translate("MainWindow", "Enter Second Number"))
        self.label_3.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Sub"))
        self.pushButton_3.setText(_translate("MainWindow", "Mul"))
        self.pushButton_4.setText(_translate("MainWindow", "Div"))

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.sub)
        self.pushButton_3.clicked.connect(self.mul)
        self.pushButton_4.clicked.connect(self.div)
        self.lineEdit_3.setReadOnly(True)

    def values(self):
        self.num_1 = self.lineEdit.text()
        self.num_2 = self.lineEdit_2.text()
        return int(self.num_1), int(self.num_2)

    def add(self):
        num_1, num_2 = self.values()
        result = num_1 + num_2
        # print("Clicked on add")
        self.lineEdit_3.setText(str(result))

    def sub(self):
        print("Clicked on sub")

    def div(self):
        print("Clicked on div")

    def mul(self):
        print("Clicked on mul")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

