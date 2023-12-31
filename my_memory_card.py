from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox,
    QPushButton, QHBoxLayout, 
    QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup)
from random import shuffle, randint
app = QApplication([])

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык в России', 'Русский', 'Англисский', 'Итальянский', 'Немецкий'))
question_list.append(Question('Какого цвета нет во флаге России', 'Зелёный', 'Белый', 'Синий', 'Красный'))
question_list.append(Question('Национальность в России', 'Русские', 'Итальянцы', 'Немцы', 'Французы'))
question_list.append(Question('Столица России', 'Москва', 'Питер', 'Пенза', 'Самара'))
question_list.append(Question('Сколько месяцев в году', '12', '7', '6', '0'))
question_list.append(Question('В какой год в феврале 29 дней', 'Високосный', 'Обычный', 'ааа.......', '2001'))
question_list.append(Question('Первая женщина в космосе', 'Терешкова', 'Онегин', 'Моя мама', 'Сибярикова'))
question_list.append(Question('В каком гооду открыт Московский институт', '1755', '1333', '775', '820'))

window = QWidget()
window.setWindowTitle('Carrot')
btn_OK = QPushButton ('Ответить')

lb_Question = QLabel ('В каком году была основана Москва?')
RadioGroupBox = QGroupBox ('Варианты ответов')
rbtn_1 = QRadioButton ('1147')
rbtn_2 = QRadioButton ('1242')
rbtn_3 = QRadioButton ('1861')
rbtn_4 = QRadioButton ('1943')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1= QHBoxLayout()
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))

layout_line3.addStretch (1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_line2.addWidget(RadioGroupBox)
layout_card = QVBoxLayout ()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addSpacing(5)
layout_card.addLayout(layout_line3, stretch=8)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show_correct('правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросо:', window.total, '\n-Правильных отетов:', window.score)
        print('Рейтинг:', (window.score/window.total*100),'%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100),'%')
def next_question():
    '''window.cur_question = window.cur_question + 1'''
    window.total += 1
    print('Статистика\n-Всего вопросо:', window.total, '\n-Правильных отетов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    '''if window.cur_question >= len(question_list):
       window.cur_question = 0'''
    ask(q) 

def click_OK():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()
q=Question('Как звали попугая из мультика"Кеша"', 'Кеша', 'doq', 'собака', 'Артём')

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = -1

btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()

