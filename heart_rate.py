
def calculate_zones(max_hr):
    return{
        "zone1": (0.50 * max_hr, 0.60 * max_hr),
        "zone2": (0.60 * max_hr, 0.70 * max_hr),
        "zone3": (0.70 * max_hr, 0.80 * max_hr),
        "zone4": (0.80 * max_hr, 0.90 * max_hr),
        "zone5": (0.90 * max_hr,  max_hr),
    }

def get_zone_status (heart_rate, max_hr):

    zone_range = calculate_zones(max_hr)
    if heart_rate < zone_range["zone1"][1] :
        return "Slow"
    elif heart_rate <= zone_range["zone2"][1] :
        return "Perfect"
    elif heart_rate < zone_range["zone3"][1] :
        return "Fast"
    else:
        return "Danger"

if __name__ == "__main__":
    max_hr = 192
    print(calculate_zones(max_hr))
    print(get_zone_status(180, max_hr))
    print(get_zone_status(120, max_hr))
    print(get_zone_status(150, max_hr))