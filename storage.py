import json
import os 
from itertools import islice



def set_initial_data(username):
    file_name = get_file_name(username)
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            data = {"run_history" : [], "pace_history" :[]}
            json.dump(data, f, indent=4)
        

def save_run_peak(username, age, heart_rate_peak, run_date):

    file_name = get_file_name(username)
    with open(file_name, "r") as f:
        data = json.load(f)  
    data["run_history"].append({"date": run_date, "peak_hr": heart_rate_peak, "age": age})

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def calculate_current_max_hr(username, age):
    current_max_hr = 208 - (0.7 * age)
    file_name = get_file_name(username)
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            data = json.load(f)
        reversed_iterator= reversed(data["run_history"])
        last_10_reversed = list(islice(reversed_iterator, 10))
    
        for hr_rate in last_10_reversed:
            if current_max_hr < hr_rate["peak_hr"]:
                current_max_hr = hr_rate["peak_hr"]

    return current_max_hr


def get_file_name(username):
    return "user_" + str(username) +".json"
if __name__ == "__main__":
    set_initial_data(25)
    save_run_peak(188, "2026-09-10")
    save_run_peak(192, "2026-09-12")
    save_run_peak(178, "2026-09-14")
    print(calculate_current_max_hr(25))



def save_pace_entry(username, run_date, target_zones, blocks):
    file_name = get_file_name(username)
    with open(file_name, "r") as f:
        data = json.load(f)  
    data["pace_history"].append({"date": run_date, "target_zones": target_zones, "blocks" : blocks})

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)






#"run_history" : [
#   {
#       "date" : "2026-09-14",
#       "peak_hr" : "190",
#       "age" : 25
#   }
# ]
#"pace_history": [
#    {
#        "date": "2026-09-14",
#        "target_zones": [
#            {"zone": 2, "until_minute": 20},
#            {"zone": 3, "until_minute": 40}
#        ],
#        "blocks": [
#            {"minute": 5, "zone": 2, "avg_pace": "9:30"},
#            {"minute": 10, "zone": 2, "avg_pace": "9:45"},
#            {"minute": 15, "zone": 3, "avg_pace": "8:20"},
#            {"minute": 20, "zone": 2, "avg_pace": "9:50"},
#            {"minute": 25, "zone": 3, "avg_pace": "8:40"}
#        ]
#    }
#]
