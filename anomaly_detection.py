import pandas as pd

# Load the processed data
file_path = r"C:\Users\Yawar\Detecting_Data_Breaches\data\processed_logs.csv"
logs = pd.read_csv(file_path)

# Preview the data
print(logs.head())

# Defining some basic rules to detect(flag) any suspicious activity
# Rule 1: Flag unusual login times
logs['unusual_time'] = logs['hour'].apply(lambda x: 1 if x < 5 or x > 23 else 0)

# Rule 2: Flag users with high daily activity
daily_activity = logs.groupby('user_id')['activity'].count()
logs['high_activity'] = logs['user_id'].apply(lambda x: 1 if daily_activity[x] > 100 else 0)

# Rule 3: Flag short time gaps
logs['short_gap'] = logs['time_diff'].apply(lambda x: 1 if x < 5 else 0)

# Display flagged anomalies
print(logs[['user_id', 'unusual_time', 'high_activity', 'short_gap']].head())

# Combining all the rules into a single anomaly score for every user.
# Calculate anomaly score
logs['anomaly_score'] = logs['unusual_time'] + logs['high_activity'] + logs['short_gap']

# Sort users by anomaly score
anomalies = logs.groupby('user_id')['anomaly_score'].sum().sort_values(ascending=False)
print(anomalies.head())
# saving flagged anomaly and scores
# Save flagged anomalies
output_path = r"C:\Users\Yawar\Detecting_Data_Breaches\data\anomalies.csv"
logs.to_csv(output_path, index=False)
print(f"Anomalies saved to {output_path}")


