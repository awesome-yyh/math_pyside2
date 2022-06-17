import sys
import time
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import pyperclip #剪贴板
import json

from SqlClassID import *
from HtmlFun import *  # [q,r,l] = read_html(table_id)
from doit import *
from sympy import latex
from mouse_keyboard import *
from frc import *

with open("t_dict_db.json",'r') as load_f:
    t_dict = json.load(load_f)

questionId, red_word, length = 0,0,0
question_id, copy_id = 0, 0
db_answer = []

class Form(QDialog): # QDialog是窗口类
    
    def __init__(self, parent=None): #没有parent的是最上层的窗口  
        self.msql = Mysql()
        """初始化布局"""
        super().__init__(parent) #父类初始化父类的
        self.setWindowTitle("math112113") #子类初始化子类的，设置标题
        self.setWindowIcon(QIcon("laibunizi.jpg"))
        self.resize(550,550)

        # Set dialog layout
        layout = QVBoxLayout()

        # Qtable_grid = QGridLayout()
        # layout.addLayout(Qtable_grid)

        Qquestion_grid = QGridLayout()
        layout.addLayout(Qquestion_grid)

        self.Qtable_down = QPushButton(self)
        Qquestion_grid.addWidget(self.Qtable_down, 0, 0)
        self.Qtable_down.setText(u" 下载 ")
        self.Qtable_down.setShortcut('Ctrl+x')
        self.Qtable_down.clicked.connect(self.down_push)

        self.Qtable_id = QLineEdit("6.1")
        Qquestion_grid.addWidget(self.Qtable_id, 0 ,1)
        self.Qtable_id.setValidator(QDoubleValidator(6,12,2))

        self.Qtable_read = QPushButton(self)
        Qquestion_grid.addWidget(self.Qtable_read, 0, 2)
        self.Qtable_read.setText(u" 读题 ")
        self.Qtable_read.setShortcut('Ctrl+d')
        self.Qtable_read.clicked.connect(self.table_read)

        self.QquestionID = QLabel((u'  第 ** 题  |  共 ** 题  ')) #暂未读取，读取成功，暂未下载
        Qquestion_grid.addWidget(self.QquestionID, 0 ,3)
        self.QquestionID.setFrameStyle(QFrame.Panel | QFrame.Sunken) #带凹陷的
        self.QquestionID.setAlignment(Qt.AlignCenter) #居中

        self.Qquestion_last = QPushButton(self)
        Qquestion_grid.addWidget(self.Qquestion_last, 0, 4)
        self.Qquestion_last.setText(u"<上一题")
        self.Qquestion_last.setShortcut('Ctrl+h')
        self.Qquestion_last.clicked.connect(self.question_last)

        self.Qquestion_next = QPushButton(self)
        Qquestion_grid.addWidget(self.Qquestion_next, 0, 5)
        self.Qquestion_next.setText(u"下一题>")
        self.Qquestion_next.setShortcut('Ctrl+l')
        self.Qquestion_next.clicked.connect(self.question_next)

        self.Qred_show = QLabel(u' 题中红字 --> ')
        layout.addWidget(self.Qred_show)
        self.Qred_show.setFrameStyle(QFrame.Panel | QFrame.Sunken) #带凹陷的
        self.Qred_show.setStyleSheet("color:#FF3333")

        self.Qanswers = QTextEdit(u'显示答案：')
        layout.addWidget(self.Qanswers)
        
        Qcopy_grid = QGridLayout()
        layout.addLayout(Qcopy_grid)

        self.Qdel_push = QPushButton(self)
        Qcopy_grid.addWidget(self.Qdel_push, 0, 0)
        self.Qdel_push.setText(u"删除")
        self.Qdel_push.setFixedSize(40,18)
        self.Qdel_push.clicked.connect(self.del__answer)

        self.Qcopy_line = QLabel((u'复制->')) #还能再显示20个字符
        Qcopy_grid.addWidget(self.Qcopy_line, 0, 1)
        self.Qcopy_line.setFrameStyle(QFrame.Panel | QFrame.Sunken) #带凹陷的

        self.Qcopy_last = QPushButton(self)
        Qcopy_grid.addWidget(self.Qcopy_last, 0, 2)
        self.Qcopy_last.setText(u"↑上一空↑")
        self.Qcopy_last.setShortcut('Ctrl+k')
        self.Qcopy_last.clicked.connect(self.copy_last)

        self.Qcopy_next = QPushButton(self)
        Qcopy_grid.addWidget(self.Qcopy_next, 0, 3)
        self.Qcopy_next.setText(u"↓下一空↓")
        self.Qcopy_next.setShortcut('Ctrl+j')
        self.Qcopy_next.clicked.connect(self.copy_next)


        Qwirte_grid = QGridLayout()
        layout.addLayout(Qwirte_grid)

        self.Qwirte = QLineEdit("")
        Qwirte_grid.addWidget(self.Qwirte, 0 ,0)
        
        self.Qsolve_push = QPushButton(self)
        Qwirte_grid.addWidget(self.Qsolve_push, 0, 1)
        self.Qsolve_push.setText(u"算一算")
        self.Qsolve_push.setShortcut('Ctrl+s')
        self.Qsolve_push.clicked.connect(self.solve__answer)

        self.Qsort_push = QPushButton(self)
        Qwirte_grid.addWidget(self.Qsort_push, 0, 2)
        self.Qsort_push.setText(u"排列")
        self.Qsort_push.setShortcut('Ctrl+p')
        self.Qsort_push.clicked.connect(self.sort__answer)


        Qfrac_grid = QGridLayout()
        layout.addLayout(Qfrac_grid)

        self.Qfrac = QLineEdit("")
        Qfrac_grid.addWidget(self.Qfrac, 0 ,0)
        
        self.Qfrac_push = QPushButton(self)
        Qfrac_grid.addWidget(self.Qfrac_push, 0, 1)
        self.Qfrac_push.setText(u"分数换算")
        self.Qfrac_push.setShortcut('Ctrl+f')
        self.Qfrac_push.clicked.connect(self.solve__frac)


        self.QMyanswers = QTextEdit()
        self.QMyanswers.setText("///")

        layout.addWidget(self.QMyanswers)

        Qadd_grid = QGridLayout()
        layout.addLayout(Qadd_grid)

        self.Qadd_push = QPushButton(self)
        Qadd_grid.addWidget(self.Qadd_push, 0, 0)
        self.Qadd_push.setText(u"  添加到题库  ")
        self.Qadd_push.setShortcut('Ctrl+t')
        self.Qadd_push.clicked.connect(self.add__answer)

        # self.Qadd_push = QPushButton(self)
        # Qadd_grid.addWidget(self.Qadd_push, 0, 1)
        # self.Qadd_push.setFixedSize(50,22)
        # self.Qadd_push.setText(u" Q/A ")
        # self.Qadd_push.clicked.connect(self.add__answer)

        # self.Qadd_push = QPushButton(self)
        # Qadd_grid.addWidget(self.Qadd_push, 0, 2)
        # self.Qadd_push.setFixedSize(50,22)
        # self.Qadd_push.setText(u" open ")
        # self.Qadd_push.clicked.connect(self.add__answer)

        self.Qsame_push = QPushButton(self)
        Qadd_grid.addWidget(self.Qsame_push, 0, 1)
        self.Qsame_push.setText(u"  查找同类题  ")
        self.Qsame_push.setShortcut('Ctrl+c')
        self.Qsame_push.clicked.connect(self.same__answer)

        # # 显示大题答案图案
        # self.Qimg_show = QLabel()
        # layout.addWidget(self.Qimg_show)
        # self.Qimg_show.setFixedSize(550, 200)
        # self.Qimg_show.setFrameStyle(QFrame.Panel | QFrame.Sunken) #带凹陷的
        # pixmap = QPixmap('./laibunizi.jpg')
        # self.Qimg_show.setPixmap(pixmap) 
        # self.Qimg_show.setScaledContents(True)


        self.setLayout(layout)

    def sort__answer(self):
        s = self.Qwirte.text()
        ss = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isspace():
                ss.append('.')
            ss.append(s[i])
        ss = ''.join(ss)
        if len(ss) < 35:
            selectA = ss[0:3]+'  '+ss[15:18]+'\n'+\
            ss[3:6]+'  '+ss[18:21]+'\n'+\
            ss[6:9]+'  '+ss[21:24]+'\n'+\
            ss[9:12]+'  '+ss[24:27]+'\n'+\
            ss[12:15]+' '+ss[27:31]
        else:
            selectA = ss[0:3]+'  '+ss[15:18]+'  '+ss[31:35]+'\n'+\
            ss[3:6]+'  '+ss[18:21]+'  '+ss[35:39]+'\n'+\
            ss[6:9]+'  '+ss[21:24]+'  '+ss[39:43]+'\n'+\
            ss[9:12]+'  '+ss[24:27]+'  '+ss[43:47]+'\n'+\
            ss[12:15]+' '+ss[27:31]+'  '+ss[47:51]
        self.QMyanswers.setFontPointSize(19)
        self.QMyanswers.setText(selectA)
        

    def down_push(self):
        table_id = download()
        self.Qtable_id.setText(table_id)

    def table_read(self):
        global questionId, red_word, length, question_id
        question_id = 0
        table_id = self.Qtable_id.text()
        [questionId, red_word, length] = read_html(table_id)
        if length:
            self.search__answer(0)
        else:
            self.QquestionID.setText(u'        文件不存在       ')

    def question_last(self):
        global question_id
        question_id -= 1
        if question_id < 0:
            question_id = 0
        self.search__answer(question_id)

    def question_next(self):
        global question_id, length
        question_id += 1
        if question_id > length-1:
            question_id = length-1
        self.search__answer(question_id)

    def search__answer(self, question_id):
        global t_dict, red_word, copy_id, db_answer, questionId
        copy_id = 0
        self.QquestionID.setText(u'  第 '+str(question_id+1)+' 题  |  共 '+str(length)+' 题  ')
        self.Qred_show.setText(u' 题中红字 --> '+red_word[question_id][0:70])
        """执行查询操作"""
        table_id = self.Qtable_id.text()
        table_id_m = t_dict[table_id]
        db_answer = self.msql.query(table_id_m, questionId[question_id], red_word[question_id])
        # 展示查询的结果
        if db_answer:
            db_answer = ' '.join([n for t in db_answer for n in t])
            db_answer = db_answer.split(',')
        else:
            red_word_list = red_word[question_id].split(',')
            db_answer = doit(questionId[question_id], red_word_list)
        self.show_answer(question_id)

    def show_answer(self,question_id):
        global red_word, copy_id, db_answer, questionId
        db_answer0 = db_answer[0]
        self.Qcopy_line.setText(u'复制->'+db_answer0[0:20])
        pyperclip.copy(db_answer0)
        db_answer_edit = '\n'.join(db_answer)
        self.Qanswers.setText(db_answer_edit)
        self.QMyanswers.setText('///')
        red_word_list = red_word[question_id].split(',')
        if db_answer[0] == "nocode":
            self.Qanswers.setText(u'没有找到答案！题号: '+questionId[question_id]+
                '\n红字个数： '+str(len(red_word_list))+
                '\n红字： '+red_word[question_id]+
                '\n请编程……：\n')
        self.copy_next()
        self.copy_next()

    def copy_last(self):
        global copy_id, db_answer
        if db_answer:
            copy_id -= 1
            if copy_id < 0:
                copy_id = 0
            db_answers_id = db_answer[copy_id]
            self.Qcopy_line.setText(u'复制->'+db_answers_id[0:20])
            pyperclip.copy(db_answers_id)

    def copy_next(self):
        global copy_id, db_answer
        if db_answer:
            copy_id += 1
            if copy_id > len(db_answer)-1:
                copy_id = len(db_answer)-1
            db_answers_id = db_answer[copy_id]
            self.Qcopy_line.setText(u'复制->'+db_answers_id[0:20])
            pyperclip.copy(db_answers_id)

    def solve__answer(self):
        global questionId, db_answer
        mywrite = self.Qwirte.text()
        mywrite = mywrite.split(' ')
        db_answer = doit(questionId[question_id], mywrite)
        self.show_answer(question_id)

    def solve__frac(self):
        number = self.Qfrac.text()
        frc = circulator_to_fraction(number)
        h = hcf(frc[0],frc[1])
        frc_s = str(int(frc[0]/h))+'/'+str(int(frc[1]/h))
        self.Qwirte.setText(frc_s)

    def add__answer(self):
        """执行添加新题操作"""
        global question_id, questionId, red_word
        table_id = self.Qtable_id.text()
        table_id_m = t_dict[table_id]
        myanswers = self.QMyanswers.toPlainText()
        myanswers = '\n'+myanswers
        myanswers = myanswers.replace('\n',',').replace(';', ',')
        val = [questionId[question_id], red_word[question_id], myanswers]
        self.msql.insert(table_id_m, val)
        time.sleep(0.02)
        self.question_next()

    def del__answer(self):
        """执行从库中删除此答案的操作"""
        global  question_id,questionId, red_word
        rely = QMessageBox.question(self,"删除","确定将此答案从题库中删除吗？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if rely == QMessageBox.Yes:
            table_id = self.Qtable_id.text()
            table_id_m = t_dict[table_id]
            self.msql.dele(table_id_m, questionId[question_id], red_word[question_id])
            time.sleep(0.02)
            self.search__answer(question_id)


    def same__answer(self):
        """查找同类题，以供参考"""
        global t_dict, red_word, copy_id, db_answer, questionId
        copy_id = 0
        self.QMyanswers.setText('///')
        self.QquestionID.setText(u'  第 '+str(question_id+1)+' 题  |  共 '+str(length)+' 题  ')
        self.Qred_show.setText(u' 题中红字 --> '+red_word[question_id][0:70])
        """执行查询操作"""
        table_id = self.Qtable_id.text()
        table_id_m = t_dict[table_id]
        db_answer = self.msql.query_same(table_id_m, questionId[question_id])
        # 展示查询的结果
        if db_answer:
            db_answer = '$'.join([n for t in db_answer for n in t])
            db_red_ans = db_answer.split('$')
            db_red = db_red_ans[0]
            db_answer = db_red_ans[1]
            db_answer = db_answer.split(',')
            db_answer0 = db_answer[0]
            self.Qcopy_line.setText(u'复制->'+db_answer0[0:20])
            pyperclip.copy(db_answer0)
            db_answer_edit = '///red/'+db_red+'\n'.join(db_answer)
            self.Qanswers.setText(db_answer_edit)
        else:
            self.Qanswers.setText(u'没有找到答案！请补充……')
            self.Qcopy_line.setText(u'复制->')
            self.question_next()
        


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop直到exit()被调用,即运行程序
    sys.exit(app.exec_()) # 前面的show方法并没有显示，通过此时的层层调用才显示

