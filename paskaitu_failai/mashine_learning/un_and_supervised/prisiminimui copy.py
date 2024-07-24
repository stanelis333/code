import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
os.environ['LOKY_MAX_CPU_COUNT'] = '8'

# # Sukurkite 1D masyvą iš sąrašo [10, 20, 30, 40, 50]

# array_1d = np.array([10, 20, 30, 40, 50])
# print("1D masyvas:", array_1d)
# print(f"Forma: {array_1d.shape}")
# print("Duomenų tipas:", array_1d.dtype)

# # Sukurkite 2D masyvą su 3x3 dimensijomis, užpildytą atsitiktiniais sveikaisiais skaičiais tarp 0 ir 100

# array_2d = np.random.randint(0, 101, (3, 3))
# suma = array_2d.sum()
# vidurkis = array_2d.mean()
# print("2D masyvas:\n", array_2d)
# print("Visų elementų suma:", suma)
# print("Vidurkis:", vidurkis)

# # Sukurkite Pandas DataFrame su 3 stulpeliais ('Vardas', 'Amžius', 'Balas') ir 5 atsitiktinių duomenų eilutėmis
# data = {
#     'Vardas': ['Jonas', 'Petras', 'Ona', 'Ieva', 'Rasa'],
#     'Amžius': np.random.randint(18, 60, 5),
#     'Balas': np.random.randint(0, 100, 5)
# }
# df = pd.DataFrame(data)
# print("DataFrame:\n", df)
# print("\nKiekvieno stulpelio duomenų tipai:\n", df.dtypes)

# # Linijinės grafikos sukūrimas naudojant Seaborn

# x = np.arange(0, 11)
# y = 2 * x + 3

# sns.lineplot(x=x, y=y)
# plt.xlabel('x reikšmės')
# plt.ylabel('y reikšmės')
# plt.title('Linijinė grafika: y = 2x + 3')
# plt.show()

# #   Prideti random miestus

# miestai = ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys']
# df['Miestas'] = np.random.choice(miestai, 5)
# print("\nAtnaujintas DataFrame:\n", df)

# filtered_df = df[df['Amžius'] > 20]
# print("\nFiltruotas DataFrame (Amžius > 20):\n", filtered_df)

# grouped_df = df.groupby('Miestas')['Balas'].mean().reset_index()
# print("\nVidutinis balas pagal miestą:\n", grouped_df)

# #Histogramos grafikos sukūrimas
# random_integers = np.random.randint(0, 100, 100)
# sns.histplot(random_integers, bins=10)
# plt.xlabel('Reikšmės')
# plt.ylabel('Dažnis')
# plt.title('Atsitiktinių sveikųjų skaičių pasiskirstymas')
# plt.show()


#--------------------------------------------------------------- Average ---------------------------------------------------------


# # Sukurkite 3D masyvą su (2, 3, 4) forma, užpildytą atsitiktiniais skaičiais

# array_3d = np.random.random((2, 3, 4))
# print("3D masyvas:\n", array_3d)

# # Sukurkite 2D masyvą su 5x5 dimensijomis, užpildytą atsitiktiniais sveikaisiais skaičiais tarp 0 ir 100
# array_2d = np.random.randint(0, 101, (5, 5))
# print("2D masyvas:\n", array_2d)
# print("Forma:", array_2d.shape)
# print("Duomenų tipas:", array_2d.dtype)

# vidurkiai = array_2d.mean(axis=0)
# stds = array_2d.std(axis=0)

# array_2d_normalized = (array_2d - vidurkiai) / stds
# print("\nNormalizuotas masyvas:\n", array_2d_normalized)
# array_2d_squared = np.square(array_2d)
# print("\nPradinio masyvo kvadratai:\n", array_2d_squared)


# # Sukurkite Pandas DataFrame su 4 stulpeliais ('Produktas', 'Kaina', 'Kiekis', 'Kategorija') ir 10 atsitiktinių duomenų eilutėmis
# data = {
#     'Produktas': ['Produktas'+str(i) for i in range(1, 11)],
#     'Kaina': np.random.randint(10, 100, 10),
#     'Kiekis': np.random.randint(1, 10, 10),
#     'Kategorija': np.random.choice(['Maistas', 'Gėrimai', 'Drabužiai', 'Elektronika'], 10)
# }
# df = pd.DataFrame(data)
# print("DataFrame:\n", df)
# print("\nKiekvieno stulpelio duomenų tipai:\n", df.dtypes)

