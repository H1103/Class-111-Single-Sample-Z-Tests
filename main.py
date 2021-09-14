import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("School1.csv")
data = df["Math_score"].tolist()

#print(data)

fig = ff.create_distplot([data],["Math_score"], show_hist = False)
fig.show()


mean = statistics.mean(data)
print("Mean of the population is ", mean)

std_dev = statistics.stdev(data)
print("Standard deviation of the mean is ", std_dev)

