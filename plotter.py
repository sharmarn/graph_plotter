import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

total_alive = cbook.get_sample_data('C:/Java Projects/quality_assurance/evaluate_total_alive.csv', asfileobj=False)
total_area = cbook.get_sample_data('C:/Java Projects/quality_assurance/evaluate_total_area.csv', asfileobj=False)

option = total_area

plt.plotfile(option, ('time_limit','default','radius','in_range','osm_id','random'),delimiter=';',subplots=False)

plt.xlabel('time t')

if option == total_alive:
    plt.title('Bayern - Total alive')
    plt.ylabel('number of centers alive')

else:
    plt.title('Bayern - Total area')
    plt.ylabel('total area')

plt.show()
