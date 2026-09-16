import storage
import heart_rate
import time

def main():
    user_age = user_age_prompt()
    username = user_name_prompt()
    storage.set_initial_data(username)
    max_hr = heart_rate.calculate_current_max_hr(user_age)
    target_zone = target_zone_prompt()
    
    while(running):
        current_hr = get_current_hr()
        curernt_zone = heart_rate.get_zone_status(current_hr, max_hr)
        if current_zone == "Slow":
            #send slow virbation
        if current_zone == "Fast":
            #send fast vibration
        if current_zone == "Danger":
            #send non stop vibration

        while pause_run:
            time.sleep(0.5)

        #user changes zone 
        if(zone_change):
            zones_data.Append({"zone": target_zone, "untilminute" : timer_from_watch})
            target_zone = new_zone


        #save pace every minute 
        if(timer_every_minute)
            minute_pace.Append(current_pace)

        #save pace info every five minutes #minute_pace.clear() if you want to clear or do or minute_pace[::5]
        if(timer_from_watch%5 == 0): ##what if it skips the 5x minute mark ?
            average_pace = sum(minute_pace[::5]) /5 
            pace_info.Append({"minute": timer_every_five, "zone": target_zone, "avg_pace": average_pace})

        if stop_run:
            zones_data.Append({"zone": target_zone, "untilminute" : timer_from_watch})
            running = False
        time.sleep(1)

    storage.save_pace_entry(username, run_date, zones_data, pace_info):
    storage.save_run_peak(username, user_age, heart_peak, run_date)
    




def target_zone_prompt():
    zone_not_given = True
    acceptable_Zone = [1,2,3,4,5]
    while zone_not_given:
        target_zone = input ("Heart Rate Zone (1-5): ")
        int_zone = try_parse_int(target_zone)
        if(int_zone is None or int_zone not in acceptable_zone):
            print("Invalid zone, Try again")

def user_age_prompt():
    age_not_given = True
    while age_not_given:
        user_age = input("Age: ")
        int_age = try_parse_int(user_age)
        if(int_age is None or int_age > 80 or int_age < 8):
            print("Invalid Age, Try again")
        else:
            age_not_given = False
    return int_age

def user_name_prompt():
        valid_name_not_given = True
    while valid_name_not_given:
        user_name = input("username (must be less than 5 letters): ")
        if len(user_name) > 5:
            print("Invalid name, Try again")
        else:
            valid_name_not_given = False
    return user_name

def try_parse_int(s, val=None):
  try:
    return int(s)
  except ValueError:
    return val