# df['Bendra Kaina'] = df['Kaina'] * df['Kiekis']

# food_df = df[df['Kategorija'] == 'Maistas']

# avg_price_per_category = df.groupby('Kategorija')['Kaina'].mean().reset_index()

# pivot_table = df.pivot_table(values='Bendra Kaina', index='Kategorija', aggfunc='sum').reset_index()

# print("\nDataFrame su 'Bendra Kaina':\n", df)
# print("\nFiltruotos eilutės ('Maistas'):\n", food_df)
# print("\nVidutinė kaina pagal kategoriją:\n", avg_price_per_category)
# print("\nPivot lentelė su bendromis kainomis:\n", pivot_table)


#-------------------------------------------------------------------------------------------------------

# csv_path = 'C:\\code\\paskaitu_failai\\duomenu_analitika\\databases\\seattle-weather.csv'
# weather_df = pd.read_csv(csv_path)
# weather_df['temp_average'] = (weather_df['temp_max'] + weather_df['temp_min']) / 2
# weather_df = weather_df.drop(['temp_max', 'temp_min', 'wind', 'weather'], axis=1)

# print("Pirmos 10 eilutės:\n", weather_df.head(10))
# print("\nBendra informacija apie duomenis:\n")
# weather_df.info()

# weather_df['Month'] = pd.to_datetime(weather_df['date']).dt.month
# monthly_stats = weather_df.groupby('Month').agg({'temp_average': 'mean', 'precipitation': 'sum'}).reset_index()

# print("\nVidutinė temperatūra ir bendras kritulių kiekis pagal mėnesį:\n", monthly_stats)


# #Užduotis: Naudodami Seaborn, sukurkite daugiafunkcinį grafiką, kuriame būtų linijinė grafika, barplot grafikas ir histograma.

# x = np.arange(0, 21)
# y = 2 * x + 3
# prekiu_pavadinimai = ['Prekė1', 'Prekė2', 'Prekė3', 'Prekė4', 'Prekė5']
# pardavimai = np.random.randint(10, 100, 5)
# random_numbers = np.random.randint(0, 101, 50)

# fig, ax = plt.subplots(1, 3, figsize=(10, 10))

# sns.lineplot(x=x, y=y, ax=ax[0])
# ax[0].set_title('Linijinis grafikas: y = 2x + 3')
# ax[0].set_xlabel('x')
# ax[0].set_ylabel('y')

# sns.barplot(x=prekiu_pavadinimai, y=pardavimai, ax=ax[1])
# ax[1].set_title('Prekių pardavimai')
# ax[1].set_xlabel('Prekės')
# ax[1].set_ylabel('Pardavimai')

# sns.histplot(random_numbers, bins=10, ax=ax[2])
# ax[2].set_title('Atsitiktinių skaičių paskirstymas')
# ax[2].set_xlabel('Reikšmės')
# ax[2].set_ylabel('Dažnis')

# plt.tight_layout()
# plt.show()

#------------------------------------------------------------------------------------------------------------------------------------

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix
# from sklearn.datasets import load_iris
# iris = load_iris()


# X = iris.data[iris.target != 2]
# y = iris.target[iris.target != 2]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LogisticRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)
# recall = recall_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred)

# print("Tikslumas:", accuracy)
# print("Jautrumas:", recall)
# print("Specifiškumas:", precision)

# conf_matrix = confusion_matrix(y_test, y_pred)
# print("Painiavos matrica:\n", conf_matrix)


# #--------------------------------------------------------------------------


# X = iris.data

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# sse = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X_scaled)
#     sse.append(kmeans.inertia_)

# plt.figure(figsize=(8, 5))
# plt.plot(range(1, 11), sse, marker='o')
# plt.xlabel('K reikšmė')
# plt.ylabel('Sum of Squared Errors (SSE)')
# plt.title('Alkūnės metodas')
# plt.show()

# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans.fit(X_scaled)

# print("Klasterių centrai:\n", kmeans.cluster_centers_)

# clusters = kmeans.labels_

# plt.figure(figsize=(8, 5))
# plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', marker='o')
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
# plt.xlabel('Savybė 1')
# plt.ylabel('Savybė 2')
# plt.title('K-klasių Kaimynų klasterizavimas')
# plt.legend()
# plt.show()


