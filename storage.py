import json

file_name = "user_data.json"

def set_initial_data():
    

    with open(file_name, "w") as f:
        json.dump({}, f, indent=4)

def save_run_peak(heart_rate_peak):
    with open(file_name, "r") as f:
        data = json.load(f)
        
    data["Latest_heart_rate_peak"] = heart_rate_peak

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def calculate_current_max_hr(age):
    current_max_hr = 208 - (0.7 * age)
 
    # Reading
    with open(file_name, "r") as f:
        data = json.load(f)
    for rate in range(len(data), len(data)-10, -1):
        if data["Latest_heart_rate_peak"] > current_max_hr:
            current_max_hr = data["Latest_heart_rate_peak"]

    return current_max_hr
