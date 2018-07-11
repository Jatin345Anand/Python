from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    expression = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 861, 81))
        self.lineEdit.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 610, 71, 61))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 520, 71, 61))
        self.pushButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 520, 71, 61))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 520, 71, 61))
        self.pushButton_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 420, 71, 61))
        self.pushButton_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 420, 71, 61))
        self.pushButton_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 420, 71, 61))
        self.pushButton_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 320, 71, 61))
        self.pushButton_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 320, 71, 61))
        self.pushButton_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 320, 71, 61))
        self.pushButton_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 420, 71, 61))
        self.pushButton_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(560, 510, 71, 61))
        self.pushButton_12.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(560, 600, 71, 61))
        self.pushButton_13.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(670, 320, 181, 61))
        self.pushButton_16.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_16.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(670, 410, 181, 61))
        self.pushButton_15.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(560, 320, 71, 61))
        self.pushButton_14.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_14.setObjectName("pushButton_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 31))
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
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_11.setText(_translate("MainWindow", "\\"))
        self.pushButton_12.setText(_translate("MainWindow", "-"))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_15.setText(_translate("MainWindow", "="))
        self.pushButton_16.setText(_translate("MainWindow", "Clear"))

        self.lineEdit.setReadOnly(True)


        self.buttons = [self.pushButton,self.pushButton_2,self.pushButton_3,
                        self.pushButton_4, self.pushButton_5, self.pushButton_6,
                        self.pushButton_7, self.pushButton_8, self.pushButton_9,
                        self.pushButton_10, self.pushButton_11, self.pushButton_12,
                        self.pushButton_13, self.pushButton_14]

        for btn in self.buttons:
            btn.clicked.connect(self.calc)

        self.pushButton_15.clicked.connect(self.calculate)
        self.pushButton_16.clicked.connect(self.clear)

    def calc(self):
        s = self.sender()
        # print(s.text())
        self.expression.append(s)
        self.lineEdit.clear()
        # print(self.expression)
        for data in self.expression:
            self.lineEdit.setText(self.lineEdit.text() +  data.text())

    def calculate(self):
        exp = self.lineEdit.text()
        result = eval(exp)
        self.lineEdit.setText(str(result))

    def clear(self):
        self.expression.clear()
        self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

