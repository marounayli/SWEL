import matplotlib.pyplot as plt

# Read the file and plot the values
with open('integers.txt', 'r') as file:
    int_list = [float(line.strip()) for line in file]

plt.plot(int_list)
plt.show()
