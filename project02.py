from tkinter import *
from tkcalendar import *

root = Tk()
root.geometry('600x400')
root.title("Jaskirat's Calendar")

cal=Calendar(root, selectmode="day",year=2020, month=5, day=22)
cal.pack(pady=20,expand=True,fill="both")

def grab_Date():
    my_label.config(text="Today's Date is " + cal.get_date())

btn = Button(root, text = 'Get Date', command = grab_Date)
btn.pack(side = 'top') 

my_label= Label(root, text="")
my_label.pack(pady=20)

 
root.mainloop()