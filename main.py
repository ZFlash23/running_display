import storage
import heart_rate
import time
import random
import keyboard

def main():
    user_age = user_age_prompt()
    username = user_name_prompt()
    storage.set_initial_data(username)
    max_hr = storage.calculate_current_max_hr(username, user_age)
    target_zone = target_zone_prompt()
    heart_peak = 0
    minute_pace = []
    zones_data = []
    pace_info = []
    #testing
    print("Max Heart Rate: ", max_hr)
    how_long = 60 * 5 #3 minutes
    timer_from_watch = time.perf_counter()
    last_added_min = 0
    last_added_five = 5
    running = True
    new_target_zone = 0

    while(time.perf_counter() - timer_from_watch < how_long and running):

        current_hr = random.randint(90, 190)  # Simulate getting current heart rate
        current_pace = random.uniform(4.0, 6.0)  # Simulate getting current pace
        current_zone = heart_rate.get_zone_status(current_hr, max_hr)
        if current_zone == "Slow":
            #send slow virbation
            print("speed up your pace, your current heart rate is " + str(current_hr))
        if current_zone == "Fast":
            #send fast vibration
            print("too fast, go slower, your current heart rate is " + str(current_hr))
        if current_zone == "Danger":
            #send non stop vibration
            print("DANGER, slow down, your current heart rate is " + str(current_hr))




        if(current_hr > heart_peak):
            heart_peak = current_hr
        time.sleep(1)

        #pause for testing 
        if keyboard.is_pressed('p'):
            print("paused, press r to resume")
            timer_paused = time.perf_counter()
            while(not keyboard.is_pressed('r')):
                time.sleep(0.5)
            timer_from_watch += time.perf_counter() - timer_paused # take account pausing
            

        #user changes zone for testing 
        if keyboard.is_pressed('z'): #zone change
            timer_paused = time.perf_counter()
            new_target_zone = target_zone_prompt()
            if(new_target_zone != target_zone):
                target_zone = new_target_zone
                zones_data.append({"zone": target_zone, "untilminute" : (time.perf_counter() - timer_from_watch)/60})
                
            timer_from_watch +=  time.perf_counter() - timer_paused # take account pausing


        timer_in_minute = (time.perf_counter() - timer_from_watch)/60

        #testing values
        print("timer in minute: " + str(timer_in_minute) + " current pace: " +
            str(current_pace) + " current heart rate: " + str(current_hr) + 
            " target zone: " + str(target_zone))
        
        #save pace every minute 
        if (timer_in_minute % 1 > 0.9 and last_added_min == int(timer_in_minute)): #every minute
            minute_pace.append(current_pace)
            last_added_min += 1
            print (str(timer_in_minute/60) + "is the minute, pace is " + str(current_pace))

        #save pace info every five minutes #minute_pace.clear() if you want to clear or do or minute_pace[::5]
        timer_every_five = int(timer_in_minute) % 5
        if(timer_every_five == 0 and timer_in_minute%5 > 0.9 
           and last_added_five == int(timer_in_minute)): ##what if it skips the 5x minute mark ?
            average_pace = sum(minute_pace[::5]) /5 
            pace_info.append({"minute": timer_every_five, "zone": target_zone, "avg_pace": average_pace})
            last_added_five+=5
            print (str(timer_in_minute) + "is the five minute mark")

        #stopping for testing
        if keyboard.is_pressed('q'): #stopping
            zones_data.append({"zone": target_zone, "untilminute" : (time.perf_counter() - timer_from_watch)/60})
            print("stopping, saving data")
            running = False
        time.sleep(1)

    storage.save_pace_entry(username, "17/09/2026", zones_data, pace_info)
    storage.save_run_peak(username, user_age, heart_peak, "17/09/2026")

def target_zone_prompt():
    zone_not_given = True
    acceptable_zone = [1,2,3,4,5]
    while zone_not_given:
        target_zone = input ("Heart Rate Zone (1-5): ")
        int_zone = try_parse_int(target_zone)
        if(int_zone is None or int_zone not in acceptable_zone):
            print("Invalid zone, Try again")
        else:
            zone_not_given = False
    return int_zone

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

if __name__ == "__main__": 
    main()