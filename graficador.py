import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
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
    if act_rango==True:
        #ran=[0,12]
        x = np.arange(int(ran[0]), int(ran[1]), .01)
    else:
        x = np.arange(0, 10, .01)
    try:
        solo=eval(graph_data)
        ax1.clear()
        ax1.plot(x,solo)
    except:
        ax1.plot()

def represent():
    global graph_data
    texto_orig=et.get()
    ta=texto_orig.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tl=tb.replace("log","np.log")
    tc=tl.replace("tan","np.tan")
    graph_data=tc

def rango():
    global ran
    global act_rango
    rann=ets.get()
    ran=rann.split(",")
    act_rango=True

button = tkinter.Button(master=root, text="SET", command=represent)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

et =tkinter.Entry(master=root,width=60)
et.pack(side=tkinter.TOP)
button.pack(side=tkinter.BOTTOM)
#textvariable=input_text

ets=tkinter.Entry(master=root,width=10)#.place(x=20,y=20)
#ets.pack()
Buttonn=tkinter.Button(master=root, text="ESTAB",command=rango).place(x=20,y=40)
ets.pack(side=tkinter.RIGHT)
#ets.pack(root)

tkinter.mainloop()


