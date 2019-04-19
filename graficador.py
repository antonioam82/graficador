import tkinter, os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from math import pi

os.chdir(r'C:\Users\Antonio\Documents\docs')

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
    t = np.arange(0, 3, .01)
    graph_dataa = open('ejemplo.txt','r') #nuevo sitio
    graph_data=graph_dataa.read()
    #2*np.sin(2*np.pi*t)
    solo=eval(graph_data)
    ax1.clear()
    ax1.plot(t,solo)

    #lines = graph_data.split('\n')
    #xs = []
    #ys = []
    #for line in lines:
        #if len(line) > 1:
            #x, y = line.split(',')
            #xs.append(x)
            #ys.append(y)
    #print("22")
       
    #ax1.clear()
    #ax1.plot(xs, ys)

def represent():
    graph_dataa = open('ejemplo.txt','r')
    graph_dataa.close()
    graph_dataa=open('ejemplo.txt','w')
    texto_orig=str(et.get())
    graph_dataa.write(texto_orig+"\n")
    #print(et.get())
    graph_dataa.close()

button = tkinter.Button(master=root, text="SET", command=represent)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

et =tkinter.Entry(master=root,width=60)
et.pack(side=tkinter.TOP)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()

