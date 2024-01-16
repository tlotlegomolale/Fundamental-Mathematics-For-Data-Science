import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

# Modal Category for 'manufacturer_country' column
print(car_eval.manufacturer_country.value_counts())

# Modal Category with normalized counts
print(car_eval.manufacturer_country.value_counts(normalize= True))
print(car_eval.buying_cost.unique())

# Define buying cost categories and convert the 'buying_cost' column to an ordered categorical type

buying_cost_categories = ['low', 'med' ,'high' ,'vhigh']
car_eval.buying_cost = pd.Categorical(car_eval.buying_cost,buying_cost_categories, ordered = True )

# Calculate the median index for 'buying_cost' and find the median buying cost category
median_index= np.median(car_eval.buying_cost.cat.codes)
median_buying_cost = buying_cost_categories[int(median_index)]
print(median_buying_cost)

# Display the normalized value counts for the 'luggage' column
print(car_eval.luggage.value_counts(normalize = True).head())

# Display the normalized value counts for 'luggage' column including missing values
print(car_eval.luggage.value_counts(normalize = True, dropna = False).head())

# Display the value counts for 'luggage' column as proportions of the total dataset
print(car_eval.luggage.value_counts()/len(car_eval.luggage))

# Calculate the frequency of "5more" in the 'doors' column
frequency = (car_eval["doors"] == "5more").sum()
print(frequency)

# Calculate the mean of "5more" in the 'doors' column
mean = (car_eval["doors"] == "5more").mean()
print(mean)
