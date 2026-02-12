import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("heart_disease_data.csv")

X = df.drop("target", axis=1)
y = df["target"]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.1, random_state=1
)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)

def Predict(age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal):

    input_data = np.array([[
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope, ca, thal
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = knn.predict(input_scaled)

    return int(prediction[0])
