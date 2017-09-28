import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
import matplotlib.figure as mplfig
import matplotlib.backends.backend_tkagg as tkagg
pi = np.pi
from LightSensor import *

class App(object):
    def __init__(self, master):
        self.master = master
        self.thisPlayer = Bunch(
            rebounds=20.0,
            freeThrows=5.0,
            steal=5.0,
            underRim=10,
            distance=10)
        self.fig = mplfig.Figure(figsize=(15.5, 15.5))
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=False)
        self.canvas = tkagg.FigureCanvasTkAgg(self.fig, master=master)
        #self.ax.grid(False)
	self.values = []

	self.light_sensor = LightSensor()
	"""
        N = 5
        theta = np.arange(0.0, 2 * pi, 2 * pi / N)
        radii = [self.thisPlayer.rebounds, self.thisPlayer.freeThrows,
                 self.thisPlayer.steal, self.thisPlayer.underRim,
                 self.thisPlayer.distance]
        width = [2 * pi / (N)] * 5
        bars = (
            # self.ax.bar(0, 20, width=2 * pi, linewidth=0) +
            self.ax.bar(theta, radii, width=width, bottom=0.2))
        cmap = plt.get_cmap('jet')
        for r, bar in zip(radii, bars):
            bar.set_facecolor(cmap(r / 20.))
            bar.set_alpha(0.5)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.canvas.get_tk_widget().pack()
	"""
	self.canvas.get_tk_widget().pack()
        self.canvas.draw()
	self.update_value()

    def update_value(self):
	ls_value = "%.2f" %  self.light_sensor.get_value()
	self.values.append(ls_value)
	self.ax.cla()
	self.ax.plot(self.values, '--', linewidth=2)
	self.canvas.draw()
	print ls_value
        self.master.after(1000, self.update_value)


class Bunch(object):
    """
    http://code.activestate.com/recipes/52308
    foo=Bunch(a=1,b=2)
    """
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


def main():
    root = tk.Tk()
    app = App(root)
    tk.mainloop()

if __name__ == '__main__':
    main()