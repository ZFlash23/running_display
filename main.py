import storage
import heart_rate
import time

def main():
    user_age = user_age_prompt()
    storage.set_initial_data(user_age)
    max_hr = heart_rate.calculate_current_max_hr(user_age)
    zone_range = heart_rate.calculate_zones(max_hr)
    while(running):
        current_hr = get_current_hr()
        curernt_zone = heart_rate.get_zone_status(current_hr, max_hr)
        if current_zone == "Slow":
            #send slow virbation
        if current_zone == "Fast":
            #send fast vibration
        if current_zone == "Danger":
            #send non stop vibration

        time.sleep(1)
        while pause_run:
            time.sleep(0.5)
        if stop_run:
            running = False






def user_age_prompt():
    age_not_given = True
    while age_not_given:
        user_age = input("Age: ")
        int_age = try_parse_int(user_age)
        if int_age > 80 or int_age < 8:
            print("Invalid Age, Try again")
        else:
            age_not_given = False
    return int_age

def try_parse_int(s, val=None):
  try:
    return int(s)
  except ValueError:
    return val