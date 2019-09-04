import tkinter as tk
import datetime
from time import gmtime, strftime

root = tk.Tk()
root.title ("Weeding calculator!")
logo = tk.PhotoImage(file="para.png")

def convert_second (s):
    hour = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    seconds = s

    if hour == 1:
        hh = "godzina"
    elif hour ==2 or hour ==3 or hour ==4 or hour == 22 or hour == 23:
        hh = "godziny"
    else:
        hh = "godzin"

    return(f'{hour} {hh}, {minutes} minut, {seconds} sekund')


now = datetime.datetime.now()
wedding_day = datetime.datetime(2020,6,20,17,0, 0)

dtime = (wedding_day-now)
hms = convert_second(dtime.seconds)
txdelta =(f'{dtime.days} dni, {hms}')


date_wed = '20 czerwca 2020 godz. 17.00'
abc = '''Do Waszego ślubu pozostało:'''
name = "Agnieszka & Andrzej"

w = tk.Label(
    root,
    compound=tk.CENTER,
    text=name,
).pack()
w = tk.Label(
    root,
    compound=tk.CENTER,
    text=date_wed,
).pack()

w = tk.Label(
    root,
    compound=tk.CENTER,
    text=txdelta,
).pack(side=tk.BOTTOM)
w = tk.Label(
    root,
    compound=tk.CENTER,
    text=abc,
).pack(side=tk.BOTTOM)
w = tk.Label(
    root,
    compound=tk.CENTER,
    image=logo,
    justify=tk.LEFT
).pack(side=tk.TOP)


root.mainloop()
