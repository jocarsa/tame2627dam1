import matplotlib.pyplot as plt

# Set manual colors for the pie chart
colors = ['#B0C4DE', '#4169E1', '#ADD8E6']

plt.pie([45, 76, 23], labels=["A", "B", "C"], colors=colors)
plt.title("Mi primer gráfico de tarta")

plt.show()