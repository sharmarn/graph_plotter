import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

fname = cbook.get_sample_data('C:/Python Projects/graph_plotter/test_plot.csv', asfileobj=False)

plt.plotfile(fname, ('x','hello','world','tree'),delimiter=';',subplots=False)

plt.show()
