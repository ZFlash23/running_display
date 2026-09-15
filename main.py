import storage
import heart_rate
import time
import random

def main():
    user_age = user_age_prompt()
    storage.set_initial_data(user_age)
    max_hr = storage.calculate_current_max_hr(user_age)
    heart_peak = 0
    #testing
    print("Max Heart Rate: ", max_hr)

    start = time.time()
    while(time.time() - start < 20):

        current_hr = random.randint(90, 190)  # Simulate getting current heart rate
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
        #while pause_run:
           # time.sleep(0.5)
       # if stop_run:
            #running = False
    #add run data to storage
    storage.save_run_peak(heart_peak, "15/09/2026")


def user_age_prompt():
    age_not_given = True
    while age_not_given:
        user_age = input("Age: ")
        int_age = try_parse_int(user_age)
        if(int_age is None):
            print("Invalid Age, Try again")

        elif int_age > 80 or int_age < 8:
            print("Invalid Age, Try again")
        else:
            age_not_given = False
    return int_age

def try_parse_int(s, val=None):
  try:
    return int(s)
  except ValueError:
    return val

if __name__ == "__main__": 
    main()