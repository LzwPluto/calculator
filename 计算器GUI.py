import tkinter as tk
import os

root = tk.Tk()
root.title("计算器GUI")
root.geometry("340x410")
root.resizable(False, False)
num = 0
temp = 0
result = 0
sign = ''
text_var = tk.StringVar()
text_var.set(str(temp))
entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
entry.place(x=5,y=0,width=330,height=80)

def signclear():
    global num
    global temp
    global sign
    if sign == '+':
        num += temp
    elif sign == '-':
        num -= temp
    elif sign == '*':
        num *= temp
    elif sign == '/':
        num /= temp
    elif sign == '' and num == 0:
        num = temp
    temp = 0

def result_show():
    global result
    global num
    global sign
    text_var = tk.StringVar()
    text_var.set(str(num))
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    sign = ''
    print(temp)
    print(num)
    print(sign)
    print('-'*10)
def button_click_1():
    global temp
    global sign
    temp *= 10
    temp += 1
    text_var = tk.StringVar()
    text_var.set(str(temp))
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)
def button_click_2():
    global temp
    global sign
    temp *= 10
    temp += 2
    text_var = tk.StringVar()
    text_var.set(str(temp))
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_3():
    global temp
    global sign
    temp *= 10
    temp += 3
    text_var = tk.StringVar()
    text_var.set(str(temp))
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_4():
    global temp
    global sign
    temp *= 10
    temp += 4
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_5():
    global temp
    global sign
    temp *= 10
    temp += 5
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_6():
    global temp
    global sign
    temp *= 10
    temp += 6
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_7():
    global temp
    global sign
    temp *= 10
    temp += 7
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_8():
    global temp
    global sign
    temp *= 10
    temp += 8
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_9():
    global temp
    global sign
    temp *= 10
    temp += 9
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_0():
    global temp
    global sign
    temp *= 10
    temp += 0
    text_var = tk.StringVar()
    text_var.set(str(temp))    
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    print(temp)
    print(num)
    print(sign)
    print('-'*10)    
def button_click_add():
    global sign
    signclear()
    sign = '+'
def button_click_sub():
    global sign
    signclear()
    sign = '-'
def button_click_mul():
    global sign
    signclear()
    sign = '*'
def button_click_div():
    global sign
    signclear()
    sign = '/'
def button_click_equal():
    signclear()
    result_show()
def button_click_clear():
    global result
    global num
    global sign
    global temp
    result = 0
    num = 0
    temp = 0 
    sign = ''
    text_var = tk.StringVar()
    text_var.set(str(num))
    entry = tk.Entry(root,state = 'disabled',textvariable=text_var,justify='right')
    entry.place(x=5,y=0,width=330,height=80)
    os.system("cls")
button = tk.Button(root,text='1',command=button_click_1)
button.place(x=15,y=250,width=70,height=70)
button = tk.Button(root,text='2',command=button_click_2)
button.place(x=95,y=250,width=70,height=70)
button = tk.Button(root,text='3',command=button_click_3)
button.place(x=175,y=250,width=70,height=70)
button = tk.Button(root,text='4',command=button_click_4)
button.place(x=15,y=170,width=70,height=70)
button = tk.Button(root,text='5',command=button_click_5)
button.place(x=95,y=170,width=70,height=70)
button = tk.Button(root,text='6',command=button_click_6)
button.place(x=175,y=170,width=70,height=70)
button = tk.Button(root,text='7',command=button_click_7)
button.place(x=15,y=90,width=70,height=70)
button = tk.Button(root,text='8',command=button_click_8)
button.place(x=95,y=90,width=70,height=70)
button = tk.Button(root,text='9',command=button_click_9)
button.place(x=175,y=90,width=70,height=70)
button = tk.Button(root,text='0',command=button_click_0)
button.place(x=95,y=330,width=70,height=70)
button = tk.Button(root,text='+',command=button_click_add)
button.place(x=255,y=250,width=70,height=70)
button = tk.Button(root,text='-',command=button_click_sub)
button.place(x=255,y=170,width=70,height=70)
button = tk.Button(root,text='*',command=button_click_mul)
button.place(x=255,y=90,width=70,height=70)
button = tk.Button(root,text='/',command=button_click_div)
button.place(x=255,y=330,width=70,height=70)
button = tk.Button(root,text='=',command=button_click_equal)
button.place(x=175,y=330,width=70,height=70)
button = tk.Button(root,text='C',command=button_click_clear)
button.place(x=15,y=330,width=70,height=70)
root.mainloop()