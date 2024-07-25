import numpy as np

# data = np.array([10,22,22,66,44,8,55,44])

# print(data)

# mean = np.mean(data)
# print (f"Mean: {mean}")

# median = np.median(data)
# print ( f"Median: {median}" )

# std = np.std(data)
# print(f"Standart Deviation: {std}")

# max = np.max(data)
# print (f"Max: {max}")

# min = np.min(data)
# print(f"Min: {min}" )

#----------------------------------------------------------------

# data4 = np.array([[1,2,3],[4,5,6], [7,8,9], [1,2,3], [4,5,6], [7,8,9],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[4,5,6],[7,8,9]])

# print(f"Data 4: \n{data4}")

# # array[start: stop:step, start:stop:step]


# slice_data4 = data4[::11, :1]
# print(f"Slice Data 4: \n{slice_data4}")

# # value_data4 = data4[0, 2]
# # print(f"Value Data 4: \n{value_data4}")

#----------------------------------------------------------------

# data6 = np.random.normal(100, 13, (5,5))
# data6 = np.round(data6).astype(int)
# print(f"Value Data 6: \n{data6}")


# data6 = np.random.randint(0, 10, (3,3))
# print(f"Value Data 6: \n{data6}")

#----------------------------------------------------------------

# data7 = np.array([[1,2,3]])
# data8 = np.array([[4,5,6]])

# print(f"Value Data 7: \n{data7}")
# print(f"Value Data 8: \n{data8}")

# data_vertical = np.vstack((data7, data8))
# data_horizontal = np.hstack((data7, data8))

# print(f"Value Data Vertical: \n{data_vertical}")
# print(f"Value Data Horizontal: \n{data_horizontal}")


#----------------------------------------------------------------1.UZDUOTIS----------------------------------------------------


# data = np.array([1, 2, 3, 4, 5])

# data2 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# data3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # value_data3 = data3[1,1]
# # print(value_data3)
# slice_data3 = data3[:2, 1:3]
# print(data3)
# print(slice_data3)

#-------------------------------------------------------------

# data4 = np.array([1, 2, 3])
# data5 = np.array([4, 5, 6])

# sudetis = data4 + data5
# print(f"sudejus: {sudetis}")
# atimtis = data4 - data5
# print(f"atemus: {atimtis}")
# daugyba = data4 * data5
# print(f"sudauginus: {daugyba}")
# dalyba = data4 / data5
# print(f"padalinus: {dalyba}")

# data_horizontal = np.hstack((data4, data5))

# sum = np.sum([data_horizontal])
# print (f"Suma: {sum}")

# mean = np.mean([data_horizontal])
# print (f"Vidurkis: {mean}")

# max = np.max([data_horizontal])
# print (f"Maximumas: {max}")

# min = np.min([data_horizontal])
# print (f"Minimumas: {min}")

#----------------------------------------------------------------

# data = np.array([0, np.pi/2, np.pi])

# sin_data = np.sin(data)
# cos_data = np.cos(data)
# tan_data = np.tan(data)

# exp_data = np.exp(data)
# log_data = np.log(data[1:])  

# print("Sin:", sin_data)
# print("Cos:", cos_data)
# print("Tan:", tan_data)

# print("Exponentials:", exp_data)
# print("Natural Logarithms:", log_data)

#----------------------------------------------------------------
#-------------------------------------------------------------------2.UZDUOTIS-----------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(0)

# Define the date range for one year (2024)
date_range = pd.date_range(start="2024-01-01", end="2024-12-31")

# Generate random temperatures for each month separately
temperatures = []

for month in range(1, 13):
    days_in_month = pd.date_range(start=f"2024-{month:02d}-01", end=f"2024-{month:02d}-01").days_in_month
    if month in [12, 1, 2]:  # Winter months
        month_temps = np.random.uniform(low=-25, high=11, size=days_in_month)
    elif month in [3, 4, 5]:  # Spring months
        month_temps = np.random.uniform(low=-5, high=27, size=days_in_month)
    elif month in [6, 7, 8]:  # Summer months
        month_temps = np.random.uniform(low=10, high=35, size=days_in_month)
    elif month in [9, 10, 11]:  # Autumn months
        month_temps = np.random.uniform(low=-15, high=25, size=days_in_month)
    temperatures.extend(month_temps)

# Convert to a NumPy array
temperatures = np.array(temperatures)

# Create a DataFrame to store the dates and temperatures
weather_data = pd.DataFrame({
    "Date": date_range,
    "Temperature": temperatures
})

# Insert anomalies
weather_data.loc[weather_data['Date'] == '2024-01-15', 'Temperature'] = 10  # Unusually warm day in January
weather_data.loc[weather_data['Date'] == '2024-01-20', 'Temperature'] = -30  # Sudden drop in temperature

# Calculate monthly average temperatures
weather_data['Month'] = weather_data['Date'].dt.month
monthly_avg_temps = weather_data.groupby('Month')['Temperature'].mean()

# Identify anomalies using standard deviation
std_dev = weather_data['Temperature'].std()
mean_temp = weather_data['Temperature'].mean()
anomalies = weather_data[(weather_data['Temperature'] > mean_temp + 2 * std_dev) | 
                         (weather_data['Temperature'] < mean_temp - 2 * std_dev)]

# Print the results
print("Weather Data for One Year (2024):")
print(weather_data.head())

print("\nMonthly Average Temperatures:")
print(monthly_avg_temps)

print("\nAnomalies:")
print(anomalies)

# Advanced: Plot the data and highlight anomalies
plt.figure(figsize=(14, 7))
plt.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature', color='blue')
plt.scatter(anomalies['Date'], anomalies['Temperature'], color='red', label='Anomalies')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Data for 2024 with Anomalies Highlighted')
plt.legend()
plt.show()














