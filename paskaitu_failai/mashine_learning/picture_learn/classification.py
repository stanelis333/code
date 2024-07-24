import os
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

dtrain = pd.read_csv('C:\\code\\paskaitu_failai\\mashine_learning\\picture_learn\\sign_mnist_train.csv')
dtest = pd.read_csv('C:\\code\\paskaitu_failai\\mashine_learning\\picture_learn\\sign_mnist_test.csv')

x_train = dtrain.drop('label', axis=1)
y_train = dtrain['label']

x_test = dtest.drop('label', axis=1)
y_test = dtest['label']

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)
print()
print("RandomForestClassifier:")
print(classification_report(y_test, y_pred_rf))
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"RandomForestClassifier: modelio tikslumas: {accuracy_rf}")



# Aplankų kūrimas ir nuotraukų išsaugojimas
output_dir = 'C:\\code\\paskaitu_failai\\mashine_learning\\picture_learn\\predictions'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for idx, pred in enumerate(y_pred_rf):
    pred_dir = os.path.join(output_dir, str(pred))
    if not os.path.exists(pred_dir):
        os.makedirs(pred_dir)
    
    img_data = x_test.iloc[idx].values.reshape(28, 28).astype(np.uint8)
    img = Image.fromarray(img_data, 'L')
    img_path = os.path.join(pred_dir, f'image_{idx}.png')
    img.save(img_path)

print(f"Nuotraukos sugrupuotos ir išsaugotos kataloge: {output_dir}")
