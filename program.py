import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("height_weight.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["HIGHT DISTRIBUTION GRAPH"], show_hist= False)
fig.show()
fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["THE WEIGHT DISTRIBUTION GRAPH"], show_hist = False)
fig2.show()
