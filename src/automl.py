import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load your dataset
data = pd.read_csv('/content/steps_calories_data.csv')

X = data[['Calories_Burned']]  # Features
y = data['Steps']  # Target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LinearRegression": LinearRegression(),
    "KNeighborsRegressor": KNeighborsRegressor(),
    "Lasso": Lasso()
}

best_model = None
best_rmse = float('inf')

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"{name} RMSE: {rmse}")

    if rmse < best_rmse:
        best_rmse = rmse
        best_model = model

# Save the best model
joblib.dump(best_model, 'best_step_predictor.pkl')
print(f"Best model: {type(best_model).__name__} with RMSE: {best_rmse}")
