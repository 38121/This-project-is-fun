import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

tik = tk.Tk()

#dimensions and things
tik.geometry('500x450')
tik.title('calculator')

# row and column gird
tik.columnconfigure((1,3,5,7,9), weight=1)
tik.columnconfigure((2,4,6,8), weight=4)
tik.rowconfigure((1,3,5,7,9,11,13), weight=1)
tik.rowconfigure((2,4,6,8,10,12), weight=4)

#now making a dictionary so i dont have to make bunch of def functions

def ok_lets_see():
        try:
                when = eval(lbl.get())
                white = f'{when}'
                fin = (lbl.delete(0, tk.END))
                thent = (lbl.insert('end', white))
        except:
                messagebox.showerror('error','there is a value error')
                
        pass

#buttonsi
btn0 = ttk.Button(tik, text=('0'), command=lambda: (lbl.insert('end', '0')))
btn1 = ttk.Button(tik, text=('1'), command=lambda: (lbl.insert('end', '1')))
btn2 = ttk.Button(tik, text=('2'), command=lambda: (lbl.insert('end', '2')))
btn3 = ttk.Button(tik, text=('3'), command=lambda: (lbl.insert('end', '3')))
btn4 = ttk.Button(tik, text=('4'), command=lambda: (lbl.insert('end', '4')))
btn5 = ttk.Button(tik, text=('5'), command=lambda: (lbl.insert('end', '5')))
btn6 = ttk.Button(tik, text=('6'), command=lambda: (lbl.insert('end', '6')))
btn7 = ttk.Button(tik, text=('7'), command=lambda: (lbl.insert('end', '7')))
btn8 = ttk.Button(tik, text=('8'), command=lambda: (lbl.insert('end', '8')))
btn9 = ttk.Button(tik, text=('9'), command=lambda: (lbl.insert('end', '9')))
btn10 = ttk.Button(tik, text=('.'), command=lambda: (lbl.insert('end', '.')))
btn11 = ttk.Button(tik, text=('='), command=ok_lets_see)
btn12 = ttk.Button(tik, text=('+'), command=lambda: (lbl.insert('end', '+')))
btn13 = ttk.Button(tik, text=('-'), command=lambda: (lbl.insert('end', '-')))
btn14 = ttk.Button(tik, text=('*'), command=lambda: (lbl.insert('end', '*')))
btn15 = ttk.Button(tik, text=('/'), command=lambda: (lbl.insert('end', '/')))
btn16 = ttk.Button(tik, text='clear', command=lambda: lbl.delete(0, tk.END))

#labels
lbl = ttk.Entry(tik,font=('dejavu sans', 20), justify='right')

#packages that are packed and are in shipping process
btn0.grid(row=10, column=2,sticky='news')
btn1.grid(row=4, column=2, sticky='news')
btn2.grid(row=4, column=4, sticky='news')
btn3.grid(row=4, column=6, sticky='news')
btn4.grid(row=6, column=2, sticky='news')
btn5.grid(row=6, column=4, sticky='news')
btn6.grid(row=6, column=6, sticky='news')
btn7.grid(row=8, column=2, sticky='news')
btn8.grid(row=8, column=4, sticky='news')
btn9.grid(row=8, column=6, sticky='news')
btn10.grid(row=10, column=4, sticky='news')
btn11.grid(row=10, column=6, sticky='news')
btn12.grid(row=10, column=8, sticky='news')
btn13.grid(row=8, column=8, sticky='news')
btn14.grid(row=6, column=8, sticky='news')
btn15.grid(row=4, column=8, sticky='news')
btn16.grid(row=12, column=2, columnspan=7, sticky='news')

lbl.grid(row=2, column=2, columnspan=7, sticky='news')


tik.mainloop()