import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMenuBar, QMenu
from untitled import *
import time
import xlsxwriter
import os
import back

iter = 0
time0 = 0
timer = 0
nomer = 0
pos1 = 0
pos2 = 0
people = 0
name2 = 0
name1 = 0
txt = ""
ph = os.path.abspath(os.path.dirname(sys.argv[0]))
path = os.path.join(ph, "file" + str(nomer) + ".xlsx")


while True:
    if os.path.exists(path):
        nomer = nomer + 1
        path = os.path.join(ph, "file" + str(nomer) + ".xlsx")
    if os.path.exists(path) == False:
        break
workbook = xlsxwriter.Workbook(path)
worksheet = workbook.add_worksheet()



def start():
    if ui.plainTextEdit.toPlainText() == "":
        ui.label.setStyleSheet("background-color: red")

    if ui.plainTextEdit.toPlainText() != "":
        ui.label.setStyleSheet("background-color: green")
        ui.pushButton_4.setEnabled(True)


def absolut():
    global name1
    global name2
    if ui.plainTextEdit_2.toPlainText() == "":
        ui.label_2.setStyleSheet("background-color: normal")
        name2 = 0
    if ui.plainTextEdit_2.toPlainText() != "":
        try:
            ui.label_2.setStyleSheet("background-color: green")
            name1 = int(ui.plainTextEdit_2.toPlainText())
            name2 = 1
        except ValueError:
            ui.label_2.setStyleSheet("background-color: red")


def delete():
    global pos1
    if pos1 > 0:
        global people
        quest = QMessageBox()
        quest.setWindowTitle("подтверждение удаления")
        quest.setText("вы уверены?")
        quest.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        req = quest.exec_()
        if req == QMessageBox.Yes:
            people = people - 1
            worksheet.write(pos1 - 1, pos2, " ")
            worksheet.write(pos1 - 1, pos2 + 1, " ")
            ui.label_4.setText(str(people))
            quest.close()
            pos1 = pos1 - 1

            ui.label_6.setText("")
        if req == QMessageBox.No:
            quest.close()

    if pos1 == 0:
        pass


def go():
    global iter
    global time0
    global timer
    global pos1
    global pos2
    global people
    if iter % 2 == 0:
        time0 = time.time()
        ui.pushButton_4.setStyleSheet('color: green')
    if iter % 2 == 1:
        timer = round(time.time() - time0, 2)
        ui.label_6.setText(str(timer) + " " + str(ui.plainTextEdit.toPlainText()))
        if name2 == 1:
            timer = round(name1 - timer, 2)
        worksheet.write(pos1, pos2, ui.plainTextEdit.toPlainText())
        worksheet.write(pos1, pos2 + 1, timer)
        pos1 = pos1 + 1
        people = people + 1
        ui.label_4.setText(str(people))
        ui.label.setStyleSheet("background-color: normal")
        ui.pushButton_4.setStyleSheet('color: normal')
        ui.plainTextEdit.setPlainText("")
        ui.pushButton_4.setEnabled(False)
    iter = iter + 1

def new():
    print("!")





def ti():
    ui.centralwidget.show()



try:

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_4.setEnabled(False)
    MainWindow.showMaximized()

    ui.pushButton.clicked.connect(start)
    ui.pushButton_2.clicked.connect(absolut)
    ui.pushButton_3.clicked.connect(delete)
    ui.pushButton_4.clicked.connect(go)

    ui.menubar.setNativeMenuBar(False)
    file = ui.menubar.addMenu("File")
    pr = file.addAction("примеры")
    st = file.addAction("время")
    pr.triggered.connect(new)
    st.triggered.connect(ti)
    ui.menubar.show()


    ui.statusbar.showMessage("123")
    ui.statusbar.show()

    sys.exit(app.exec())

finally:
    workbook.close()

