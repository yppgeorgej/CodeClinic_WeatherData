from csv import DictReader
from datetime import datetime
from tkinter import ttk, messagebox
from tkinter import *

import matplotlib
import numpy as np
from matplotlib.dates import date2num, num2date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTk, NavigationToolbar2Tk)


class WeatherStats:

    def __init__self(self,master):
        barometriclist = []
        datetimelist = []

        ##### WEATHER DATA POPULATION ##
        basefilepath = "Environmental_Data_Deep_Moor_"
        for year in range(2012, 2016):
            fname = basefilepath + str(year) + ".txt"
            import re

            datetime_re = re.compile(r'[\d]{2,4}')

            for row in DictReader(open(fname, 'r'), delimiter='\t'):
                barometriclist.append(float(row['Wind_Dir']))
                datetimelist.append(
                    date2num(datetime(*list(map(int, datetime_re.findall(row['date       time    ']))))))

            # ARRAY CONVERSION
            datetime_array = np.array(datetimelist)
            barometriclist = np.array(barometriclist)

            master.tittle('Weather Statistics')
            master.resizable(True, True)
            master.state('Zoomed')

            matplotlib.rc('font', size=18)
            f = Figure()
            f.set_facecolor(0,0,0,0)
            self.a = f.add_subplot(111)
            self.canvas.draw()
            toolbar_frame = ttk.Frame(master)
            toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
            toolbar.update()
            toolbar.pack(side=TOP, fill=X, expand=0)
            self.canvas._tkcanvase.pack(fill=BOTH, expand=1)

            control_frame = ttk.Frame(Master)
            controls_frame.pack()
check = WeatherStats(asd)
