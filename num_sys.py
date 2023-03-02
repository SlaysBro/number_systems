from tkinter import*

class mv:
    anw = 2
    anw_two = 10

def main():
    a = num1.get().lower()
    result_ten = 0
    other_result = ''
    other_result_inv = ''
    i = 0
    remnant=0
    s = len(a) - 1
    sixteen = 0

    try:
        for i in a:
            if mv.anw == 16:
                if i == 'a':
                    sixteen = 10
                elif i == 'b':
                    sixteen = 11
                elif i == 'c':
                    sixteen = 12
                elif i == 'd':
                    sixteen = 13
                elif i == 'e':
                    sixteen = 14
                elif i == 'f':
                    sixteen = 15
                else:        
                    sixteen = int(i) 
                result_ten+=sixteen*16**s
                s-=1      
            else:
                result_ten+=int(i)*mv.anw**s
                s-=1
            
        while result_ten//mv.anw_two != 0:
            remnant = result_ten % mv.anw_two
            
            result_ten//=mv.anw_two
            
            if mv.anw_two == 16:
                if remnant < 10:   
                    other_result+=str(remnant)
                elif remnant == 10:
                    other_result+='A'
                elif remnant == 11:
                    other_result+='B'
                elif remnant == 12:
                    other_result+='C'
                elif remnant == 13:
                    other_result+='D'
                elif remnant == 14:
                    other_result+='E'
                elif remnant == 15:
                    other_result+='F'
                else:   
                    other_result+=str(remnant)
            else:
                other_result+=str(remnant)
                
        if mv.anw_two == 16:
            if result_ten == 10:
                other_result+='A'
            elif result_ten == 11:
                other_result+='B'
            elif result_ten == 12:
                other_result+='C'
            elif result_ten == 13:
                other_result+='D'
            elif result_ten == 14:
                other_result+='E'
            elif result_ten == 15:
                other_result+='F'
            else:   
                other_result+=str(result_ten)
        else:
            other_result+=str(result_ten)

        i = len(other_result) - 1

        while i >= 0:
            other_result_inv+=other_result[i]
            i-=1

        num2.delete(0, 'end')
        num2.insert(0, other_result_inv)
    except:
        num2.delete(0, 'end')
        num2.insert(0, 'ERROR')

def b1():
    mv.anw = 2
    ot()
    clr()

def b2():
    mv.anw = 8
    ot()
    clr()

def b3():
    mv.anw = 10
    ot()
    clr()

def b4():
    mv.anw = 16
    ot()
    clr()

def b5():
    mv.anw_two = 2
    ot()
    clr()

def b6():
    mv.anw_two = 8
    ot()
    clr()

def b7():
    mv.anw_two = 10
    ot()
    clr()

def b8():
    mv.anw_two = 16
    ot()
    clr()

def ot():
    res.config(text=(f'Из {mv.anw}-чной в {mv.anw_two}-чной сс:'))

def clr():
    num2.delete(0, 'end')

w = Tk()
w.geometry('500x350')
w['bg'] = 'black'
w.title('Кал. сс')
w.resizable(0, 0)

l1 = Label(fg='red', bg='black', font=('Comic Sans MS', 16, 'bold'), text='Из какой системы?')
l1.place(x=55, y=0)

l2 = Label(fg='red', bg='black', font=('Comic Sans MS', 16, 'bold'), text='В какую?')
l2.place(x=105, y=90)

txt = Label(fg='red', bg='black', font=('Comic Sans MS', 16, 'bold'), text='Введите значение:')
txt.place(x=60, y=180)

res = Label(fg='red', bg='black', font=('Comic Sans MS', 16, 'bold'), text=f'Из 2-чной в 10-чной сс:')
res.place(x=20, y=260)

num1 = Entry(fg='red', width=10, font=('Comic Sans MS', 16, 'bold'))
num1.place(x=90, y=220)
num1.insert(0, '101101')

num2 = Entry(fg='red', width=10, font=('Comic Sans MS', 16, 'bold'))
num2.insert(0, '45')
num2.place(x=90, y=300)

b2_1 = Button(bg='grey', text='2', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b1)
b2_1.place(x=55, y=35)

b8_1 = Button(bg='grey', text='8', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b2)
b8_1.place(x=105, y=35)

b10_1 = Button(bg='grey', text='10', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b3)
b10_1.place(x=155, y=35)

b16_1 = Button(bg='grey', text='16', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b4)
b16_1.place(x=205, y=35)

b2_2 = Button(bg='grey', text='2', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b5)
b2_2.place(x=55, y=125)

b8_2 = Button(bg='grey', text='8', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b6)
b8_2.place(x=105, y=125)

b10_2 = Button(bg='grey', text='10', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b7)
b10_2.place(x=155, y=125)

b16_2 = Button(bg='grey', text='16', width=3, height=1, font=('Comic Sans MS', 16, 'bold'), fg='red', relief='flat', command=b8)
b16_2.place(x=205, y=125)

btn = Button(bg='grey', text='Вывод', font=('Comic Sans MS', 28, 'bold'), fg='red', relief='flat', command=main)
btn.place(x=320, y=250)

w.mainloop()