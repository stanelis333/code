
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

url = "C:\\code\\paskaitu_failai\\duomenu_analitika\\databases\\train.csv"
df = pd.read_csv(url)
print(df.head(12))
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']] #for KN best -3
df['Age'] = df['Age'].fillna(df['Age'].median())

df = pd.get_dummies(df, drop_first=True)
x = df.drop('Survived', axis=1)
y = df['Survived']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.08, random_state=49) 

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

knn_model = KNeighborsClassifier(n_neighbors=7)
knn_model.fit(x_train_scaled, y_train)
y_pred_knn = knn_model.predict(x_test_scaled)
print("KNeighborsClassifier:")
print(classification_report(y_test, y_pred_knn))
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"KNN modelio tikslumas: {accuracy_knn}")


model = LogisticRegression()
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)
print()
print("LogisticRegression:")
print(classification_report(y_test, y_pred))
accuracy = accuracy_score(y_test, y_pred)
print(f"Modelio tikslumas: {accuracy}")

#----------------------------------------------------------------

#visual

# conf_matrix = confusion_matrix(y_test, y_pred)
# sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Nepavyko išgyventi', 'Pavyko išgyventi'], yticklabels=['Nepavyko išgyventi', 'Pavyko išgyventi'])
# plt.xlabel('Prognozuotos reikšmės')
# plt.ylabel('Tikrosios reikšmės')
# plt.title('Klaidų matrica')
# plt.show()

#------------------------------------------------------

# print(df.head())
# # Faktiniai duomenys pagal amziu
# plt.figure(figsize=(16, 7))
# plt.subplot(1, 2, 1)
# sns.histplot(x='Age', hue='Survived', data=df, kde=True, palette='Set1', bins=30)
# plt.title('Survival Distribution by Age (Actual)')
# plt.xlabel ('Age')
# plt.ylabel('Count')

# # Nuspejami duomenys pagal amziu
# plt.subplot(1, 2, 2)
# df_pred = pd.DataFrame({'Age': x_test['Age'], 'Survived': y_pred})
# sns.histplot(x='Age', hue='Survived', data=df_pred, kde=True, palette='Set2', bins=30)
# plt.title('Predicted Survival Distribution by Age')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.tight_layout()
# plt.show()

# print("-------------")