import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV

url = "C:\\code\\paskaitu_failai\\duomenu_analitika\\databases\\Student_performance_data.csv"
df = pd.read_csv(url)
print(df)
df = df.drop(['Gender', 'ParentalEducation', 'Ethnicity', 'Volunteering'], axis=1)

x = df.drop('GPA', axis=1)
y = df['GPA']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=49) 

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


rf = RandomForestRegressor(n_estimators=59, random_state=40)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)
mse_svm = mean_squared_error(y_test, y_pred_rf)
rmse_svm = np.sqrt(mse_svm)
print("RandomForestRegressor: Mean Squared Error:", mse_svm)
print("RandomForestRegressor: Root Mean Squared Error:", rmse_svm)

lf = LinearRegression()
lf.fit(x_train_scaled, y_train)
y_pred_lin = lf.predict(x_test_scaled)
mse_svm = mean_squared_error(y_test, y_pred_lin)
rmse_svm = np.sqrt(mse_svm)
print("LinearRegression: Mean Squared Error:", mse_svm)
print("LinearRegression: Root Mean Squared Error:", rmse_svm)

svm = SVR(kernel='rbf') 
svm.fit(x_train_scaled, y_train)
y_pred_svm = svm.predict(x_test_scaled)
mse_svm = mean_squared_error(y_test, y_pred_svm)
rmse_svm = np.sqrt(mse_svm)
print("SVR Mean Squared Error:", mse_svm)
print("SVR Root Mean Squared Error:", rmse_svm)

gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=0)
gbr.fit(x_train_scaled, y_train)
y_pred_gbr = gbr.predict(x_test_scaled)
mse_gbr = mean_squared_error(y_test, y_pred_gbr)
rmse_gbr = np.sqrt(mse_gbr)
print("GradientBoostingRegressor: Mean Squared Error:", mse_gbr)
print("GradientBoostingRegressor: Root Mean Squared Error:", rmse_gbr)

#--------------------------------------------------------------------  VISUAL  -------------------->

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(y_test, y_pred_gbr, alpha=0.5)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('GradientBoostingRegressor: Actual vs Predicted')

plt.subplot(1, 3, 2)
plt.scatter(y_test, y_pred_lin, alpha=0.5)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('LinearRegression: Actual vs Predicted')

plt.subplot(1, 3, 3)
plt.scatter(y_test, y_pred_svm, alpha=0.5)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('SVR: Actual vs Predicted')

plt.tight_layout()
plt.show()