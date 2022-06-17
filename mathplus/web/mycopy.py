import sys
import time
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from mouse_keyboard import * 


class Form(QDialog): # QDialog是窗口类
    
    def __init__(self, parent=None): #没有parent的是最上层的窗口  
        """初始化布局"""
        super().__init__(parent) #父类初始化父类的
        self.setWindowTitle("mycopy") #子类初始化子类的，设置标题
        self.setWindowIcon(QIcon("mycopy.jpg"))
        self.resize(50,50)

        # Set dialog layout
        layout = QVBoxLayout()

        self.Qtable_id = QLineEdit("6.1")
        layout.addWidget(self.Qtable_id)
        self.Qtable_id.setValidator(QDoubleValidator(6,12,2))

        self.Qdown_push = QPushButton(self)
        layout.addWidget(self.Qdown_push)
        self.Qdown_push.setText(u"  自动下载  ")
        self.Qdown_push.clicked.connect(self.down_push)


        self.Qcopy_line = QLabel((u'浏1定位math2(4)右上角')) #还能再显示20个字符
        layout.addWidget(self.Qcopy_line)
        self.Qcopy_line.setFrameStyle(QFrame.Panel | QFrame.Sunken) #带凹陷的
        self.Qcopy_line.setStyleSheet("color:#FF3333")


        Qcopy_grid = QGridLayout()
        layout.addLayout(Qcopy_grid)
        
        self.Qcopy_edit = QLineEdit('')
        Qcopy_grid.addWidget(self.Qcopy_edit, 0 ,0)
        self.Qcopy_edit.setValidator(QIntValidator(0,100))

        self.Qcopy_push = QPushButton(self)
        Qcopy_grid.addWidget(self.Qcopy_push, 0, 1)
        self.Qcopy_push.setText(u"  快速复制  ")
        self.Qcopy_push.clicked.connect(self.quick_copy)


        Qcopy_plus_grid = QGridLayout()
        layout.addLayout(Qcopy_plus_grid)

        self.Qcopy_plus_edit = QLineEdit('')
        Qcopy_plus_grid.addWidget(self.Qcopy_plus_edit, 0 ,0)
        self.Qcopy_plus_edit.setValidator(QIntValidator(0,100))

        self.Qcopy_plus_push = QPushButton(self)
        Qcopy_plus_grid.addWidget(self.Qcopy_plus_push, 0, 1)
        self.Qcopy_plus_push.setText(u"  高级复制  ")
        self.Qcopy_plus_push.clicked.connect(self.plus_copy)

        self.setLayout(layout)


    def quick_copy(self):
        times = self.Qcopy_edit.text()
        times = int(times)
        copy(times)

    def plus_copy(self):
        times = self.Qcopy_plus_edit.text()
        times = int(times)
        copy_plus(times)

    def down_push(self):
        table_id = self.Qtable_id.text()
        download(table_id)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop直到exit()被调用,即运行程序
    sys.exit(app.exec_()) # 前面的show方法并没有显示，通过此时的层层调用才显示

