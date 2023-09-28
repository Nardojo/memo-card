from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
#создание PushButton
button_menu = QPushButton('Меню')
button_sleep = QPushButton('Відпочити')
button_otvet = QPushButton('Відповісти')
#создание BoxLayout
main_line=QHBoxLayout()
v_line = QVBoxLayout()
v_line2 = QVBoxLayout()

#создание RadioButtoт
radbut1 = QRadioButton()
radbut2 = QRadioButton()
radbut3 = QRadioButton()
radbut4 = QRadioButton()
#прикрипление линий
v_line.addWidget(radbut1,alignment = Qt.AlignCenter)
v_line.addWidget(radbut2,alignment = Qt.AlignCenter)
v_line2.addWidget(radbut3,alignment = Qt.AlignCenter)
v_line2.addWidget(radbut4,alignment = Qt.AlignCenter)
#прикрипление вертикальной линий к горизонтальной
main_line.addLayout(v_line)
main_line.addLayout(v_line2)
#обьединение кнопок в группы
Radios = QButtonGroup()
Radios.addButton(radbut1)
Radios.addButton(radbut2)
Radios.addButton(radbut3)
Radios.addButton(radbut4)
#Рамка кнопок
RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroupBox.setLayout(main_line)
#spinbox
box_minutes = QSpinBox()
box_Minutes.setValue(30)
