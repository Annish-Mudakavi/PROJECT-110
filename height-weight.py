import csv
import statistics
import pandas as pd
import plotly.express as px

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

#Calculating the Mean for height and weight using statistics
height_mean = statistics.mean(height_list) 
weight_mean = statistics.mean(weight_list) 

#Calculating the Median for height and weight using statistics
height_median = statistics.median(height_list) 
weight_median = statistics.median(weight_list)

#Calculating the Mode for height and weight using statistics
height_mode = statistics.mode(height_list) 
weight_mode = statistics.mode(weight_list)

#Printing the variable mean, median, mode
print("mean, meidan, mode of height is {}, {} & {} respectively".format(height_mean, height_median, height_mode))
print("mean, meidan, mode of weight is {}, {} & {} respectively".format(weight_mean, weight_median, weight_mode))

#Standard deviation for height and weight
height_std = statistics.stdev(height_list)
weight_std = statistics.stdev(weight_list)

#PRINTING THE STANDARD DEVIATION
print("Standard deviation of height and weight are {}, {} respectively".format( height_std, weight_std))

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
#HEIGHT
height_first_std_deviation_start, height_first_std_deviation_end = height_mean - height_std, height_mean + height_std
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std), height_mean+(2*height_std)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std), height_mean+(3*height_std)

