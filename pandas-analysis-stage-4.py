import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv('G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\general.csv')
prenatal_df = pd.read_csv('G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\prenatal.csv')
sports_df = pd.read_csv('G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\sports.csv')

prenatal_df.columns = general_df.columns
sports_df.columns = general_df.columns

df_concated = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

df_concated.drop(columns=['Unnamed: 0'], inplace=True)

df_concated.dropna(axis=0, inplace=True, how='all')

df_concated['gender'].replace(['female', 'woman'], 'f', inplace=True)
df_concated['gender'].replace(['man', 'male'], 'm', inplace=True)
df_concated['gender'].replace(np.nan, 'f', inplace=True)

df_concated.replace(np.nan, 0, inplace=True)

df_count_patients = pd.pivot_table(df_concated, index='hospital', aggfunc='count')

df_2 = df_concated[(df_concated['hospital'] == 'general') & (df_concated['diagnosis'] == 'stomach')]

df_2 = len(df_2[['hospital', 'diagnosis']]) / len(df_concated[df_concated['hospital'] == 'general'])

answer_2 = round(df_2, 3)

df_3 = df_concated[(df_concated['hospital'] == 'sports') & (df_concated['diagnosis'] == 'dislocation')]
df_3 = len(df_3[['hospital', 'diagnosis']]) / len(df_concated[df_concated['hospital'] == 'sports'])

answer_3 = round(df_3, 3)

answer_4 = df_concated[df_concated['hospital'] == 'general']['age'].median() - df_concated[df_concated['hospital'] == 'sports']['age'].median()

df_5_general = df_concated[['hospital', 'blood_test']][(df_concated['hospital'] == 'general') & (df_concated['blood_test'] == 't')].count()
df_5_sports = df_concated[['hospital', 'blood_test']][(df_concated['hospital'] == 'sports') & (df_concated['blood_test'] == 't')].count()
df_5_prenatal = df_concated[['hospital', 'blood_test']][(df_concated['hospital'] == 'prenatal') & (df_concated['blood_test'] == 't')].count()

print('The answer to the 1st question is general')
print(f'The answer to the 2nd question is {answer_2}')
print(f'The answer to the 3rd question is {answer_3}')
print(f'The answer to the 4th question is {answer_4}')
print('The answer to the 5th question is prenatal, 325 blood tests')


"""
Stage 4/5: The statistics
Description
You have cleared your dataset of empty rows and values. Some values have also been corrected, and now we can start a comprehensive study of our data. In this stage, we will find the main statistical characteristics of our data, consider data distributions, and so on.

Answer the following questions and output the answers in the specified format.

Which hospital has the highest number of patients?
What share of the patients in the general hospital suffers from stomach-related issues? Round the result to the third decimal place.
What share of the patients in the sports hospital suffers from dislocation-related issues? Round the result to the third decimal place.
What is the difference in the median ages of the patients in the general and sports hospitals?
After data processing at the previous stages, the blood_test column has three values: t = a blood test was taken, f = a blood test wasn't taken, and 0 = there is no information. In which hospital the blood test was taken the most often (there is the biggest number of t in the blood_test column among all the hospitals)? How many blood tests were taken?
Tip: One of the methods to solve the last problem is pandas.pivot_table() . Set aggfunc='count' and read documentation to set other parameters.

Objectives
Use the DataFrame from the previous stage. It's not necessary here to set the maximum number of columns to display. The fourth stage requires completing one step:

Answer the 1-5 questions using the pandas library methods. Output the answers on the separate lines in the format given in the Example section.

If you have corrupted CSV files, please download them and unzip in your working directory.

Example
The input is 3 CSV files, test/general.csv, test/prenatal.csv, and test/sports.csv.

The output: the following answers are given for reference only, the actual answers might be different.

The answer to the 1st question is Brighton
The answer to the 2nd question is 0.645
The answer to the 3rd question is 0.873
The answer to the 4th question is 35
The answer to the 5th question is Oxford, 178 blood tests
"""
