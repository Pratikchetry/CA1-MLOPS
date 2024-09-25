import pandas as pd

class StepCounter:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Date', 'Steps', 'Calories_Burned'])

    def add_daily_steps(self, date, steps, calories_burned):
        # Use concat to add a new row to the DataFrame
        new_row = pd.DataFrame({
            'Date': [date], 
            'Steps': [steps], 
            'Calories_Burned': [calories_burned]
        })
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def total_weekly_steps(self):
        # Assuming 7 rows of data for a week
        weekly_data = self.data.tail(7)
        return weekly_data['Steps'].sum()

    def average_daily_steps(self):
        return self.data['Steps'].mean()

    def activity_level(self):
        avg_steps = self.average_daily_steps()
        if avg_steps < 5000:
            return "Low"
        elif avg_steps < 10000:
            return "Moderate"
        else:
            return "High"

# Sample Usage
if __name__ == "__main__":
    step_counter = StepCounter()
    step_counter.add_daily_steps('2024-09-01', 8000, 250)
    step_counter.add_daily_steps('2024-09-02', 9500, 280)
    print("Total Weekly Steps:", step_counter.total_weekly_steps())
    print("Average Daily Steps:", step_counter.average_daily_steps())
    print("Activity Level:", step_counter.activity_level())
