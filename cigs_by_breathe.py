
#22 ug/m^3 PM2.5 = 1 cig/day

import sys
import math

def analyze_air(concentration):
    if(concentration > 0):
        cigs_per_day = concentration / pm25
        cigs_per_hour = round(cigs_per_day / 24.0, 2)
        hours_per_cig = round(1.0 / cigs_per_hour, 2)
        time_per_cig = ""

        frac, whole = math.modf(hours_per_cig)
        time_per_cig += str(int(whole)) + " hours"
        if frac > 0.0:
            minutes_and_seconds = frac * 60  # convert to minutes

            frac, whole = math.modf(minutes_and_seconds)
            time_per_cig += " " + str(int(whole)) + " minutes"
            if frac > 0.0: # there are seconds
                seconds = round(60*frac)
                if seconds:
                    time_per_cig += " and " + str(seconds) + " seconds"

        if(concentration > 10000):
            print("RIP you")
        else:
            print(cigs_per_hour, "cigs per hour by breathing")
            print(f"1 cig every {time_per_cig}")
    else:
        print("No it's not lmao.")

if len(sys.argv) == 2:
    pm25 = 22.0  # 1 cig per day
    err = False
    try:
        concentration = float(sys.argv[1])  # PM2.5 concentration in the air
    except:
        print("Wtf man, give me your AQI")
        err = True
    analyze_air(concentration)
else:
    print("Get your cigs by calling me with your air AQI like 'python cigs_by_breathing.py 134'")