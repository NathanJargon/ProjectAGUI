from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
import sys
import os
import subprocess
import warnings
warnings.filterwarnings("ignore")

w=Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

# 3. After No.2
def new_win():
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', 'login.py')
    subprocess.run(['python', app_path])

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text=' WATER BILL', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

# 2. Animation Window

#image_a=ImageTk.PhotoImage(Image.open('img/c2.png'))
#image_b=ImageTk.PhotoImage(Image.open('img/c1.png'))
image_a=ImageTk.PhotoImage(Image.open('_internal/img/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('_internal/img/c1.png'))


for i in range(3): # 3 Loops at 0.3 delay
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

w.destroy()
new_win()