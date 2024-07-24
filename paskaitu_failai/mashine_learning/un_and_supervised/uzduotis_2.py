
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

url = "C:\code\paskaitu_failai\duomenu_analitika\databases\prekes.csv"
df = pd.read_csv(url)
print(df.head(4))
df = df[['Kaina', 'Svoris', 'Kategorija']]


df['Kategorija'], _ = pd.factorize(df['Kategorija'])
x = df.drop(columns=['Kategorija'])
y = df['Kategorija']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=11) 

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

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

conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Drabužiai', 'Elektronika', 'Maistas'], yticklabels=['Drabužiai', 'Elektronika', 'Maistas'])
plt.xlabel('Prognozuotos reikšmės')
plt.ylabel('Tikrosios reikšmės')
plt.title('Klaidų matrica')
plt.show()

#------------------------------------------------------
