# Fitness App Step Counter

This project is part of the **'Enterprise Guide to DataOps and MLOps'** lab assignment. It involves building a Python-based step counter that tracks daily activity and provides insights on weekly performance, along with predictive analytics using AutoML techniques to forecast future step counts.

## Features

### StepCounter Class
The core of this project is the `StepCounter` class, which tracks the following metrics:
- **Daily Steps**: Logs the number of steps taken each day.
- **Total Weekly Steps**: Calculates the sum of steps over the past week.
- **Average Daily Steps**: Provides the average number of daily steps over a week.
- **Activity Level Feedback**: Categorizes activity as low, moderate, or high based on the total number of steps.

The data is stored in a table with the following columns:
- `Date`: The date on which the steps were taken.
- `Steps`: The number of steps taken.
- `Calories_Burned`: Estimated calories burned based on the number of steps.

### Project Structure
This project follows a structured branching strategy:
- **Main branch**: Holds stable and tested versions of the project.
- **Development branch**: Used for integrating new features like setting daily step goals.
- **Feature branches**: Separate branches for specific functionalities, such as:
  - **Calories Calculation**: Implement functionality to calculate calories burned from steps.
  - **Other features**: Additional functionality is merged into development, and later into main.

### AutoML Predictions
The project uses AutoML to predict future step counts based on historical activity data. Three models are compared:
1. **Linear Regression**
2. **KNeighbors Regressor**
3. **Lasso**

The model with the lowest RMSE (Root Mean Squared Error) is selected for future predictions.

Columns used for prediction:
- `Age`
- `Steps`
- `Calories_Burned`
- `Weight`

### Testing
We use `unittest` to ensure the accuracy and reliability of the `StepCounter` class:
- Verify total weekly steps calculation.
- Ensure high activity levels are correctly identified.

## Installation

To set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Pratikchetry/fitness-app-step-counter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd fitness-app-step-counter
    ```

3. Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Initialize the `StepCounter` class to track daily steps:
    ```python
    from step_counter import StepCounter

    counter = StepCounter()
    ```

2. Log daily steps and get weekly summaries:
    ```python
    counter.add_daily_steps("2024-09-01", 10000)
    total_steps = counter.get_weekly_steps()
    ```

3. Predict future step counts:
    ```python
    from auto_ml import predict_future_steps
    prediction = predict_future_steps(user_data)
    ```

## Branching Strategy

- **Main Branch**: Stable versions of the project.
- **Development Branch**: Ongoing work and feature integration.
- **Feature Branches**: New features such as daily goals or calories burned, merged back into `development` before being integrated into `main`.


