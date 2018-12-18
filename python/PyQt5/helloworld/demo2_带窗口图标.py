import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()

        #使用initUI()方法创建一个GUI
        self.initUI()

    def initUI(self):

        #设置窗口位置及大小(x, y, 宽, 高)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('RaoYi.net')
        #添加窗口图标
        self.setWindowIcon(QIcon('web.png'))

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
