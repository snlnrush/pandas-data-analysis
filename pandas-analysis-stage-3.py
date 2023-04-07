import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 8)

# general_df = pd.read_csv('test/general.csv')
general_df = pd.read_csv(r'G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\general.csv')
# prenatal_df = pd.read_csv('test/prenatal.csv')
prenatal_df = pd.read_csv(r'G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\prenatal.csv')
# sports_df = pd.read_csv('test/sports.csv')
sports_df = pd.read_csv(r'G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\sports.csv')

prenatal_df.columns = general_df.columns
sports_df.columns = general_df.columns

df_concated = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

df_concated.drop(columns=['Unnamed: 0'], inplace=True)

df_concated.dropna(axis=0, inplace=True, how='all')

df_concated['gender'].replace(['female', 'woman'], 'f', inplace=True)
df_concated['gender'].replace(['man', 'male'], 'm', inplace=True)
df_concated['gender'].replace(np.nan, 'f', inplace=True)

df_concated.replace(np.nan, 0, inplace=True)

print('Data shape:', df_concated.shape)
print(df_concated.sample(n=20, random_state=30))

"""
Stage 3/5: Improve your dataset
Description
Some cells in our table have NaN as values: the patient gender is not defined in the prenatal hospital, and columns with the results of medical tests have empty values in all three tables. We still cannot commit to the analysis as the statistics are not going to be objective. We have to correct the table for further study.

Let's take a closer look at the gender column. It's a big mess: there we have female, male, man, woman. You need to correct the data in this column. The values should be either f or m. Replace the empty gender column values for prenatal patients with f (we can assume that the prenatal treats only women).

The bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns also need to be corrected. Replace the NaN values of the columns above with zeros.

Objectives
We continue to process the DataFrame from the previous stage. The third stage requires completing the following steps:

Delete all the empty rows
Correct all the gender column values to f and m respectively
Replace the NaN values in the gender column of the prenatal hospital with f
Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros
Print shape of the resulting DataFrame like in example
Print random 20 rows of the resulting DataFrame. For the reproducible output set random_state=30
Keep pd.set_option('display.max_columns', 8) in your code.

Tip: To complete the last step use pandas.DataFrame.sample(n=20, random_state=30).

If you have corrupted CSV files, please download them and unzip in your working directory.

Example
The input is 3 CSV files, test/general.csv, test/prenatal.csv, and test/sports.csv.

The output is the following:
(This data is given for reference only, the actual values might be different)

Data shape: (442, 14)
      hospital gender   age  height  ...    mri  xray  children  months
148        NaN      m   NaN   163.0  ...   96.0     0       3.0     0.0
408  Cambridge      f   NaN   196.0  ...  189.0    no       0.0     2.0
214     Oxford      m  51.0     NaN  ...   65.0     0       3.0     1.0
67      Oxford      f   NaN     NaN  ...   97.0    no       3.0     1.0
241  Cambridge      m   NaN   199.0  ...  177.0     0       0.0     0.0
205        NaN      f  25.0   187.0  ...    0.0     0       0.0     2.0
126  Cambridge      f  50.0     NaN  ...   99.0   yes       0.0     1.0
193   Brighton      m  26.0   195.0  ...  116.0    no       0.0     1.0
338  Cambridge      m  17.0   176.0  ...  214.0     0       0.0     1.0
317        NaN      m   NaN   153.0  ...  190.0     0       3.0     1.0
344   Brighton      m   NaN     NaN  ...  200.0   yes       2.0     1.0
31         NaN      m  65.0   156.0  ...   59.0    no       2.0     0.0
164        NaN      m  53.0   150.0  ...    0.0   yes       1.0     2.0
212   Brighton      f  18.0     NaN  ...    0.0    no       0.0     0.0
213  Cambridge      f  55.0   172.0  ...    0.0   yes       2.0     2.0
201     Oxford      f   NaN   183.0  ...    0.0   yes       3.0     1.0
342   Brighton      f   NaN   189.0  ...  178.0     0       0.0     0.0
236        NaN      f   NaN   164.0  ...   67.0   yes       3.0     0.0
211        NaN      f  40.0   165.0  ...   70.0    no       0.0     1.0
384        NaN      f  29.0     NaN  ...   69.0     0       0.0     1.0

[20 rows x 14 columns]
"""