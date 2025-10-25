from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
DISPLAY_NUMBER = "999990"
def number_print(number):
    global DISPLAY_NUMBER
    print(number)
    DISPLAY_NUMBER += number
    print(DISPLAY_NUMBER)
ttk.Label(frm, text=f"{DISPLAY_NUMBER}").grid(row=0)
ttk.Button(frm, text="1", command=lambda: number_print("1")).grid(column=0, row=1)
ttk.Button(frm, text="2", command=lambda: number_print("2")).grid(column=1, row=1)
ttk.Button(frm, text="3", command=lambda: number_print("3")).grid(column=2, row=1)
ttk.Button(frm, text="4", command=lambda: number_print("4")).grid(column=0, row=2)
ttk.Button(frm, text="5", command=lambda: number_print("5")).grid(column=1, row=2)
ttk.Button(frm, text="6", command=lambda: number_print("6")).grid(column=2, row=2)
ttk.Button(frm, text="7", command=lambda: number_print("7")).grid(column=0, row=3)
ttk.Button(frm, text="8", command=lambda: number_print("8")).grid(column=1, row=3)
ttk.Button(frm, text="9", command=lambda: number_print("9")).grid(column=2, row=3)

root.mainloop()