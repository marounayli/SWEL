import matplotlib.pyplot as plt
import numpy as np
import os
import heapq as hq
folder_path = 'plots/'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted {filename}")

data = [] 
dat = []

with open('integers.txt', 'r') as file:
    for line in file:
        if line.startswith("#"):
            data.append(dat)
            dat=[]
        else:
            dat.append(float(line))
    data.append(hq.nlargest(50,dat))
for i in range(len(data)):
    p =  plt.plot(data[i])
    plt.savefig("plots/plots"+str(i)+".png")
    plt.clf()
