import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SEÇİM EKRANI")
        self.showMaximized() #pencere açılırken tam ekran açılacak ki farklı boyutlardakı ekranlara uyum sağlasın
        self.setStyleSheet(open("themes/Perstfic.qss","r").read()) #css içeren tasarım için kullanılan qss dosyasını okutma işlemi
        self.setUI()


    def but1(self): #buton1 e basıldığında eyeDetection dosyasını çalıştırıyor. çıkmak için q ya basmak gerek

        import faceDetection #import deyip py uzantılı dosyayı çalıştırmış oluyoruz, çalıştırmak istediğimiz py uzantılı dosya projemizde olmak zorunda
        print("kod çalıştı-1") #bu fonksiyona girip girmediğini kontrol ediyorum
    def but2(self):
        import eyeDetection
        print("kod çalıştı-2")
    def but3(self):
        import one
        print("kod çalıştı-3")

    def setUI(self):


      h_box=QHBoxLayout() #butonların yan yana dizili durması için oluşturdum

      button1=QPushButton("\nRENKLİ(RGB)KAMERAYI AÇ")
      button1.setMaximumHeight(600)
      button1.setIcon(QIcon("icons/rgb.png"))
      button1.clicked.connect(lambda:self.but1())


      button2=QPushButton("  TERMAL KAMERAYI AÇ")
      button2.setMaximumHeight(600)
      button2.setIcon(QIcon("icons/termalicon.png"))
      #button2.setIconSize(QSize(100,120))
      button2.clicked.connect(lambda:self.but2())

      button3=QPushButton("  ÇALIŞTIR")
      button3.setMaximumHeight(600)
      button3.setIcon(QIcon("icons/run.png"))
      #button3.setIconSize(QSize(120, 160))
      button3.clicked.connect(lambda: self.but3())

      h_box.addWidget(button1)
      h_box.addWidget(button2)
      h_box.addWidget(button3)

      self.setLayout(h_box)

      self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec())