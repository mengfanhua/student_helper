from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from get_UI import poemUI, noteUI, classUI, settingUI
from get_database import sqlitedatabase


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        desktop = QApplication.desktop()
        # 宽和高，经过多次测试获得，在测试机上看起来最舒服的一种大小
        self.width = int(desktop.width()*0.35)
        self.height = int(desktop.height()*0.88)
        # 不可变化大小
        self.setMaximumSize(QSize(self.width, self.height))
        self.setMinimumSize(QSize(self.width, self.height))
        # 显示位置
        self.move(QPoint(int(desktop.width()*0.60), int(desktop.height()*0.04)))
        # 使用palette来设置背景图片，但测试发现，在子widget中设置无效
        self.setObjectName("MainWindow")
        self.setStyleSheet("QWidget#MainWindow{background-color:transparent;}")
        self.setContentsMargins(0, 0, 0, 0)
        # 以上为设置主界面的位置、大小、背景等方法

        self.oneLayout = QVBoxLayout()
        self.oneLayout.setContentsMargins(0, 0, 0, 0)
        # 由于该布局中仅有两个widget，故设置占比为9：1
        self.oneLayout.setStretch(0, 9)
        self.oneLayout.setStretch(1, 1)
        self.oneLayout.setSpacing(0)
        # 第一层layout, 纵向

        self.twoWidget1 = QWidget(self)
        self.twoWidget1.setObjectName("TopWidget")
        self.twoWidget1.setStyleSheet("QWidget#TopWidget{background-color:transparent;}")
        self.twoWidget1.setContentsMargins(0, 0, 0, 0)
        self.twoWidget2 = QWidget(self)
        self.twoWidget2.setObjectName("BottomWidget")
        self.twoWidget2.setStyleSheet("QWidget#BottomWidget{background-color:qlineargradient("
                                      "spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(55, 140, 225, 255),"
                                      " stop:1 rgba(255, 255, 255, 255));}")

        # 设置下层layout的上边框显示，颜色和粗细待调整
        self.twoWidget2.setContentsMargins(0, 0, 0, 0)

        self.twoLayout1 = QStackedLayout()
        self.twoLayout1.setContentsMargins(0, 0, 0, 0)

        # 下方四个分别来自于不同的Widget，用于界面设计的解耦
        self.one = poemUI.PoemWidget()
        self.two = classUI.ClassWidget()
        self.three = noteUI.NoteWidget()
        self.four = settingUI.SettingWidget()
        self.twoLayout1.addWidget(self.one)
        self.twoLayout1.addWidget(self.two)
        self.twoLayout1.addWidget(self.three)
        self.twoLayout1.addWidget(self.four)
        # 第二层上层layout，此为层叠布局，可根据下方按钮点击更换层叠布局

        self.twoLayout2 = QHBoxLayout()
        self.twoLayout2.setContentsMargins(0, 0, 0, 0)  # 布局内边距
        self.twoLayout2.setSpacing(0)
        # layout内组件间隔为0，但与实际情况不符合，仍会有一小部分的间隔

        fontId = QFontDatabase.addApplicationFont("./fonts/汉仪糯米团简.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
        # 导入字体，使界面更美观

        # 构建按钮，绑定事件
        self.button1 = QPushButton("诗")#QIcon("./resources/poem1.png"), "")
        self.button1.setFont(QFont(fontName))
        # self.button1.setIconSize(QSize(self.button1.width(), self.button1.height()))
        self.button1.clicked.connect(lambda: self.show_widget(0))
        self.button1.setFixedSize(QSize(int(self.width / 4), int(self.height / 14)))
        self.button1.setStyleSheet("border:none;font-size:%spx;font-weight:bold;color:#477CF1" %
                                   int(self.height / 20))
        self.button2 = QPushButton("课")
        self.button2.setFont(QFont(fontName))
        # self.button2.setIconSize(QSize(self.button2.width(), self.button2.height()))
        self.button2.clicked.connect(lambda: self.show_widget(1))
        self.button2.setFixedSize(QSize(int(self.width / 4), int(self.height / 14)))
        self.button2.setStyleSheet("border:none;font-size:%spx;font-weight:bold;color:#477CF1" %
                                   int(self.height / 20))
        self.button3 = QPushButton("记")
        self.button3.setFont(QFont(fontName))
        # self.button3.setIconSize(QSize(self.button3.width(), self.button3.height()))
        self.button3.clicked.connect(lambda: self.show_widget(2))
        self.button3.setFixedSize(QSize(int(self.width / 4), int(self.height / 14)))
        self.button3.setStyleSheet("border:none;font-size:%spx;font-weight:bold;color:#477CF1" %
                                   int(self.height / 20))
        #self.button4 = QPushButton("我")
        #self.button4.setFont(QFont(fontName))
        # self.button4.setIconSize(QSize(self.button4.width(), self.button4.height()))
        #self.button4.clicked.connect(lambda: self.show_widget(3))
        #self.button4.setFixedSize(QSize(int(self.width / 4), int(self.height / 14)))
        #self.button4.setStyleSheet("border:none;font-size:%spx;font-weight:bold;color:#477CF1" %
        #                           int(self.height / 20))
        # 布局添加按钮
        self.twoLayout2.addWidget(self.button1)
        self.twoLayout2.addWidget(self.button2)
        self.twoLayout2.addWidget(self.button3)
        #self.twoLayout2.addWidget(self.button4)
        # 第二层下层layout，用于放置层叠布局切换按钮

        self.twoWidget1.setLayout(self.twoLayout1)
        self.twoWidget2.setLayout(self.twoLayout2)
        # 由于layout不可直接嵌套layout，故使用两个Widget来接受layout

        self.oneLayout.addWidget(self.twoWidget1)
        self.oneLayout.addWidget(self.twoWidget2)
        # 第一层添加第二层

        self.setLayout(self.oneLayout)
        # 主界面设置layout

        self.setWindowTitle("Hello Qt")
        # 在窗口初始化的时候加入就可以了
        # self.window是QMainWindow()
        # self.show()
        # self.twoWidget1.show()
        # self.twoWidget2.show()
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框，置顶

    def show_widget(self, index):
        self.twoLayout1.setCurrentIndex(index)
        # 在button绑定该事件时传入对应参数，即调用不同层叠布局


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    sqlitedatabase.load_db()
    screen = MainWidget()
    screen.show()
    sys.exit(app.exec_())
