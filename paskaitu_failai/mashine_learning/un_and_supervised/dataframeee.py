
import pandas as pd
import numpy as np

# name = pd.DataFrame({'Name': ['Justas', 'Antanas', 'Marius', 'Julius'] })
# age = pd.DataFrame({'Age': [21,25,22,23]})

# asmenys = pd.concat([name,age], axis=1)
# # print(asmenys)

# last_name = pd.DataFrame({'Last Name': ['John', 'Johnn', 'John', 'Johnn'] })
# asmenys1 = pd.concat([asmenys, last_name], axis=1)
# print(asmenys1)


#----------------------------------------------------------------

# df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion', 'monkey', 'parrot', 'shark', 'whale', 'zebra']})

# df2 = pd.DataFrame({'species': ['reptile', 'insect', 'bird', 'mammal', 'mammal', 'bird', 'fish', 'mammal', 'mammal']})

# combined = pd.concat([df,df2],axis=1)

# df3=pd.DataFrame({'life span':[20, 1, 4, 10, 20, 50, 10, 100, 70]})

# combined = pd.concat([combined,df3],axis=1)

# combined['naujas'] =[10,5,0,9,8,7,5,3,7]
# combined.drop('naujas',axis=1, inplace=True)

# print(combined)
# # print(combined.groupby('species')['life span'].mean())

#----------------------------------------------------------- 1. UZDUOTIS --------------------------------------
"""
country = pd.DataFrame({'Country': ['Lithuania', 'Italy', 'Latvia', 'Estonia', 'Poland']})
city = pd.DataFrame({'City': ['Vilnius', 'Rome', 'Riga', 'Tallinn', 'Warsaw']})
temperatureee = np.random.randint(-10,10, size=5)
temperature = pd.DataFrame(temperatureee, columns=['Temperature'])
weather = pd.concat([country, city, temperature], axis=1)
print(weather)

print()
print('ONLY 2 and 4:')
print(weather.iloc[[2,4]])

print()
print('BELOW ZERO:')
print(weather[weather['Temperature'] < 0])

print()
print('TEMPERATURE SUMMARY:')
print(weather['Temperature'].sum())

winddd = np.random.randint(3,30, size=5)
wind = pd.DataFrame(winddd, columns=['Wind m/s'])
weather = pd.concat([weather, wind], axis=1)
print()
print('ADDED WIND:')
print(weather)

weather['ColdRisk'] = weather['Temperature'].apply(lambda x: 'Yes' if x < 0 else 'No')
print()
print('ADDED ColdRisk:')
print(weather)

weather['Wind m/s'] = weather['Wind m/s'].apply(lambda x: 'Weak' if x < 10 else ('Normal' if x < 20 else 'Strong'))
print()
print('Change Wind rows:')
print(weather)

print()
print('Group by ColdRisk, average temperature:')
print(weather.groupby('ColdRisk')['Temperature'].mean())

print()
print('Sorted by temperature:')
print(weather.sort_values('Temperature', ascending=False))

#----------------------------------------------------------------------MERGING

days = []
for day in pd.date_range(start="2024-07-03", end="2024-07-07"):
    days.append(day) 
Date = pd.DataFrame(days, columns=['Date'])
onee = weather['Temperature']
print()
print()
one = pd.concat([Date, onee], axis=1)
print()
print('only date and temperature:')
print(one)

secondd = weather['Wind m/s']
second = pd.concat([Date, secondd], axis=1)
print()
print('only date and wind speed:')
print(second)

merged = pd.merge(one, second, on='Date')
print()
print('merged temperature and wind speed by date:')
print(merged)

"""
#---------------------------------------------------------------------- 2.UZDUOTIS------------------------------------

data = pd.read_csv("C:\\code\\paskaitu_failai\\duomenu_analitika\\databases\\train.csv")
print("All missing values in dataset:\n", data.isnull().sum())

data['Embarked'].fillna('?', inplace=True)
data['Cabin'].fillna('Who knows', inplace=True)
data['Age'].fillna(data['Age'].median(), inplace=True)
print()

data['FamilySize'] = data['SibSp'] + data['Parch']
data.drop(columns=['SibSp', 'Parch'], inplace=True)
print(data)
def categorize_age(age):
    if age < 18:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

data['AgeGroup'] = data['Age'].apply(categorize_age)

print()
print('Travel alone?')
data['TravelAlone'] = np.where(data['FamilySize'] > 0, 'No', 'Yes')
print(data)
print('Class ages average')
print(data.groupby('Pclass')['Age'].mean())     
