import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# x = [1,3,1,7,9]
# # y = [2,4,6,8,10]

# sns.set_theme(style="darkgrid")
# sns.lineplot(x)
# plt.title('Test#######################')
# plt.xlabel('X_line_name')
# plt.ylabel('Y_line_name')
# plt.show()



# names = ["Justas", "Karolis", "Mantas"]
# counts = [41,58,5]
# sns.set_theme(style="darkgrid")
# sns.lineplot(y=counts,x=names) #sea.barplot(y=counts,x=names)  BUS STULPELINIS GRAFIKAS
# plt.show()


#---------------------------------------------------------------- 1.Uzduotis--------------------


titanic = sns.load_dataset('titanic')

# sns.countplot(data = titanic, x='class', hue='sex', palette = "Set2")
# plt.title('Number of Passengers in Each Class')
# plt.xlabel('Class')
# plt.ylabel('Number of Passengers')
# plt.show()

# sns.catplot(data=titanic, x='class', hue='survived', col='sex', kind='count', palette = "Set1")
# plt.suptitle('Survival by Gender and Class')
# plt.show()

# sns.boxplot(x='class', y='age', data=titanic, palette = "Set2")
# plt.title('Classes Distribution by Age')
# plt.xlabel('Class')
# plt.ylabel('Age')
# plt.show()

# age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
# titanic['age_group'] = pd.cut(titanic['age'], bins=age_bins)
# age_group_counts = titanic.groupby(['age_group', 'survived']).size().unstack(fill_value=0).reset_index()
# age_group_counts_melted = age_group_counts.melt(id_vars='age_group', value_vars=[0, 1], var_name='survived', value_name='count')
# sns.barplot(x='age_group', y='count', hue='survived', data=age_group_counts_melted)
# plt.title('Survival by Age')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()

# numerical_cols = titanic.select_dtypes(include=['float64', 'int64']).columns
# corr_matrix = titanic[numerical_cols].corr()
# sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='twilight_shifted', linewidths=0.5)
# plt.title('Correlation Heatmap of Numerical Variables')
# plt.show()

# age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
# titanic['age_group'] = pd.cut(titanic['age'], bins=age_bins)
# age_gender= titanic.groupby(['age_group', 'sex', 'survived']).size().unstack(fill_value=0).reset_index()
# age_gender_melted = age_gender.melt(id_vars=['age_group', 'sex'], value_vars=[0, 1], var_name='survived', value_name='count')
# sns.catplot(x='age_group', y='count', hue='survived', col='sex', data=age_gender_melted, kind='bar')
# plt.suptitle('Survival by Age and Gender')
# plt.xlabel('age_group')
# plt.ylabel('Count')
# plt.show()

