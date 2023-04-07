import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv('G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\general.csv')
prenatal_df = pd.read_csv('G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\prenatal.csv')
sports_df = pd.read_csv('G:\\Python-learning\\PyCharm-community\\PycharmProjects\\ahos\\sports.csv')

df_set = (general_df, prenatal_df, sports_df)

colors = ['orange', 'green', 'blue']
bins = [_ for _ in range(0, 85, 5)]
names = ['General', 'Prenatal', 'Sports']

plt.hist([general_df['age'], prenatal_df['age'], sports_df['age']], label=names, bins=bins, color=colors, edgecolor="white")
plt.title("What is the most common age of a patient among all hospitals?")
plt.ylabel("Number of people")
plt.xlabel("Age")
plt.legend()
plt.show()

# data = [general_df['diagnosis'], prenatal_df['diagnosis'], sports_df['diagnosis']]
data = pd.concat([general_df['diagnosis'], prenatal_df['diagnosis'], sports_df['diagnosis']], ignore_index=True)

print(data.head())
#print(general_df['diagnosis'].value_counts())
#print(prenatal_df['diagnosis'].value_counts())
#print(sports_df['diagnosis'].value_counts())


# plt.pie(general_df['diagnosis'].value_counts(), labels=general_df['diagnosis'].unique(), autopct='%.1f%%')
plt.pie(data.value_counts(), labels=general_df['diagnosis'].unique(), autopct='%.1f%%')
plt.title("What is the most common diagnosis among patients in all hospitals?")

plt.show()

# data = [general_df['height'], prenatal_df['height'], sports_df['height']]
data = pd.concat([general_df, prenatal_df, sports_df])
data['height'] = data['height'] * 100

print(data['height'].head())

# fig, axes = plt.subplots()
plt.violinplot(dataset=data['height'])
plt.title("Build a violin plot of height distribution by hospitals")

plt.show()

print("""
The answer to the 1st question: 15-35
The answer to the 2nd question: pregnancy
The answer to the 3rd question: 160-180
""")

"""
Stage 5/5: Visualize it!
Description
Are you ready to catch sight of your data?

Graphics are arguably the most accessible way to represent the data and its structure. Sometimes, it can help to find the main data patterns and deviations. We will use data visualization methods to conclude our dataset.

In the last stage, you need to create data visualization to answer the following questions:

What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
What is the most common diagnosis among patients in all hospitals? Create a pie chart.
Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is required to answer this question.
Tip: To answer the last question think about specializations of the hospitals in the dataset and the unit of measurement of height.

Please note that the answers are independent of each other.

At this stage, use pandas visualization tools, seaborn or matplotlib. For second plot use pandas or matplotlib, this is necessary for the tests to run correctly.

Objectives
Use the DataFrame from the previous stage. The fifth stage requires completing one step:

Answer questions 1-3. Output the answers in the specified format. The answers to the first two questions should be formatted as in the examples. No special form is required to answer the third question

If you have corrupted CSV files, please download them and unzip in your working directory.

Example
The input is 3 CSV files, test/general.csv, test/prenatal.csv, and test/sports.csv.

The output:
(The following answers are given for reference only, the actual answers might be different)

The answer to the 1st question: 0-15
The answer to the 2nd question: flu
The answer to the 3rd question: It's because...
"""

