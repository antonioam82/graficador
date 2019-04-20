import tkinter, os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from math import *

#os.chdir()

root = tkinter.Tk()
root.wm_title("Graficador")
#root.geometry("500x500")
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

def animate(i):
    t = np.arange(0, 5, .01)
    try:
        graph_dataa = open('ejemplo.txt','r') #nuevo sitio
        graph_data=graph_dataa.read()
        #2*np.sin(2*np.pi*t)
        solo=eval(graph_data)
        ax1.clear()
        ax1.plot(solo)
    except:
        ax1.plot()

def represent():
    graph_dataa = open('ejemplo.txt','r')
    graph_dataa.close()
    graph_dataa=open('ejemplo.txt','w')
    texto_orig=str(et.get())
    #chapuzi
    ta=texto_orig.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tc=tb.replace("tan","np.tan")
    graph_dataa.write(tc+"\n")
    #print(et.get())
    graph_dataa.close()

button = tkinter.Button(master=root, text="SET", command=represent)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

et =tkinter.Entry(master=root,width=60)
et.pack(side=tkinter.TOP)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()


