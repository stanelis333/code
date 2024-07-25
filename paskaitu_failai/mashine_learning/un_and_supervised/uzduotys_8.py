# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib.ticker import FuncFormatter
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.svm import SVR
# from sklearn.metrics import r2_score, mean_squared_error
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import GridSearchCV
# import os 
# os.environ['LOKY_MAX_CPU_COUNT'] = '8'


# # Load datasets
# dtrain = pd.read_csv('C:/code/paskaitu_failai/duomenu_analitika/databases/House_Prices_Advanced_Regression_train.csv')
# dtest = pd.read_csv('C:/code/paskaitu_failai/duomenu_analitika/databases/House_Prices_Advanced_Regression_test.csv')
# dsub = pd.read_csv('C:/code/paskaitu_failai/duomenu_analitika/databases/House_submission.csv')

# # Columns to drop
# columns_to_drop = ['Street', 'Alley', 'Utilities', 'LandSlope', 'Condition2', 'RoofMatl',
#                    'MasVnrArea','BsmtCond', 'BsmtFinSF2', 'Heating', 'Electrical',
#                    'LowQualFinSF', 'BsmtHalfBath', 'KitchenAbvGr', 'Functional',
#                    'GarageYrBlt', 'GarageQual', 'GarageCond', 'PavedDrive', '3SsnPorch',
#                    'ScreenPorch', 'PoolQC', 'MiscFeature', 'MiscVal', 'Neighborhood',
#                    'MSZoning', 'LotShape', 'LandContour', 'Condition1', 'BldgType',
#                    'RoofStyle', 'Exterior1st', 'Exterior2nd', 'HouseStyle'
#                   ]

# dtrain = dtrain.drop(columns=columns_to_drop)
# dtest = dtest.drop(columns=columns_to_drop)

# # Continuous features
# continuous_features = ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond',
#                        'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF',
#                        '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'BsmtFullBath', 'FullBath',
#                        'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars',
#                        'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', 'PoolArea',
#                        'MoSold', 'YrSold', 'SalePrice']


# indicators = ['MSSubClass', 'LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF']
# indicator_names = ['MSSubClass', 'LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF']
 
# fig, axes = plt.subplots(3, 2, figsize=(16, 13))
# fig.suptitle('house pricing', fontsize=15)

# for i, (indicator, name) in enumerate(zip(indicators , indicator_names)):
#     row, col = divmod(i, 2)
#     sns.violinplot(x='SalePrice', y=indicator, data=dtrain, ax=axes[row, col], palette="muted", split=True)
#     axes[row, col].set_title(f'SalePrice vs {name}')
#     axes[row, col].set_xlabel('')
#     axes[row, col].set_ylabel(name)
 
# plt.tight_layout()
# plt.show()


# # Handle outliers and missing values for continuous features in dtrain
# Q1 = dtrain[continuous_features].quantile(0.25)
# Q3 = dtrain[continuous_features].quantile(0.75)
# IQR = Q3 - Q1
# upperFilter = dtrain[continuous_features] >= (Q3 + 1.5 * IQR)

# for column in continuous_features:
#     value_to_assign = Q3[column] + 1.5 * IQR[column]
#     value_to_assign = value_to_assign.astype(dtrain[column].dtype)
#     dtrain.loc[upperFilter[column], column] = value_to_assign
    
# dtrain[continuous_features] = dtrain[continuous_features].fillna(dtrain[continuous_features].mean())
# dtrain.fillna(dtrain.select_dtypes(include=['object']).mode().iloc[0], inplace=True)

# # Continuous and categorical features for dtest
# dtest.fillna(dtest.select_dtypes(include=[np.number]).median(), inplace=True)
# dtest.fillna(dtest.select_dtypes(include=['object']).mode().iloc[0], inplace=True)

# # Convert categorical variables to dummies
# categorical_features = dtrain.select_dtypes(include=['object']).columns
# categorical_features_test = dtest.select_dtypes(include=['object']).columns
# dtrain = pd.get_dummies(dtrain, columns=categorical_features, drop_first=True)
# dtest = pd.get_dummies(dtest, columns=categorical_features_test, drop_first=True)

