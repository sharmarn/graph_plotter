import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Enter the path to the files
total_alive = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_alive.csv', asfileobj=False)
total_area = cbook.get_sample_data('C:/Java Projects/quality_assurance/total_area.csv', asfileobj=False)

# Set one option, that are given above
option = total_alive

# Set the name of the region for the headline of the graph
cityName = 'Hamburg'

# Set the exact heuristic names from the .csv file
plt.plotfile(option, ('time_limit','default','radius','in_range','random', 'lp_solution'),delimiter=';',subplots=False)

# Set log-scales for y-axis to get a clear graph
plt.yscale('log')

plt.xlabel('elimination time')

if option == total_alive:
    plt.title(cityName + ' - Total Alive')
    plt.ylabel('number of centers alive')

else:
    plt.title(cityName + ' - Total Area')
    plt.ylabel('total area covered by label disks')

plt.show()
