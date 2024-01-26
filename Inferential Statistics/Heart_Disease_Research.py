# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

#Use the dataset yes_hd to save cholesterol levels for patients with heart disease as a variable named chol_hd
chol_hd= yes_hd['chol']

#Calculate the mean cholesterol value of patients diagnosed with heart disease
print('The average number of patients with heart disease is' + ' ' + str(chol_hd.mean()))

#Conduct a hypothesis test 
sig_thresh = 0.05
tstat, pval = ttest_1samp(chol_hd, 240)
print('The p-value is:'+ ' ' + str(pval/2))

#Repetition of the above code for patients without heart disease
chol_nhd = no_hd['chol']
print('The average number of patients without heart disease is:' + ' ' + str(chol_nhd.mean()))

#Conduct a hypothesis test
tstat, pval = ttest_1samp(chol_nhd, 240)
print('The p-value is:'+ ' ' + str(pval/2))

#Quantifying the number of patients in the dataset
num_patients = len(heart)
print('There are {0} patients in this particular dataset'.format(num_patients))

#Calculate the number of patients with fasting blood sugar
num_highfbs_patients = np.sum(heart.fbs)
print(num_highfbs_patients)

# Calculate eight percent of the sample population
print(0.08 * num_patients)

# Run a binomial test to check if the sample came from a population in which the rate of fbs > 120 mg/dl equals 8%
p_value = binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')

# Output p_value
print(p_value)

# Interpreting the p_value
print('The p-value of 0.0000469, which is less than 0.05, indicating that this sample is most likely drawn from a population in which more than 8% of persons with fbs > 120 mg/dl')
