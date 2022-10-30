from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_hesapMakinesi(object):
    def setupUi(self, hesapMakinesi):
        hesapMakinesi.setObjectName("hesapMakinesi")
        hesapMakinesi.resize(248, 329)
        self.pushButton = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton.setGeometry(QtCore.QRect(0, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 280, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 230, 51, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_12.setGeometry(QtCore.QRect(100, 280, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 280, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_14.setGeometry(QtCore.QRect(150, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_16.setGeometry(QtCore.QRect(150, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_17.setGeometry(QtCore.QRect(200, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_18.setGeometry(QtCore.QRect(200, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_19.setGeometry(QtCore.QRect(200, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_20.setGeometry(QtCore.QRect(150, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_21.setGeometry(QtCore.QRect(100, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_22.setGeometry(QtCore.QRect(50, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(hesapMakinesi)
        self.pushButton_23.setGeometry(QtCore.QRect(0, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.lineEdit = QtWidgets.QLineEdit(hesapMakinesi)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.retranslateUi(hesapMakinesi)
        QtCore.QMetaObject.connectSlotsByName(hesapMakinesi)

        self.pushButton.clicked.connect(self.sayi1)
        self.pushButton_2.clicked.connect(self.sayi2)
        self.pushButton_3.clicked.connect(self.sayi3)
        self.pushButton_4.clicked.connect(self.sayi4)
        self.pushButton_5.clicked.connect(self.sayi5)
        self.pushButton_6.clicked.connect(self.sayi6)
        self.pushButton_7.clicked.connect(self.sayi7)
        self.pushButton_8.clicked.connect(self.sayi8)
        self.pushButton_9.clicked.connect(self.sayi9)
        self.pushButton_10.clicked.connect(self.sayi0)
        self.pushButton_11.clicked.connect(self.hesapla)
        self.pushButton_12.clicked.connect(self.nokta)
        self.pushButton_13.clicked.connect(self.toplam)
        self.pushButton_14.clicked.connect(self.cikar)
        self.pushButton_15.clicked.connect(self.carp)
        self.pushButton_16.clicked.connect(self.bol)
        self.pushButton_17.clicked.connect(self.parso)
        self.pushButton_18.clicked.connect(self.parsa)
        self.pushButton_19.clicked.connect(self.faktoriyel)
        self.pushButton_20.clicked.connect(self.dondur)
        self.pushButton_21.clicked.connect(self.karekok)
        self.pushButton_22.clicked.connect(self.yuz)
        self.pushButton_23.clicked.connect(self.sil)

    def sayi1(self):
        yazi = self.lineEdit.text() + "1"
        self.lineEdit.setText(yazi)

    def sayi2(self):
        yazi = self.lineEdit.text() + "2"
        self.lineEdit.setText(yazi)

    def sayi3(self):
        yazi = self.lineEdit.text() + "3"
        self.lineEdit.setText(yazi)

    def sayi4(self):
        yazi = self.lineEdit.text() + "4"
        self.lineEdit.setText(yazi)

    def sayi5(self):
        yazi = self.lineEdit.text() + "5"
        self.lineEdit.setText(yazi)

    def sayi6(self):
        yazi = self.lineEdit.text() + "6"
        self.lineEdit.setText(yazi)

    def sayi7(self):
        yazi = self.lineEdit.text() + "7"
        self.lineEdit.setText(yazi)

    def sayi8(self):
        yazi = self.lineEdit.text() + "8"
        self.lineEdit.setText(yazi)

    def sayi9(self):
        yazi = self.lineEdit.text() + "9"
        self.lineEdit.setText(yazi)

    def sayi0(self):
        yazi = self.lineEdit.text() + "0"
        self.lineEdit.setText(yazi)

    def bol(self):
        yazi = self.lineEdit.text() + "/"
        self.lineEdit.setText(yazi)

    def carp(self):
        yazi = self.lineEdit.text() + "*"
        self.lineEdit.setText(yazi)

    def cikar(self):
        yazi = self.lineEdit.text() + "-"
        self.lineEdit.setText(yazi)

    def toplam(self):
        yazi = self.lineEdit.text() + "+"
        self.lineEdit.setText(yazi)

    def sil(self):
        self.lineEdit.setText("")

    def yuz(self):
        yazi = eval(self.lineEdit.text())
        cevap = yazi/100
        try:
            self.lineEdit.setText(str(int(cevap)))
        except:
            self.lineEdit.setText(str(float(cevap)))

    def karekok(self):
        yazi = math.sqrt(float(self.lineEdit.text()))
        self.lineEdit.setText(str(yazi))

    def faktoriyel(self):
        yazi = math.factorial(int(self.lineEdit.text()))
        self.lineEdit.setText(str(yazi))

    def dondur(self):
        yazi = int(self.lineEdit.text()) * -1
        self.lineEdit.setText(str(yazi))

    def hesapla(self):
        yazi = eval(self.lineEdit.text())
        self.lineEdit.setText(str(float(yazi)))

    def parsa(self):
        yazi = self.lineEdit.text() + ")"
        self.lineEdit.setText(yazi)

    def parso(self):
        yazi = self.lineEdit.text() + "("
        self.lineEdit.setText(yazi)

    def nokta(self):
        yazi = self.lineEdit.text() + "."
        self.lineEdit.setText(yazi)


    def retranslateUi(self, hesapMakinesi):
        _translate = QtCore.QCoreApplication.translate
        hesapMakinesi.setWindowTitle(_translate("hesapMakinesi", "Hesap Makinesi"))
        self.pushButton.setText(_translate("hesapMakinesi", "1"))
        self.pushButton_2.setText(_translate("hesapMakinesi", "2"))
        self.pushButton_3.setText(_translate("hesapMakinesi", "3"))
        self.pushButton_4.setText(_translate("hesapMakinesi", "4"))
        self.pushButton_5.setText(_translate("hesapMakinesi", "5"))
        self.pushButton_6.setText(_translate("hesapMakinesi", "6"))
        self.pushButton_7.setText(_translate("hesapMakinesi", "7"))
        self.pushButton_8.setText(_translate("hesapMakinesi", "8"))
        self.pushButton_9.setText(_translate("hesapMakinesi", "9"))
        self.pushButton_10.setText(_translate("hesapMakinesi", "0"))
        self.pushButton_11.setText(_translate("hesapMakinesi", "="))
        self.pushButton_12.setText(_translate("hesapMakinesi", "."))
        self.pushButton_13.setText(_translate("hesapMakinesi", "+"))
        self.pushButton_14.setText(_translate("hesapMakinesi", "-"))
        self.pushButton_15.setText(_translate("hesapMakinesi", "*"))
        self.pushButton_16.setText(_translate("hesapMakinesi", "/"))
        self.pushButton_17.setText(_translate("hesapMakinesi", "("))
        self.pushButton_18.setText(_translate("hesapMakinesi", ")"))
        self.pushButton_19.setText(_translate("hesapMakinesi", "x!"))
        self.pushButton_20.setText(_translate("hesapMakinesi", "+/-"))
        self.pushButton_21.setText(_translate("hesapMakinesi", "√¯"))
        self.pushButton_22.setText(_translate("hesapMakinesi", "%"))
        self.pushButton_23.setText(_translate("hesapMakinesi", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hesapMakinesi = QtWidgets.QWidget()
    ui = Ui_hesapMakinesi()
    ui.setupUi(hesapMakinesi)
    hesapMakinesi.show()
    sys.exit(app.exec_())
