import pandas as pd
import random
from datetime import datetime, timedelta

# Simulation of log data of USERs
def generate_logs(num_records=1000):
    user_ids = [f"user_{i}" for i in range(1, 101)]  # 100 unique users
    activities = ["login", "file_upload", "password_reset"]
    locations = ["New Delhi", "Mumbai", "Bangalore", "Pune", "Hyderabad"]
    statuses = ["success", "failed"]

    data = []
    for i in range(num_records):
        timestamp = datetime.now() - timedelta(days=random.randint(0, 30)) - timedelta(hours=random.randint(0, 23))
        user_id = random.choice(user_ids)
        activity = random.choice(activities)
        location = random.choice(locations)
        status = random.choice(statuses)
        data.append([timestamp, user_id, activity, location, status])

    columns = ["timestamp", "user_id", "activity", "location", "status"]
    return pd.DataFrame(data, columns=columns)

# Generate and save logs
logs = generate_logs(1000)
logs.to_csv(r"C:\Users\Yawar\Detecting_Data_Breaches\data\examples.csv", index=False)
print("Simulated logs has saved to data/examples/simulated_logs.csv")
