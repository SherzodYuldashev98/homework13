'''1) RadioButtondan foydalanib 5ta test tuzing. Agar to'g'ri javob belgilansa +1bal qo'shilsin
va agar noto'g'ri bo'lsa bal qo'shilmasin va oxirida umumiy bali chiqsin.'''
#1-task
'''
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtWidgets import QRadioButton,QPushButton,QButtonGroup,QMessageBox
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
app.setStyle("Fusion")
class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setFixedSize(800,900)
        self.start()
        self.correct=0
        #self.setStyleSheet("background-color:pink")
    def start(self):
        self.question1=QLabel("1. C++ tilida massiv indeksi nechadan boshlanadi?",self)
        self.font(self.question1,50,50)
        self.a1=QRadioButton("0 dan",self)
        self.font(self.a1,80,80)
        self.b1=QRadioButton("1 dan",self)
        self.font(self.b1,80,110)
        self.c1=QRadioButton("2 dan",self)
        self.font(self.c1,80,140)

        self.g1=QButtonGroup(self)
        self.g1.addButton(self.a1)
        self.g1.addButton(self.b1)
        self.g1.addButton(self.c1)

        self.question2=QLabel("2. C++ dasturi qaysi tilga asoslanib tuzilgan?",self)
        self.font(self.question2,50,170)
        self.a2=QRadioButton("B va BCPL tillariga",self)
        self.font(self.a2,80,200)
        self.b2=QRadioButton("C tiliga",self)
        self.font(self.b2,80,230)
        self.c2=QRadioButton("BCPL tiliga",self)
        self.font(self.c2,80,260)

        self.g2=QButtonGroup(self)
        self.g2.addButton(self.a2)
        self.g2.addButton(self.b2)
        self.g2.addButton(self.c2)

        self.question3=QLabel("3. Massiv – bu …",self)
        self.font(self.question3,50,290)
        self.a3=QRadioButton("Elementlarning tartiblangan strukturasi",self)
        self.font(self.a3,80,320)
        self.b3=QRadioButton("Elementlarning tartiblanmagan strukturasi",self)
        self.font(self.b3,80,350)
        self.c3=QRadioButton("Elementlarning tartiblangan va tartiblanmagan strukturalari",self)
        self.font(self.c3,80,380)

        self.g3=QButtonGroup(self)
        self.g3.addButton(self.a3)
        self.g3.addButton(self.b3)
        self.g3.addButton(self.c3)

        self.question4=QLabel("4. Pythonda kiritish funksiyasi?",self)
        self.font(self.question4,50,410)
        self.a4=QRadioButton("print()",self)
        self.font(self.a4,80,440)
        self.b4=QRadioButton("input()",self)
        self.font(self.b4,80,470)
        self.c4=QRadioButton("scanf()",self)
        self.font(self.c4,80,500)

        self.g4=QButtonGroup(self)
        self.g4.addButton(self.a4)
        self.g4.addButton(self.b4)
        self.g4.addButton(self.c4)

        self.question5=QLabel("5. Pythonda chiqarish funksiyasi?",self)
        self.font(self.question5,50,530)
        self.a5=QRadioButton("print()",self)
        self.font(self.a5,80,560)
        self.b5=QRadioButton("cout<<",self)
        self.font(self.b5,80,590)
        self.c5=QRadioButton("scanf()",self)
        self.font(self.c5,80,620)

        self.g5=QButtonGroup(self)
        self.g5.addButton(self.a5)
        self.g5.addButton(self.b5)
        self.g5.addButton(self.c5)

        result=QPushButton("Result",self)
        result.setFont(QFont("Times",20))
        result.move(330,800)
        result.clicked.connect(self.run)

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",12))
        obj.move(x,y)
        obj.adjustSize()

    def run(self):
        if self.a1.isChecked():
            self.correct+=1
        if self.b2.isChecked():
            self.correct+=1
        if self.c3.isChecked():
            self.correct+=1
        if self.b4.isChecked():
            self.correct+=1
        if self.a5.isChecked():
            self.correct+=1
        win=QMessageBox(self)
        win.setWindowTitle("Result")
        win.setText("Correct answer: "+str(win1.correct)+"\n")
        win.setText(win.text()+"Incorrect answer: "+str(5-win1.correct))
        win.setFont(QFont("Times",16))
        win.show()

win1=Window1()
win1.show()
sys.exit(app.exec_())
'''
'''
2) Restoran menyusini tuzuvchi dastur tuzing. 
Unda 1-taomlar ro'yhati, 2-taomlar ro'yhati, ichimliklar va desert ro'yhatidagi kamida
5tadan ma'lumotlarni CheckBox orqali tanlaydi va oxirida Chek ro'yhati chiqarilsin. 
Chek quyidagi ko'rinishda bo'lishi kerak:
1-taomlar: tanlanganlar ro'yhati (narxlari bilan)
2-taomlar: tanlanganlar ro'yhati (narxlari bilan)
Ichimliklar: tanlanganlar ro'yhati (narxlari bilan)
Desert: tanlanganlar ro'yhati (narxlari bilan)
'''
#2-task

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QCheckBox,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
app.setStyle("Fusion")
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bacardi restaurant")
        self.setFixedSize(1000,900)
        self.start()
        self.setStyleSheet("color:orange; background-color:black")
        self.price=0
    def start(self):
        m=QLabel("Bacardi restaurant menu!!!",self)
        m.setFont(QFont("Harlow Solid Italic",34))
        m.move(230,20)
        menu1=QLabel("Starters",self)
        menu1.setFont(QFont("Algerian",20))
        menu1.move(50,120)
        
        self.starters1=QCheckBox("Tomato soup.............$10.00",self)
        self.font(self.starters1,50,170)
        self.starters2=QCheckBox("Chicken soup.............$14.00",self)
        self.font(self.starters2,50,220)
        self.starters3=QCheckBox("Guacaole salad.............$16.00",self)
        self.font(self.starters3,50,270)
        self.starters4=QCheckBox("Chicken salad.............$8.00",self)
        self.font(self.starters4,50,320)
        self.starters5=QCheckBox("Nachos Plain.............$17.00",self)
        self.font(self.starters5,50,370)
        
        menu2=QLabel("Main Courses",self)
        menu2.setFont(QFont("Algerian",20))
        menu2.move(500,120)
        self.meal1=QCheckBox("Turkey and ham pie.............$10.00",self)
        self.font(self.meal1,500,170)
        self.meal2=QCheckBox("Vegetable pasta.............$14.00",self)
        self.font(self.meal2,500,220)
        self.meal3=QCheckBox("Beef kebab.............$40.00",self)
        self.font(self.meal3,500,270)
        self.meal4=QCheckBox("Grilled fish and potatoes.............$10.00",self)
        self.font(self.meal4,500,320)
        self.meal5=QCheckBox("Chicken and rice.............$10.00",self)
        self.font(self.meal5,500,370)

        menu3=QLabel("Drinks",self)
        menu3.setFont(QFont("Algerian",20))
        menu3.move(50,470)
        self.drink1=QCheckBox("Mineral Water.............$2.00",self)
        self.font(self.drink1,50,520)
        self.drink2=QCheckBox("Fresh fruit juice.............$7.00",self)
        self.font(self.drink2,50,570)
        self.drink3=QCheckBox("Coffee.............$5.00",self)
        self.font(self.drink3,50,620)
        self.drink4=QCheckBox("Green tea.............$3.00",self)
        self.font(self.drink4,50,670)
        self.drink5=QCheckBox("Wines.............$10.00",self)
        self.font(self.drink5,50,720)

        menu4=QLabel("Desserts",self)
        menu4.setFont(QFont("Algerian",20))
        menu4.move(500,470)
        self.dessert1=QCheckBox("Fruit and cream.............$5.00",self)
        self.font(self.dessert1,500,520)
        self.dessert2=QCheckBox("Ice cream.............$7.00",self)
        self.font(self.dessert2,500,570)
        self.dessert3=QCheckBox("Chocolate cake.............$15.00",self)
        self.font(self.dessert3,500,620)
        self.dessert4=QCheckBox("Strawberry cake.............$13.00",self)
        self.font(self.dessert4,500,670)
        self.dessert5=QCheckBox("Apple pie.............$12.00",self)
        self.font(self.dessert5,500,720)

        order=QPushButton("ordering",self)
        self.font(order,450,800)
        order.setStyleSheet("color:black; background-color:orange")
        order.clicked.connect(self.run)
    def font(self,obj,x,y):
        obj.setFont(QFont("Brush Script MT",18))
        obj.move(x,y)
    def run(self):
        miniwindow=QMessageBox(self)
        miniwindow.setWindowTitle("Total price")
        if self.starters1.isChecked():
            miniwindow.setText(miniwindow.text()+self.starters1.text()+"\n")
        if self.starters2.isChecked():
            miniwindow.setText(miniwindow.text()+self.starters2.text()+"\n")
        if self.starters3.isChecked():
            miniwindow.setText(miniwindow.text()+self.starters3.text()+"\n")
        if self.starters4.isChecked():
            miniwindow.setText(miniwindow.text()+self.starters4.text()+"\n")
        if self.starters5.isChecked():
            miniwindow.setText(miniwindow.text()+self.starters5.text()+"\n")

        if self.meal1.isChecked():
            miniwindow.setText(miniwindow.text()+self.meal1.text()+"\n")
        if self.meal2.isChecked():
            miniwindow.setText(miniwindow.text()+self.meal2.text()+"\n")
        if self.meal3.isChecked():
            miniwindow.setText(miniwindow.text()+self.meal3.text()+"\n")
        if self.meal4.isChecked():
            miniwindow.setText(miniwindow.text()+self.meal4.text()+"\n")
        if self.meal5.isChecked():
            miniwindow.setText(miniwindow.text()+self.meal5.text()+"\n")

        if self.drink1.isChecked():
            miniwindow.setText(miniwindow.text()+self.drink1.text()+"\n")
        if self.drink2.isChecked():
            miniwindow.setText(miniwindow.text()+self.drink2.text()+"\n")
        if self.drink3.isChecked():
            miniwindow.setText(miniwindow.text()+self.drink3.text()+"\n")
        if self.drink4.isChecked():
            miniwindow.setText(miniwindow.text()+self.drink4.text()+"\n")
        if self.drink5.isChecked():
            miniwindow.setText(miniwindow.text()+self.drink5.text()+"\n")

        if self.dessert1.isChecked():
            miniwindow.setText(miniwindow.text()+self.dessert1.text()+"\n")
        if self.dessert2.isChecked():
            miniwindow.setText(miniwindow.text()+self.dessert2.text()+"\n")
        if self.dessert3.isChecked():
            miniwindow.setText(miniwindow.text()+self.dessert3.text()+"\n")
        if self.dessert4.isChecked():
            miniwindow.setText(miniwindow.text()+self.dessert4.text()+"\n")
        if self.dessert5.isChecked():
            miniwindow.setText(miniwindow.text()+self.dessert5.text()+"\n")
        temp=(miniwindow.text()).split("\n")
        for i in temp:
            if i!="":
                k=i.split("$")
                self.price=self.price+float(k[1])
        miniwindow.setText(miniwindow.text()+"Total price: $"+str(self.price))
        miniwindow.setFont(QFont("Adobe Ming Std L",16))
        miniwindow.setStyleSheet("color:black; background-color:white")
        miniwindow.show()
        self.price=0
