def calculate_max_hr(age):
    return 208 - (0.7 * age)

def calculate_zones(age):
    max_hr  =  calculate_max_hr(age)
    return{
        "zone1": (0.50 * max_hr, 0.60 * max_hr),
        "zone2": (0.60 * max_hr, 0.70 * max_hr),
        "zone3": (0.70 * max_hr, 0.80 * max_hr),
        "zone4": (0.80 * max_hr, 0.90 * max_hr),
        "zone5": (0.90 * max_hr,  max_hr),
    }

def get_zone_status (heart_rate, age):

    zone_range = calculate_zones(age)
    if heart_rate < zone_range["zone1"][1] :
        return "Too Slow"
    elif heart_rate <= zone_range["zone2"][1] :
        return "Perfect"
    elif heart_rate < zone_range["zone3"][1] :
        return "Getting a little too high"
    else:
        return "DANGER"

if __name__ == "__main__":
    age = 25
    print(calculate_zones(age))
    print(get_zone_status(180, age))
    print(get_zone_status(120, age))
    print(get_zone_status(150, age))