# # Align train and test datasets
# # dtrain, dtest = dtrain.align(dtest, join='left', axis=1, fill_value=0)

# # Split features and target
# X_train = dtrain.drop('SalePrice', axis=1)
# y_train = dtrain['SalePrice']
# X_test = dtest
# y_test = dsub.drop('Id', axis=1).squeeze()

# # K-Nearest Neighbors
# param_grid = {'n_neighbors': list(range(1, 101))}
# knn = KNeighborsRegressor(n_neighbors=146)
# knn.fit(X_train, y_train)
# y_pred_knn = knn.predict(X_test)
# grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
# grid_search.fit(X_test, y_test)
# best_params = grid_search.best_params_
# best_score = np.sqrt(-grid_search.best_score_)
# # print(f"KNN Best parameters for KNN: {best_params}")
# # print(f"KNN Best RMSE from GridSearchCV: {best_score}")
# mse_svm = mean_squared_error(y_test, y_pred_knn)
# rmse_svm = np.sqrt(mse_svm)
# print("KNN Mean Squared Error:", mse_svm)
# print("KNN Root Mean Squared Error:", rmse_svm)


# # Decision Tree
# param_grid_tree = {'max_depth': [10]}
# tree = DecisionTreeRegressor(max_depth=1,min_samples_split=10,min_samples_leaf=10,max_features=3,random_state=42)
# grid_search_tree = GridSearchCV(tree, param_grid_tree, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
# grid_search_tree.fit(X_train, y_train)
# best_params_tree = grid_search_tree.best_params_
# best_score_tree = np.sqrt(-grid_search_tree.best_score_)
# tree.fit(X_train, y_train)
# y_pred_tree = tree.predict(X_test)
# # print(f"Decision Tree Best parameters: {best_params_tree}")
# # print(f"Decision Tree Best RMSE from GridSearchCV: {best_score_tree}")
# mse_svm = mean_squared_error(y_test, y_pred_tree)
# rmse_svm = np.sqrt(mse_svm)
# print("Decision Tree Mean Squared Error:", mse_svm)
# print("Decision Tree Root Mean Squared Error:", rmse_svm)



# # Support Vector Machine
# svm = SVR(kernel='rbf', C=23.0) 
# svm.fit(X_train, y_train)
# y_pred_svm = svm.predict(X_test)
# mse_svm = mean_squared_error(y_test, y_pred_svm)
# rmse_svm = np.sqrt(mse_svm)
# print("SVM Mean Squared Error:", mse_svm)
# print("SVM Root Mean Squared Error:", rmse_svm)

# #----------------------------------------------------------------------------Visual

# # Function to format y-axis labels in thousands
# def thousands_formatter(x, pos):
#     return f'{int(x/1000)}k'

# # Plot predictions vs actual values for KNN
# plt.figure(figsize=(15, 5))

# plt.subplot(1, 3, 1)
# plt.scatter(y_test, y_pred_knn, alpha=0.5)
# plt.xlabel('Actual Price')
# plt.ylabel('Predicted Price')
# plt.title('KNN: Actual vs Predicted Price')
# plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# # Plot predictions vs actual values for SVM
# plt.subplot(1, 3, 2)
# plt.scatter(y_test, y_pred_svm, alpha=0.5)
# plt.xlabel('Actual Price')
# plt.ylabel('Predicted Price')
# plt.title('SVM: Actual vs Predicted Price')
# plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# # Plot predictions vs actual values for Decision Tree
# plt.subplot(1, 3, 3)
# plt.scatter(y_test, y_pred_tree, alpha=0.5)
# plt.xlabel('Actual Price')
# plt.ylabel('Predicted Price')
# plt.title('Decision Tree: Actual vs Predicted Price')
# plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# plt.tight_layout()
# # plt.show()

