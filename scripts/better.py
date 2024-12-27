import os, json

class Patient:
    #initialize
    def __init__(
            self, 
            name, #name + surname
            pesel, #pesel number
            dates, #dictionary of all dates ==> times ==> values
                 ):
        self.name = name
        self.pesel = pesel
        self.dates = dates
    def to_dictionary(self):
        return {
            "Name" : self.name,
            "Pesel" : self.pesel,
            "Dates" : self.dates,
        }
    
FILENAME = "press-group.csv"

with open(os.path.join("Assets", FILENAME)) as file:
    input_data = file.readlines()
    # input_data = []
    # for i in range(9):
    #     input_data.append(file.readline())

output = {}
to_json = {}
dates_dictionary = {}
times_dictionary = {}
single_dictionary = {}
first_done = False
date_read = False

for elem in input_data:
    if elem[0] == "#" and first_done:
        if name_surname not in output:
            dates_dictionary[date] = times_dictionary
            output[name_surname] = Patient(name_surname, pesel, dates_dictionary)
        else:
            output[name_surname].dates[date] = times_dictionary
        dates_dictionary = {}
        times_dictionary = {}
        single_dictionary = {}
    if elem[0] == "#":
        helper = elem.split()[1:]
        name_surname = helper[0] + " " + helper[1]
        pesel = helper[2]
    else:
        helper = elem.split()
        
        #creating variables and deleting used elements of helper
        date = helper[0]
        time = helper[1]
        pulse = helper[-1]
        helper = helper[2:-1]

        #helper variables declaration
        dst = 0
        sys = 0
        qty = 0

        #iterating through elements of pressure
        for elem in helper:
            qty += 1
            pressure = elem.split("/")
            dst += int(pressure[0])
            sys += int(pressure[1])
        
        #calculating average pressure values
        dst /= qty
        sys /= qty

        #if pulse exist add it, else use "NAN" value
        if len(pulse[1:]) > 0:
            pulse = int(pulse[1:]) 
        else:
            pulse = "NAN"

        single_dictionary["SYS"] = round(sys,1)
        single_dictionary["DST"] = round(dst,1)
        single_dictionary["Pulse"] = pulse
        if sys < 140 and dst < 90:
            single_dictionary["comment"] = "Przekroczono wartosc nominalna"
        times_dictionary[time] = single_dictionary
        single_dictionary = {}
        if not first_done:
            first_done = True

if name_surname not in output:
    dates_dictionary[date] = times_dictionary
    output[name_surname] = Patient(name_surname, pesel, dates_dictionary)
else:
    output[name_surname].dates[date] = times_dictionary

for key, value in output.items():
    to_json[key] = value.to_dictionary()

with open(os.path.join("Output", "score.json"), "w") as file:
    json.dump(to_json, file, indent=4)