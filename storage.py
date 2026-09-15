import json
import os 
from itertools import islice

file_name = "user_data.json"


def set_initial_data(age):
    
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            data = {"age": age, "run_history" : []}
            json.dump(data, f, indent=4)
        

def save_run_peak(heart_rate_peak, run_date):
    with open(file_name, "r") as f:
        data = json.load(f)
        
    data["run_history"].append({"date": run_date, "peak_hr": heart_rate_peak})

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def calculate_current_max_hr(age):
    current_max_hr = 208 - (0.7 * age)

    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            data = json.load(f)
        reversed_iterator= reversed(data["run_history"])
        last_10_reversed = list(islice(reversed_iterator, 10))
    
        for hr_rate in last_10_reversed:
            if current_max_hr < hr_rate["peak_hr"]:
                current_max_hr = hr_rate["peak_hr"]

    return current_max_hr

if __name__ == "__main__":
    set_initial_data(25)
    save_run_peak(188, "2026-09-10")
    save_run_peak(192, "2026-09-12")
    save_run_peak(178, "2026-09-14")
    print(calculate_current_max_hr(25))