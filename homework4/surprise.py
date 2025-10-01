# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47' 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24' 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42' 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12' 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15' 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name(dict):
    for i in dict.keys():
        print(i)

name(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_type(dict):
    for i in dict.keys():
        print(i, dict[i]["Spectral Type"])

name_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def targets_mag(dict):
    for i in dict.keys():
        if dict[i]["Magnitude"] > 0.1:
            print(i)
targets_mag(targets)
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Alioth"] = {
    "RA": "12h 54m 1.750s",
    "Dec": "55° 57' 35″",
    "Magnitude": 1.8,
    "Spectral Type": "A1III-IVpkB9"
}
print(targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# before running the main function I have to write a supplementary function which takes the declination and converts it inot a number
def declination_fix(dict):
    declination = {}
    number = 0
    for i in dict.keys():
        for j in dict[i]['Dec']:
            if j.isdigit() == False:
                dict[i]["Dec"] = dict[i]["Dec"].replace(j, '')
        number = float(dict[i]["Dec"][0:2]) + float(dict[i]["Dec"][2:4])/60 + float(dict[i]["Dec"][4:6])/3600
        declination[i] = number
        number = 0
    return declination

def best_star(dict):
    declination = declination_fix(dict)
    best_star = None
    min_declination = 20
    min_magnitude = 0
    for i in dict.keys():
        dec_diff = abs(declination[i] - 20)
        mag_star = dict[i]['Magnitude']
        if dec_diff < min_declination or (dec_diff == min_declination and mag_star > min_magnitude):
            best_star = i
    return best_star

# for these two fucntios I ran into plenty of error mostly in data type issues and syntax errors so by fixing those thigns my code worked 
        
print(best_star(targets))   

# 6) What is your favorite constellation?
#Ursa Major
# print(targets[0])