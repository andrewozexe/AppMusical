from ast import main
import tkinter as tk
from tkinter import ttk
from back import Escala, CampoHarmonico
from commands import *

root = tk.Tk()

root.title('Me de o Tom')
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Escalas')
tabControl.add(tab2, text='Campo Harmonico')
tabControl.pack(expand=1,fill='both')
ttk.Label(tab1)
ttk.Label(tab2)

bt1 = tk.Button(tab1, text='Escala')
bt1.pack(side=tk.LEFT)

root.mainloop()