win=Window()
win.show()
sys.exit(app.exec_())

'''
3) ComboBox orqali Tug'ilgan viloyatini, Tuman yoki shaharni, Jinsini va Millatini
tanlasin va Barcha tanlangan haqida ma'lumot chiqarilsin.
'''
#3-task
'''
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QComboBox,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3-task")
        self.setFixedSize(700,600)
        self.start()
    def start(self):
        self.region=QLabel("Select the region of birth",self)
        self.font(self.region,50,50)
        self.combo1=QComboBox(self)
        self.combo1.addItems(["","Toshkent","Samarqand","Navoiy","Xorazm"])
        self.font(self.combo1,50,100)

        self.district=QLabel("Select the district of birth",self)
        self.font(self.district,50,150)
        self.comboc=QComboBox(self)
        self.comboc.addItems(["","Chilonzor","Yunusobod","Yakkasaroy","Mirobod"])
        self.font(self.comboc,50,200)

        self.gender=QLabel("Choose your gender",self)
        self.font(self.gender,50,250)
        self.combo2=QComboBox(self)
        self.combo2.addItems(["","Female","Male"])
        self.font(self.combo2,50,300)
      
        self.nation=QLabel("Select your nationality",self)
        self.font(self.nation,50,350)
        self.combo3=QComboBox(self)
        self.combo3.addItems(["","Uzbek","Karakalpak","Kazak","Russian"])
        self.font(self.combo3,50,400)

        ok=QPushButton("Ok",self)
        ok.setFont(QFont("Times",20))
        ok.move(330,500)
        ok.clicked.connect(self.run)

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",12))
        obj.move(x,y)
        obj.adjustSize()

    def run(self):
        win=QMessageBox(self)
        win.setWindowTitle("Information")
        if self.combo1.currentText()=="":
            win.setText("You did not select region\n")
        else:
            win.setText("Region: "+self.combo1.currentText()+"\n")
        if self.comboc.currentText()=="":
            win.setText(win.text()+"You did not select district\n")
        else:
            win.setText(win.text()+"District: "+self.comboc.currentText()+"\n")
        if self.combo2.currentText()=="":
            win.setText(win.text()+"You did not select gender\n")
        else:
            win.setText(win.text()+"Gender: "+self.combo2.currentText()+"\n")
        if self.combo3.currentText()=="":
            win.setText(win.text()+"You did not select nationality\n")
        else:
            win.setText(win.text()+"Nationality: "+self.combo3.currentText()+"\n")
        win.show()
window=Window()
window.show()
sys.exit(app.exec_())
'''