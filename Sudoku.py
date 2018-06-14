# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
sys.setrecursionlimit(1000000000)
class Ui_Sudoku(object):
    def setupUi(self, Sudoku):
        Sudoku.setObjectName("Sudoku")
        Sudoku.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Sudoku)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 21, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 90, 21, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 90, 21, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 90, 21, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 90, 21, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(320, 90, 21, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 90, 21, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 90, 21, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(420, 90, 21, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 120, 20, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(190, 120, 21, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(220, 120, 21, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 120, 21, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(290, 120, 21, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(320, 120, 21, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(360, 120, 21, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(390, 120, 21, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(420, 120, 21, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(160, 150, 21, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(190, 150, 21, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(220, 150, 21, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(260, 150, 21, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(290, 150, 21, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setGeometry(QtCore.QRect(320, 150, 21, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(360, 150, 21, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setGeometry(QtCore.QRect(390, 150, 20, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setGeometry(QtCore.QRect(420, 150, 21, 20))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_28.setGeometry(QtCore.QRect(160, 190, 21, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_29.setGeometry(QtCore.QRect(190, 190, 21, 20))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_30.setGeometry(QtCore.QRect(220, 190, 21, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_31.setGeometry(QtCore.QRect(260, 190, 21, 20))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_32.setGeometry(QtCore.QRect(290, 190, 21, 20))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setGeometry(QtCore.QRect(320, 190, 21, 20))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_34.setGeometry(QtCore.QRect(360, 190, 21, 20))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_35.setGeometry(QtCore.QRect(390, 190, 21, 20))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_36.setGeometry(QtCore.QRect(420, 190, 20, 20))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_37.setGeometry(QtCore.QRect(160, 220, 21, 20))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_38.setGeometry(QtCore.QRect(190, 220, 21, 20))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_39.setGeometry(QtCore.QRect(220, 220, 21, 20))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_40.setGeometry(QtCore.QRect(260, 220, 21, 20))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_41.setGeometry(QtCore.QRect(290, 220, 21, 20))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_42.setGeometry(QtCore.QRect(320, 220, 21, 20))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_43.setGeometry(QtCore.QRect(360, 220, 21, 20))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_44.setGeometry(QtCore.QRect(390, 220, 21, 20))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_45.setGeometry(QtCore.QRect(420, 220, 21, 20))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_46.setGeometry(QtCore.QRect(160, 250, 21, 20))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_47.setGeometry(QtCore.QRect(190, 250, 21, 20))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_48.setGeometry(QtCore.QRect(220, 250, 21, 20))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_49.setGeometry(QtCore.QRect(260, 250, 21, 20))
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_50.setGeometry(QtCore.QRect(290, 250, 21, 20))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_51.setGeometry(QtCore.QRect(320, 250, 21, 20))
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_52.setGeometry(QtCore.QRect(360, 250, 21, 20))
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_53.setGeometry(QtCore.QRect(390, 250, 21, 20))
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_54.setGeometry(QtCore.QRect(420, 250, 21, 20))
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_55.setGeometry(QtCore.QRect(160, 290, 21, 20))
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_56.setGeometry(QtCore.QRect(190, 290, 21, 20))
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_57.setGeometry(QtCore.QRect(220, 290, 21, 20))
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_58.setGeometry(QtCore.QRect(260, 290, 21, 20))
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_59.setGeometry(QtCore.QRect(290, 290, 21, 20))
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_60.setGeometry(QtCore.QRect(320, 290, 21, 20))
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_61.setGeometry(QtCore.QRect(360, 290, 21, 21))
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_62.setGeometry(QtCore.QRect(390, 290, 21, 21))
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_63.setGeometry(QtCore.QRect(420, 290, 21, 21))
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_64.setGeometry(QtCore.QRect(160, 320, 21, 21))
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_65.setGeometry(QtCore.QRect(190, 320, 21, 21))
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_66.setGeometry(QtCore.QRect(220, 320, 21, 21))
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.lineEdit_67 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_67.setGeometry(QtCore.QRect(260, 320, 21, 21))
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.lineEdit_68 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_68.setGeometry(QtCore.QRect(290, 320, 21, 21))
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.lineEdit_69 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_69.setGeometry(QtCore.QRect(320, 320, 21, 21))
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.lineEdit_70 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_70.setGeometry(QtCore.QRect(360, 320, 21, 21))
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.lineEdit_71 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_71.setGeometry(QtCore.QRect(390, 320, 21, 21))
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.lineEdit_72 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_72.setGeometry(QtCore.QRect(420, 320, 21, 21))
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.lineEdit_73 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_73.setGeometry(QtCore.QRect(160, 350, 21, 21))
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.lineEdit_74 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_74.setGeometry(QtCore.QRect(190, 350, 21, 21))
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.lineEdit_75 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_75.setGeometry(QtCore.QRect(220, 350, 21, 21))
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.lineEdit_76 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_76.setGeometry(QtCore.QRect(260, 350, 21, 21))
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.lineEdit_77 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_77.setGeometry(QtCore.QRect(290, 350, 21, 21))
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.lineEdit_78 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_78.setGeometry(QtCore.QRect(320, 350, 21, 21))
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.lineEdit_79 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_79.setGeometry(QtCore.QRect(360, 350, 21, 21))
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.lineEdit_80 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_80.setGeometry(QtCore.QRect(390, 350, 21, 21))
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.lineEdit_81 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_81.setGeometry(QtCore.QRect(420, 350, 21, 21))
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(520, 90, 211, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")
        Sudoku.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Sudoku)
        self.statusbar.setObjectName("statusbar")
        Sudoku.setStatusBar(self.statusbar)

        self.retranslateUi(Sudoku)
        QtCore.QMetaObject.connectSlotsByName(Sudoku)

    def retranslateUi(self, Sudoku):
        _translate = QtCore.QCoreApplication.translate
        Sudoku.setWindowTitle(_translate("Sudoku", "MainWindow"))
        self.pushButton.setText(_translate("Sudoku", "PushButton"))

class Myform(QMainWindow, Ui_Sudoku):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)

    def calc(self):
        a = []
        for i in range(81):
            if i == 0:
                a.append(self.lineEdit)
            else:
                a.append(eval('self.lineEdit_' + str(i+1)))
        b = []
        for i in a:
            content = i.text()
            if content == '':
                b.append(0)
            else:
                b.append(int(content))
        print(b)
        #b has the list of numbers now
        stack = []
        for i in range(81):
            if b[i] == 0:
                stack.append(i)
            else:
                print('Not empty')
        stackp = 0
        print(stack)
        self.ca(b, stack, stackp, 0)

    def ca(self, b, stack, stackp, times):
        times += 1
        if times == 4130:
            sn = 0
        self.plainTextEdit.setPlainText('Times:' + str(times))
        QApplication.processEvents()
        if stackp == 81:
            print('End')
            exit(0)
        if stackp == -1:
            self.plainTextEdit.setPlainText('No answer')

        top = stack[stackp]
        b[top] += 1

        if top == 0:
            s = 'self.lineEdit'
        else:
            s = 'self.lineEdit_' + str(stack[stackp] + 1)
        s = eval(s)
        s.setText(str(b[top]))
        QApplication.processEvents()

        if b[top] == 10:
            b[top] = 0
            stackp -= 1

            """if top == 0:
                s = 'self.lineEdit'
            else:
                s = 'self.lineEdit_' + str(stack[stackp] + 1)
            s = eval(s)
            s.setText(str(b[top]))
            QApplication.processEvents()"""

            self.ca(b, stack, stackp, times)
        elif(self.judge(b)) == 1:
            stackp += 1
            self.ca(b, stack, stackp,times)
        else:
            self.ca(b, stack, stackp, times)

    def judge(self, d):
        result = []
        for i in range(9):
            a = []
            b = []
            c = []
            for j in range(9):
                a.append(d[j + i * 9])
                b.append(d[j * 9 + i])
            if i < 3:
                c.append(d[0 + i * 3])
                c.append(d[1 + i * 3])
                c.append(d[2 + i * 3])

                c.append(d[9 + i * 3])
                c.append(d[10 + i * 3])
                c.append(d[11 + i * 3])

                c.append(d[18 + i * 3])
                c.append(d[19 + i * 3])
                c.append(d[20 + i * 3])
            elif i > 5:
                c.append(d[54 + (i - 6) * 3])
                c.append(d[55 + (i - 6) * 3])
                c.append(d[56 + (i - 6) * 3])

                c.append(d[63 + (i - 6) * 3])
                c.append(d[64 + (i - 6) * 3])
                c.append(d[65 + (i - 6) * 3])

                c.append(d[72 + (i - 6) * 3])
                c.append(d[73 + (i - 6) * 3])
                c.append(d[74 + (i - 6) * 3])
            else:
                c.append(d[27 + (i - 3) * 3])
                c.append(d[28 + (i - 3) * 3])
                c.append(d[29 + (i - 3) * 3])

                c.append(d[36 + (i - 3) * 3])
                c.append(d[37 + (i - 3) * 3])
                c.append(d[38 + (i - 3) * 3])

                c.append(d[45 + (i - 3) * 3])
                c.append(d[46 + (i - 3) * 3])
                c.append(d[47 + (i - 3) * 3])

            #print(c)
            result.append(self.check(a))
            result.append(self.check(b))
            result.append(self.check(c))

        #print(result)
        if 0 in result:
            return 0
        else:
            return 1



    def check(self, a):
        for i in range(9):
            if a[i] == 0:
                pass
            else:
                for j in a:
                    if a.index(j) == i:
                        pass
                    elif j != a[i]:
                        pass
                    elif j == a[i]:
                        return 0
                    else:
                        print('unexpected error occured')
        return 1


        #self.plainTextEdit.setPlainText(str(a) + str(b) + str(c))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    w.show()
    app.exec_()