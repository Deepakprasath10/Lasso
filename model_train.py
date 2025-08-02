import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("rent_data.csv")

X = df.drop("rent", axis=1)
y = df["rent"]

cat_features = ["location"]
num_features = ["area", "bedrooms", "bathrooms"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(), cat_features)
], remainder='passthrough')

model = Pipeline([
    ("pre", preprocessor),
    ("regressor", Lasso(alpha=0.1))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("Model saved successfully.")
