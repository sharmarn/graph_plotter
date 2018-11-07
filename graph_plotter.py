import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

total_alive = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_alive.csv', asfileobj=False)
total_area = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_area.csv', asfileobj=False)
total_alive_helper = cbook.get_sample_data('C:/Java Projects/quality_assurance/count_total_alive.csv', asfileobj=False)
total_area_helper = cbook.get_sample_data('C:/Java Projects/quality_assurance/count_total_area.csv', asfileobj=False)

option = total_area
cityName = 'Baden-Württemberg'

plt.plotfile(option, ('time_limit','default','radius','in_range','random'),delimiter=';',subplots=False)

plt.xlabel('elimination time')

if option == total_alive:
    plt.yscale('log')
    plt.title(cityName + ' - Total Alive')
    plt.ylabel('number of centers alive')

elif option == total_area:
    plt.yscale('log')
    plt.title(cityName + ' - Total Area')
    plt.ylabel('total covered area by label disks')

elif option == total_alive_helper:
    plt.title(cityName + ' - Frequency for Total Alive')
    plt.ylabel('number of frequency')

else:
    plt.title(cityName + ' - Frequency for Total Area')
    plt.ylabel('number of frequency')

#plt.yticks(np.arange(10^7, 10^9, 1000))
plt.show()
