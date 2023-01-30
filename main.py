from json import load
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog, QLabel, QAction, QMainWindow, QApplication
from PyQt5.uic import loadUiType
from Encrypter import Encrypter
from Decrypter import Decrypter
import base64
import os
import sys
import webbrowser


UI, _ = loadUiType("main.ui")

def start():
    global m
    m = MainPage()
    m.show()

class EncryptPage(Encrypter):

    def __init__(self):
        self.Key = ""
        self.keyFile = {}
        self.File = {}
        self.FileString = ""
        self.encryptKeyFileBtn.clicked.connect(self.encrypt_chooseKeyImage)
        self.encryptFileBtn.clicked.connect(self.chooseFileImage)
        self.backBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.encryptBtn.clicked.connect(self.onClickEncrypt)

    def encrypt_chooseKeyImage(self):
        self.keyFile = QFileDialog.getOpenFileName(self, 'Open File')
        self.keyPath.setText(self.keyFile[0])
        pixmap = QtGui.QPixmap(self.keyFile[0])
        self.encryptKeyImg.setPixmap(pixmap.scaledToHeight(290))
        if self.keyFile != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly)
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            #self.Key = base64.b64encode(pixmap_bytes)
            self.Key = pixmap_bytes

    def chooseFileImage(self):
        self.File = QFileDialog.getOpenFileName(self, 'Open File')
        self.filePath.setText(self.File[0])
        pixmap = QtGui.QPixmap(self.File[0])
        self.encryptFileImg.setPixmap(pixmap.scaledToHeight(290))
        if self.File != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)   
            buff.open(QtCore.QIODevice.WriteOnly)
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            self.FileString = base64.b64encode( pixmap_bytes)

    def onClickEncrypt(self):
        x = Encrypter(self.Key, self.FileString)
        cipherMessage = x.encrypt()
        fh = open("cipher.txt", "wb")
        fh.write(cipherMessage)
        fh.close()

class DecryptPage(Decrypter):

    def __init__(self):
        self.Key = ""
        self.keyFile = {}
        self.cipherMessage = {}
        self.decryptKeyFileBtn.clicked.connect(self.decrypt_chooseKeyImage)
        self.decryptFileBtn.clicked.connect(self.chooseCipherFile)
        self.backBtn_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.decryptBtn.clicked.connect(self.onClickDecrypt)

    def decrypt_chooseKeyImage(self):
        self.keyFile = QFileDialog.getOpenFileName(self, 'Open File')
        self.keyPath_2.setText(self.keyFile[0])
        pixmap = QtGui.QPixmap(self.keyFile[0])
        self.decryptKeyImg.setPixmap(pixmap.scaledToHeight(290))
        if self.keyFile != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly)
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            #self.Key = base64.b64encode(pixmap_bytes)
            self.Key = pixmap_bytes

    def chooseCipherFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')
        self.filePath_2.setText(file[0])
        text = open(file[0]).read()
        self.cipherMessage = text.encode('utf-8')

    def onClickDecrypt(self):
        x = Decrypter(self.Key, self.cipherMessage)
        decipheredImage = x.decrypt()
        ba = QtCore.QByteArray(decipheredImage)
        pixmap = QtGui.QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok
        self.decipheredImage.setPixmap(pixmap.scaledToHeight(401))
    

class MainPage(QMainWindow, QWidget, UI, EncryptPage, DecryptPage):

    def __init__(self):
        QMainWindow.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        EncryptPage.__init__(self)
        DecryptPage.__init__(self)

        self.HandleButtons()
        self.stackedWidget.setCurrentIndex(0)

    def HandleButtons(self):
        self.encryptPageBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.decryptPageBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.helpBtnMain.clicked.connect(lambda: webbrowser.open('http://www.google.com'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = start()
    app.exec_()
