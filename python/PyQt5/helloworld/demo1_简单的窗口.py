import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #创建一个应用对象。sys.argv是一组命令行参数的列表，提供对脚本控制的功能
    app = QApplication(sys.argv)

    #用户界面基本控件，提供基本的应用构造器
    w = QWidget()
    #定义尺寸(宽, 高)
    w.resize(250, 150)
    #定义界面位置，以屏幕左上角为原点
    w.move(300, 300)
    #窗口标题
    w.setWindowTitle('Simple')
    #显示控件
    w.show()

    sys.exit(app.exec_())
