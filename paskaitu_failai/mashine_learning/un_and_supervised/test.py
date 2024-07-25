import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

url = "C:\\code\\paskaitu_failai\\duomenu_analitika\\databases\\BTC.csv"
df = pd.read_csv(url)
df = df[['date', 'open', 'high', 'low', 'close']]
print(df.tail(4))

x = df.drop(['high', 'date', 'low'], axis=1)
print(x.tail(5))
y = df[['high', 'low']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=49)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = LinearRegression()
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)

# knn_model = KNeighborsRegressor(n_neighbors=7)
# knn_model.fit(x_train_scaled, y_train)
# y_pred_knn = knn_model.predict(x_test_scaled)
# print("KNeighborsRegressor:")
# print(f"Mean Squared Error (KNN): {mean_squared_error(y_test, y_pred_knn)}")
# print(f"R^2 Score (KNN): {r2_score(y_test, y_pred_knn)}")

print()
print("LinearRegression:")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R^2 Score: {r2_score(y_test, y_pred)}")
