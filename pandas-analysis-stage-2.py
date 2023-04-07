import pandas as pd

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

prenatal_df.columns = general_df.columns
sports_df.columns = general_df.columns

df_concated = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

df_concated.drop(columns=['Unnamed: 0'], inplace=True)

print(df_concated.sample(n=20, random_state=30))

"""
Stage 2/5: Merge them!
Description
Hooray, you have the datasets! However, they are somewhat difficult to work with. They are divided into three parts, and the column names are different: HOSPITAL and Sex in the prenatal, Hospital and Male/female in the sports facility. We cannot study our data in full and perform statistical calculations. It also stands in the way of good visualization.

In this stage, we will change the column names and merge our datasets into one. To combine the columns, use the concat function and the ignore_index=True parameter. After merging, a side Unnamed: 0 column will appear. This column contains the indexes of the tables. This column is not needed for the practical purposes of this project, so we will delete it in this stage.

Objectives
We continue to process DataFrames from the previous stage. The second stage requires completing the following steps:

Change the column names. All column names in the sports and prenatal tables must match the column names in the general table
Merge the DataFrames into one. Use the ignore_index=True parameter and the following order: general, prenatal, sports
Delete the Unnamed: 0 column
Print random 20 rows of the resulting DataFrame. For the reproducible output set random_state=30
Keep pd.set_option('display.max_columns', 8) in your code.

Tip: To complete the last step use pandas.DataFrame.sample(n=20, random_state=30).

If you have corrupted CSV files, please download them and unzip in your working directory.

Example
The input is 3 CSV files, test/general.csv, test/prenatal.csv, and test/sports.csv.

The output is the following:
(This data is given for reference only, the actual values might be different)

      hospital  gender   age  height  ...    mri  xray  children  months
148        NaN     man   NaN   163.0  ...   96.0   NaN       3.0     NaN
408  Cambridge  female   NaN   196.0  ...  189.0    no       NaN     2.0
214     Oxford     boy  51.0     NaN  ...   65.0   NaN       3.0     1.0
67      Oxford     NaN   NaN     NaN  ...   97.0    no       3.0     1.0
241  Cambridge     boy   NaN   199.0  ...  177.0   NaN       NaN     NaN
205        NaN     NaN  25.0   187.0  ...    NaN   NaN       0.0     2.0
126  Cambridge    girl  50.0     NaN  ...   99.0   yes       NaN     1.0
193   Brighton     man  26.0   195.0  ...  116.0    no       NaN     1.0
338  Cambridge     man  17.0   176.0  ...  214.0   NaN       NaN     1.0
317        NaN     man   NaN   153.0  ...  190.0   NaN       3.0     1.0
344   Brighton     boy   NaN     NaN  ...  200.0   yes       2.0     1.0
31         NaN     boy  65.0   156.0  ...   59.0    no       2.0     NaN
164        NaN     man  53.0   150.0  ...    NaN   yes       1.0     2.0
212   Brighton    girl  18.0     NaN  ...    NaN    no       0.0     NaN
213  Cambridge     NaN  55.0   172.0  ...    NaN   yes       2.0     2.0
201     Oxford    girl   NaN   183.0  ...    NaN   yes       3.0     1.0
342   Brighton    girl   NaN   189.0  ...  178.0   NaN       NaN     NaN
236        NaN     NaN   NaN   164.0  ...   67.0   yes       3.0     NaN
211        NaN     NaN  40.0   165.0  ...   70.0    no       NaN     1.0
384        NaN  female  29.0     NaN  ...   69.0   NaN       NaN     1.0

[20 rows x 14 columns]
"""