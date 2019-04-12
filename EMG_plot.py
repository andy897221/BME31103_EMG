import matplotlib.pyplot as plt
import numpy as np

thirty_temp = open("partd_30max.txt", "r")
thirty = [i[:-1] for i in thirty_temp.readlines()]
thirty_x = np.asarray([float(i.split("\t")[0]) for i in thirty])
thirty_y = np.asarray([float(i.split("\t")[1]) for i in thirty])
thirty_temp.close()

sevenFive_temp = open("partd_75max.txt", "r")
sevenFive = [i[:-1] for i in sevenFive_temp.readlines()]
sevenFive_x = np.asarray([float(i.split("\t")[0]) for i in sevenFive])
sevenFive_y = np.asarray([float(i.split("\t")[1]) for i in sevenFive])
sevenFive_temp.close()

final_y = [[],[]] # [array of 30%, array of 75%]
for i in np.arange(min(thirty_x[0], sevenFive_x[0]),max(thirty_x[-1], sevenFive_x[-1]), thirty_x[1]-thirty_x[0]):
    loc = np.where(thirty_x == i)
    if len(loc) == 0: final_y[0] += [0]
    else: final_y[0] += [thirty_y[loc[0]]]

    loc = np.where(sevenFive_x == i)
    if len(loc) == 0: final_y[1] += [0]
    else: final_y[1] += [sevenFive_y[loc[0]]]
    
    


plt.plot(thirty_x, thirty_y)
plt.plot(sevenFive_x, sevenFive_y)
plt.show()