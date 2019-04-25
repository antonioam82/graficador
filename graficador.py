import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

root = tkinter.Tk()
root.wm_title("Graficador")
ta=root.geometry("1000x700")
#root.configure(background="SkyBlue4")

style.use('fivethirtyeight')

#fig = Figure(figsize=(5, 4), dpi=100)
fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
act_rango=False
ran=""
def animate(i):
    global act_rango
    if act_rango==True:
        try:
            x = np.arange(float(ran[0]), float(ran[1]), .01)
        except:
            messagebox.showwarning("Error","Rango no válido")
            #print("Se repite")
            act_rango=False
            ets.delete(0,len(ets.get()))
    else:
        x = np.arange(1, 10, .01)
    try:
        solo=eval(graph_data)
        ax1.clear()
        ax1.plot(x,solo)
    except:
        ax1.plot()

def represent():
    global graph_data
    global ran
    global act_rango
    texto_orig=et.get()
    if ets.get()!="":
        rann=ets.get()
        ran=rann.split(",")
        act_rango=True
    ta=texto_orig.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tl=tb.replace("log","np.log")
    tc=tl.replace("tan","np.tan")
    tr=tc.replace("sqrt","np.sqrt")
    graph_data=tr


button = tkinter.Button(master=root, text="SET", command=represent)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

et =tkinter.Entry(master=root,width=60)
et.pack(side=tkinter.TOP)
button.pack(side=tkinter.BOTTOM)

ets=tkinter.Entry(master=root,width=10)
ets.pack(side=tkinter.RIGHT)


tkinter.mainloop()



