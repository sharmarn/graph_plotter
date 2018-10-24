import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

total_alive = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_alive.csv', asfileobj=False)
total_area = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_area.csv', asfileobj=False)
total_alive_helper = cbook.get_sample_data('C:/Java Projects/quality_assurance/count_total_alive.csv', asfileobj=False)
total_area_helper = cbook.get_sample_data('C:/Java Projects/quality_assurance/count_total_area.csv', asfileobj=False)

option = total_alive
cityName = 'Hamburg'

plt.plotfile(option, ('time_limit','default','radius','in_range','osm_id','random'),delimiter=';',subplots=False)

#plt.yscale('log')
#plt.yticks(np.arange(10^3, 10^4, 1))

plt.xlabel('elimination time')

if option == total_alive:
    plt.title(cityName + ' - Total alive centers')
    plt.ylabel('number of centers alive')

elif option == total_area:
    plt.title(cityName + ' - Total covered area')
    plt.ylabel('total covered area')

elif option == total_alive_helper:
    plt.title(cityName + ' - MAX Total Alive')
    plt.ylabel('count')

else:
    plt.title(cityName + ' - MAX Total Area')
    plt.ylabel('count')

plt.show()
