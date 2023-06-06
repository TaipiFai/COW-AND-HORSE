#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

qls = []

class Quest():
    def __init__(self, qes, rih_an, wr1, wr2, wr3):
        self.qes = qes
        self.rih_an = rih_an
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3

def shw_res():
    rgb.hide()
    rg1.show()
    bt1.setText('Следующий вопрос')

def shw_qes():
    rgb.show()
    rg1.hide()
    bt1.setText('Ответить')
    bgr.setExclusive(False)
    an1.setChecked(False)
    an2.setChecked(False)
    an3.setChecked(False)
    an4.setChecked(False)
    bgr.setExclusive(True)

def ask(q:Quest):
    answers[0].setText(q.rih_an)
    answers[1].setText(q.wr1)
    answers[2].setText(q.wr2)
    answers[3].setText(q.wr3)
    qs1.setText(q.qes)
    ran.setText(q.rih_an)
    shw_qes()

def nam():
    if answers[0].isChecked():
        shw_cor('Правильно!')
        win.scr += 1
    else:
        shw_cor('Неправильно!')

def shw_cor(res):
    var.setText(res)
    shw_res()

def nex_qes():
    win.cur_qes += 1
    if win.cur_qes == len(qls):
        exit()
    else:
        ask(qls[win.cur_qes])

def click():
    if bt1.text() == 'Ответить':
        nam()
    elif bt1.text() == 'Следующий вопрос':
        nex_qes()
    else:
        app.quit()

def exit():
    rg1.hide()
    qs1.setText('Правильных ответов ' + str(win.scr) + ' из ' + str(len(qls)))
    bt1.setText('Завершить')




#
app = QApplication([])
win = QWidget()
win.resize(600, 200)

win.scr = 0
#
win.setWindowTitle('Memory Card')

rgb = QGroupBox('Варианты ответов')
an1 = QRadioButton('Энцы')
an2 = QRadioButton('Смурфы')
an3 = QRadioButton('Чулымцы')
an4 = QRadioButton('Алеуты')

lh1 = QHBoxLayout()
lv1 = QVBoxLayout()
lv2 = QVBoxLayout()

lv1.addWidget(an1)
lv1.addWidget(an2)
lv2.addWidget(an3)
lv2.addWidget(an4)

lh1.addLayout(lv1)
lh1.addLayout(lv2)

rgb.setLayout(lh1)

#
rg1 = QGroupBox('Результат теста')
var = QLabel('Правильно/Неправильно')
ran = QLabel('Правильный ответ')
vli = QVBoxLayout()
vli.addWidget(var, alignment = (Qt.AlignLeft | Qt.AlignTop))
vli.addWidget(ran, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
rg1.setLayout(vli)
#

#
qs1 = QLabel('Какой национальности не существует?')

lha = QHBoxLayout()
lhb = QHBoxLayout()
lhc = QHBoxLayout()

lva = QVBoxLayout()

bt1 = QPushButton('Ответить')

lha.addWidget(qs1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
lhc.addWidget(bt1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

lhb.addWidget(rgb)
lhb.addWidget(rg1)

rg1.hide()
rgb.show()

answers = [an1, an2, an3, an4]

bgr = QButtonGroup()

bgr.addButton(an1)
bgr.addButton(an2)
bgr.addButton(an3)
bgr.addButton(an4)

lva.addLayout(lha)
lva.addLayout(lhb)
lva.addLayout(lhc)

win.setLayout(lva)

qls.append(Quest('Сколько лошадиных сил у Нивы?', '80', '50', '95', '100'))
qls.append(Quest('Сколько кирпичей в 10-этажном доме','28458', '13512', '8230', '20560'))
qls.append(Quest('В какой серии стал титаном командующий Пиксис из атаки титанов?','4 сезон 22 серия', '3 сезон 5 серия', '4 сезон 16 серия', '3 сезон 19 серия'))
qls.append(Quest('В каком году Пётр 1 ушёл в мир иной','я не знаю', '1473', 'да кому это надо?', '1629'))
qls.append(Quest('Сколько стран в мире (Хрю не считается)', '192','193','186', '172'))
qls.append(Quest('Сколько ангелов в тайтле "Евангелион"', '17', '20', '15', '19'))
qls.append(Quest('Знай, что ангелы не спят', 'Они смотрят на тебя', 'Увидишь небо ты в глазах ребенка', 'Давай, найди свой новый путь', 'Они любят тебя'))
qls.append(Quest('Угадай число', '15', '19', '234567', 'ропид'))

q = Quest('Государственный язык Бразили', 'Португальский', 'Бразильский', 'Русский','Итальянский')
ask(q)

win.cur_qes = -1
nex_qes()

bt1.clicked.connect(click)

win.show()
app.exec_()