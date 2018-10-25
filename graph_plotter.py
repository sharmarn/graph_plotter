import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

total_alive = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_alive.csv', asfileobj=False)
total_area = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_area.csv', asfileobj=False)
total_alive_helper = cbook.get_sample_data('C:/Java Projects/quality_assurance/count_total_alive.csv', asfileobj=False)
total_area_helper = cbook.get_sample_data('C:/Java Projects/quality_assurance/count_total_area.csv', asfileobj=False)

option = total_alive_helper
cityName = 'Berlin'

plt.plotfile(option, ('time_limit','default','radius','in_range','osm_id','random'),delimiter=';',subplots=False)

#plt.yticks(np.arange(0, 10^8, 1000))

plt.xlabel('elimination time')

if option == total_alive:
    plt.yscale('log')
    plt.title('Total alive centers for ' + cityName)
    plt.ylabel('number of centers alive')

elif option == total_area:
    plt.yscale('log')
    plt.title('Total covered area for ' + cityName)
    plt.ylabel('total covered area')

elif option == total_alive_helper:
    plt.title(cityName + ' - Frequency for Total Alive')
    plt.ylabel('number of frequency')

else:
    plt.title(cityName + ' - Frequency for Total Area')
    plt.ylabel('number of frequency')

plt.show()
