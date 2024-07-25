import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
url = "C:\code\paskaitu_failai\duomenu_analitika\databases\House_Prices_Advanced_Regression_train.csv"
df = pd.read_csv(url)

### Fill missing values
# print(df.info())


columns_to_drop = ['Street', 'Alley', 'Utilities', 'LandSlope', 'Condition2', 'RoofMatl',
                   'MasVnrArea','BsmtCond', 'BsmtFinSF2', 'Heating', 'Electrical',
                   'LowQualFinSF', 'BsmtHalfBath', 'KitchenAbvGr', 'Functional',
                   'GarageYrBlt', 'GarageQual', 'GarageCond', 'PavedDrive', '3SsnPorch',
                   'ScreenPorch', 'PoolQC', 'MiscFeature', 'MiscVal', 'Neighborhood',
                   'MSZoning', 'LotShape', 'LandContour', 'Condition1', 'BldgType',
                   'RoofStyle', 'Exterior1st', 'Exterior2nd', 'HouseStyle'
                  ]

df = df.drop(columns=columns_to_drop)

df.drop_duplicates(inplace=True)
# print(df.info())


for feature in df.select_dtypes(include=[np.number]).columns:  # Continuous features
    df[feature].fillna(df[feature].median(), inplace=True)
for feature in df.select_dtypes(include=['object']).columns:  # Categorical features
    df[feature].fillna(df[feature].mode()[0], inplace=True)

### Check for imbalance
# sns.boxplot(df['LotArea'])
# plt.title('LotArea')
# plt.show()

Q1 = df['LotArea'].quantile(0.25)
Q3 = df['LotArea'].quantile(0.75)
IQR = Q3 - Q1   
upperFilter = (df['LotArea'] >= Q3 + 1.5 * IQR)
df.loc[upperFilter,['LotArea']]  = Q3 + 1.5 * IQR
df['LotArea'].fillna(df['LotArea'].mean(), inplace=True)

# plt.title('LotArea after quantile')
# sns.boxplot(df['LotArea'])
# plt.show()


# for feature in df.select_dtypes(include=['object']).columns:
#     print(f"\n{feature} Value Counts (%):")
#     print(df[feature].value_counts(normalize=True) * 100)

# Transform LotArea to reduce outliers

# plt.hist(df['LotArea'], bins=19, edgecolor='black')
# plt.title('LotArea')
# plt.xlabel('LotArea')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

continuous_features = df.select_dtypes(include=[np.number]).columns.tolist()
continuous_summary = []
for feature in continuous_features:
    summary_dict = {
        'Feature': feature,
        'Count': df[feature].notnull().sum(),
        '% Miss': df[feature].isnull().mean() * 100,
        'Card.': df[feature].nunique(),
        'Min': df[feature].min(),
        'Q1': df[feature].quantile(0.25),
        'Mean': df[feature].mean(),
        'Median': df[feature].median(),
        'Q3': df[feature].quantile(0.75),
        'Max': df[feature].max(),
        'Std. Dev.': df[feature].std()
    }
    continuous_summary.append(summary_dict)
continuous_summary = pd.DataFrame(continuous_summary)

categorical_features = df.select_dtypes(include=['object']).columns.tolist()
categorical_summary = []
for feature in categorical_features:
    mode_value = df[feature].mode()[0]
    mode_freq = df[feature].value_counts().iloc[0]
    mode_percent = (mode_freq / df[feature].notnull().sum()) * 100
    second_mode = df[feature].value_counts().index[1] if len(df[feature].value_counts()) > 1 else np.nan
    second_mode_freq = df[feature].value_counts().iloc[1] if len(df[feature].value_counts()) > 1 else np.nan
    second_mode_percent = (second_mode_freq / df[feature].notnull().sum()) * 100 if len(df[feature].value_counts()) > 1 else np.nan
    
    summary_dict = {
        'Feature': feature,
        'Count': df[feature].notnull().sum(),
        '% Miss': df[feature].isnull().mean() * 100,
        'Card.': df[feature].nunique(),
        'Mode': mode_value,
        'Mode Freq': mode_freq,
        'Mode %': mode_percent,
        '2nd Mode': second_mode,
        '2nd Mode Freq': second_mode_freq,
        '2nd Mode %': second_mode_percent
    }
    categorical_summary.append(summary_dict)

categorical_summary = pd.DataFrame(categorical_summary)


print("\nContinuous Features Summary:")
print(continuous_summary)
print("\nCategorical Features Summary:")
print(categorical_summary)

### One-hot encoding
df = pd.get_dummies(df, drop_first=True)

### Standardization (continuous features)
scaler = StandardScaler()
df[continuous_features] = scaler.fit_transform(df[continuous_features])



