import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #设置提示框字体和字号
        QToolTip.setFont(QFont('SansSerif', 10))

        #创建提示框，可以使用富文本
        self.setToolTip('This is a <b>QWidget</b> widget')

        #创建按钮并创建按钮的提示框
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #调整按钮大小，sizeHint()方法为默认按钮大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
