import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import os 
import warnings
warnings.filterwarnings('ignore')
os.environ['LOKY_MAX_CPU_COUNT'] = '8'

url = "C:\\code\\paskaitu_failai\\duomenu_analitika\\databases\\smoking_driking_dataset_Ver01.csv"
df = pd.read_csv(url)

# print(df.head(7))
# print(df.isna().sum())
# print(df.info())
# print(df.describe())

df = df.sample(frac=0.011, random_state=28)
df = pd.get_dummies(df, drop_first=True)

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Koreliacija')
plt.show()

df = df.drop(['urine_protein', 'hear_left', 'hear_right', 'tot_chole'], axis=1)

# plt.title('before ouliers apply')
# sns.boxplot(df)
# plt.show()

continuous_features = ['height', 'weight', 'waistline', 'sight_left',
                       'sight_right', 'SBP', 'DBP', 'triglyceride',
                       'hemoglobin', 'serum_creatinine', 'SGOT_AST',
                         'SGOT_ALT', 'gamma_GTP', 'LDL_chole', 'BLDS']

# Handle outliers and missing values for continuous features in df
Q1 = df[continuous_features].quantile(0.25)
Q3 = df[continuous_features].quantile(0.75)
IQR = Q3 - Q1
upperFilter = df[continuous_features] >= (Q3 + 1.5 * IQR)
lowerFilter = df[continuous_features] <= (Q3 - 1.5 * IQR)

for column in continuous_features:
    value_to_assign = Q3[column] + 1.5 * IQR[column]
    value_to_assign = value_to_assign.astype(df[column].dtype)
    df.loc[upperFilter[column], column] = value_to_assign
    
    lower_value_to_assign = Q1[column] - 1.5 * IQR[column]
    lower_value_to_assign = lower_value_to_assign.astype(df[column].dtype)
    df.loc[lowerFilter[column], column] = lower_value_to_assign


# plt.title('after outliers apply')
# sns.boxplot(df)
# plt.show()
#-------------------------------------------  some VISUAL --------------------------------------

df['DRK_YN_Y'] = df['DRK_YN_Y'].apply(lambda x: 1 if x == True else 0)
smoking_drinking_crosstab = pd.crosstab(df['SMK_stat_type_cd'], df['DRK_YN_Y'])
plt.figure(figsize=(10, 6))
sns.heatmap(smoking_drinking_crosstab, annot=True, fmt='d', cmap='coolwarm', cbar=False)
plt.title('Relationship between Smoking and Drinking')
plt.xlabel('Drinking (1 = Yes, 0 = No)')
plt.ylabel('Smoking state, 1(never), 2(used to smoke but quit), 3(still smoke)')
plt.show()

indicators = ['gamma_GTP', 'SGOT_AST', 'SGOT_ALT', 'triglyceride', 'hemoglobin', 'serum_creatinine']
indicator_names = ['Gamma GTP', 'SGOT AST', 'SGOT ALT', 'Triglyceride', 'Hemoglobin', 'Serum Creatinine']
 
fig, axes = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle('Drinking vs Health Indicators', fontsize=15)

for i, (indicator, name) in enumerate(zip(indicators , indicator_names)):
    row, col = divmod(i, 2)
    sns.violinplot(x='DRK_YN_Y', y=indicator, data=df, ax=axes[row, col], palette="muted", split=True)
    axes[row, col].set_title(f'Drinking vs {name}')
    axes[row, col].set_xlabel('(Drinking) 1 = Yes, 0 = No')
    axes[row, col].set_ylabel(name)
 
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------


x = df.drop('DRK_YN_Y', axis=1)
y = df['DRK_YN_Y']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=49) 

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

#--------------------------------------------------------------------------------------------

model = LogisticRegression()
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)
print()
print("LogisticRegression:")
print(classification_report(y_test, y_pred))
accuracy_log = accuracy_score(y_test, y_pred)

#--------------------------------------------------------------------------------------------

knn_model = KNeighborsClassifier(n_neighbors=55)
knn_model.fit(x_train_scaled, y_train)
y_pred_knn = knn_model.predict(x_test_scaled)
print("KNeighborsClassifier:")
print(classification_report(y_test, y_pred_knn))
accuracy_knn = accuracy_score(y_test, y_pred_knn)

#--------------------------------------------------------------------------------------------

svm = SVC(kernel='rbf') 
svm.fit(x_train_scaled, y_train)
y_pred_svm = svm.predict(x_test_scaled)
print()
print("SVC:")
print(classification_report(y_test, y_pred_svm))
accuracy_svc = accuracy_score(y_test, y_pred_svm)

#--------------------------------------------------------------------------------------------

rf = RandomForestClassifier(n_estimators=56, random_state=55)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)
print()
print("RandomForestClassifier:")
print(classification_report(y_test, y_pred_rf))
accuracy_rf = accuracy_score(y_test, y_pred_rf)

#--------------------------------------------------------------------------------------------

# param_grid_gbc = {
#     'n_estimators': [50, 100, 150],
#     'learning_rate': [0.01, 0.1, 0.2],
#     'max_depth': [3, 4, 5],
#     'subsample': [0.8, 1.0]
# }
# grid_gbc = GridSearchCV(GradientBoostingClassifier(random_state=0), param_grid_gbc, cv=5, n_jobs=-1)
# grid_gbc.fit(x_train_scaled, y_train)
# best_gbc = grid_gbc.best_estimator_
# y_pred_gbc = best_gbc.predict(x_test_scaled)
# print("\nBest GradientBoostingClassifier:")
# print(classification_report(y_test, y_pred_gbc))
# accuracy_gbc = accuracy_score(y_test, y_pred_gbc)
# print(f"\nBest accuracy GradientBoostingClassifier:{accuracy_gbc}")

gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=0)
gbc.fit(x_train_scaled, y_train)
y_pred_gbc = gbc.predict(x_test_scaled)
print()
print("GradientBoostingClassifier:")
print(classification_report(y_test, y_pred_gbc))
accuracy_gbc = accuracy_score(y_test, y_pred_gbc)

#--------------------------------------------------------------------------------------------

print(f"RandomForestClassifier: modelio tikslumas: {accuracy_rf}")
print(f"LogisticRegression: Modelio tikslumas: {accuracy_log}")  
print(f"GradientBoostingClassifier: Modelio tikslumas: {accuracy_gbc}") 
print(f"SVC: Modelio tikslumas: {accuracy_svc}")  
print(f"KNN modelio tikslumas: {accuracy_knn}")

#-------------------------------------------------------------------------------------------- VISUAL  >>>>>>>>
accuracy_data = {
    'Model': ['Random Forest','Logistic Regression',  'Gradient Boosting', 'SVC', 'K-Nearest Neighbors'],
    'Accuracy': [accuracy_rf, accuracy_log, accuracy_gbc, accuracy_svc, accuracy_knn]
}
accuracy_df = pd.DataFrame(accuracy_data)
plt.figure(figsize=(10, 6))
sns.barplot(x='Model', y='Accuracy', data=accuracy_df, palette='rocket')
plt.title('Accuracy Comparison of Different Models')
plt.xlabel('')
plt.ylabel('Accuracy')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
 
