import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# Taking a look at the dataset
print(london_data.head())
# Looking through rows 100 to 199
print(london_data.iloc[100:200])

# Taking a look at the number of data points we have
print(len(london_data))

#Performing Descriptive Analytics on Temperature
temp = london_data['TemperatureC']
average_temp = np.mean(temp)
temperature_var = np.var(temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

# Analysing for columns that will help us group by months
print(london_data.head())
print(london_data.tail())

# Selecting temperature rows from the month of June '6'
june = london_data.loc[london_data['month']==6]['TemperatureC']

# Selecting temperature rows from the month of July '7'
july = london_data.loc[london_data['month']==7]['TemperatureC']

# Calculating the mean temperature in London for both June and July
june_mean = np.mean(june)
july_mean = np.mean(july)

# Calculating standard deviation for both june and july based on temperature
june_std = np.std(june)
print('Standard Deviation for June is ', june_std)

july_std = np.std(july)
print('Standard Deviation for June is ', july_std)

# Calculating descriptive statistics for every month
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")



