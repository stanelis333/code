import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data = pd.Series([5,4,3,1,8,7,9,5,6,4,4,2,1])
# data = data.sort_values(ascending=False)
# print(data)


# values = [104,105,106,101,102,103,107,108]
# ind= ['d','c','v','b','n','m','j','k',]
# data = pd.Series(values, ind)
# # data = pd.Series(ind, values)
# data = data.sort_values(ascending=False)

# data = data[data > 105]
# print(data)

#--------------------------------------------------------------------------------------------------------
# data = pd.read_csv("C:\code\paskaitu_failai\duomenu_analitika\databases\IMDb_Dataset.csv")
# data = data.drop_duplicates('Title')
# print(data.head(60))
# films = data[['Title', 'IMDb Rating']]
# films = films[films['IMDb Rating'] > 8.2]
# films = films.sort_values(by='IMDb Rating', ascending=False)
# # print (films.head(59))
# # films.set_index('Title')
# films.plt(kind='barh', title="Filmu grafikas", x="Title", y= "IMDb Rating", color="green")
# # plt.xlabel('Title')
# # plt.ylabel('IMDb Rating')
# plt.show()

#------------------------------------------------------------- 1.UZDUOTIS -------------------------------------------
# sk = [55,22,44,11,33]
# data = pd.Series(sk)
# print(data)

# count = data.count()
# print()
# print("kiek elementu")
# print(count)

# five_ele = data.iloc[4]
# print()
# print("penktas is saraso")
# print(five_ele)

# not_1_5 = data[1:4]
# print()
# print("be pirmo ir paskutinio")
# print(not_1_5)

# # skk = int(input('Iveskite skaiciu: '))
# # bigger_than_input = data[data > skk]
# # print("didesni skaiciai nei ivestas")
# # print(bigger_than_input)

# all_sum = data.sum()
# print()
# print("visu suma")
# print(all_sum)

# all_average = data.mean()
# print()
# print("visu vidurkis")
# print(all_average)

# multi = data.apply(lambda x: x*2)
# print()
# print("visi is saraso *2")
# print(multi)
# print()
# print()
# print()


# #--------------------------------

# sk = ['Baravykas', None, 'Anglis', 'Cementas', None, 'Anglis']
# data = pd.Series(sk)
# print("Su NONE reiksmem")
# print(data)

# drop_non = data.dropna()
# print()
# print("Ismestos NONE reiksmes")
# print(drop_non)

# upper = drop_non.str.upper()
# print()
# print("Didziosiom raidem")
# print(upper)

# uniq = data.value_counts()
# print()
# print("Suskaiciuoja reiksmes")
# print(uniq)

# data = drop_non.sort_values(ascending=True)
# print()
# print("Isrikiuota pagal abecele")
# print(data)




#------------------------------------------------------------- 2.UZDUOTIS -------------------------------------------


# year = []
# for day in pd.date_range(start="2024-01-01", end="2024-12-31"):
#     year.append(day) 
# days = pd.DataFrame(year, columns=['Data'])

# pajamosss = np.random.randint(50,500, size=366)
# pajamos = pd.DataFrame(pajamosss, columns=['Pajamos'])
# both = pd.concat([days, pajamos], axis=1)
# # print(both)

# both.set_index('Data', inplace=True)
# weekly_avg = both.resample('W').mean()
# monthly_avg = both.resample('ME').mean()
# # print(weekly_avg)
# # print(monthly_avg)

# both.loc['2024-03-17', 'Pajamos'] = 999
# both.loc['2024-07-20', 'Pajamos'] = 15
# both.loc['2024-03-15', 'Pajamos'] = 1300
# both.loc['2024-07-22', 'Pajamos'] = 9
# upper_threshold = 500
# lower_threshold = 50
# anomalies = both[(both['Pajamos'] > upper_threshold) | (both['Pajamos'] < lower_threshold)]
# # print(anomalies)

# # both.plt(kind='bar', title="pardavimai", y="Data", x= "Pajamos", color="green")
# # plt.xlabel('Pajamos')
# # plt.ylabel('Data')
# # plt.show()
