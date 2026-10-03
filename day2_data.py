import pandas as pd

# 1. Create a dictionary with sample data (like sensor readings over time)
data = {
    'Time': ['10:00', '10:01', '10:02', '10:03', '10:04'],
    'Temperature': [28.5, 29.1, 31.0, 30.5, 33.2],
    'Status': ['Normal', 'Normal', 'Warning', 'Normal', 'Alert']
}

# 2. Convert the dictionary into a Pandas DataFrame (a clean table)
df = pd.DataFrame(data)

print("--- Entire Dataset ---")
print(df)
print("\n")

# 3. Use Pandas built-in functions to analyze the data
print("--- Average Temperature ---")
avg_temp = df['Temperature'].mean()
print(f"{avg_temp}°C")

print("\n--- Filtered Rows (Where Status is Alert or Warning) ---")
high_risk = df[df['Status'] != 'Normal']
print(high_risk)