import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import joblib

df = pd.read_csv("dataset.csv")

X = df.drop("marks", axis=1)
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

models = {
    "Linear": LinearRegression(),
    "RandomForest": RandomForestRegressor(),
    "DecisionTree": DecisionTreeRegressor()
}

best_model = None
best_score = -1

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = r2_score(y_test, preds)

    print(name, score)

    if score > best_score:
        best_score = score
        best_model = model

joblib.dump(best_model, "model.pkl")