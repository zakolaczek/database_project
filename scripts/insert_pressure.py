import sqlite3, os
DATABASE_NAME = "patient.db"

INSERT_PRESSURE = """
    INSERT INTO pressure VALUES (NULL, ?, ?, ?, ?, ?, ?)
"""

class Pressure:
    def __init__(self, pesel, date, time, sys, dst, pulse):
        self.pesel = int(pesel)
        self.date = str(date)
        self.time = str(time)
        self.sys = float(sys)
        self.dst = float(dst)
        self.pulse = int(pulse)
    def to_list(self):
        return (self.pesel, self.date, self.time, self.dst, self.sys, self.pulse)

with open(os.path.join("assets", "press-group.csv"), "r") as file:
    data = file.readlines()

pressures = []
for elem in data:
    helper = elem.split()
    if elem[0] == "#":
        pesel = helper[3]
    else:
        date = helper[0]
        time = helper[1]
        pulse = helper[-1][1:]
        helper = helper[2:-1]
        sys = 0
        dst = 0
        for value in helper:
            dst += int(value.split("/")[0])
            sys += int(value.split("/")[1])
        sys = round(sys/len(helper),2)
        dst = round(dst/len(helper), 2)
        pressures.append(Pressure(pesel, date, time, sys, dst, pulse))

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        for pressure in pressures:
            cur.execute(INSERT_PRESSURE, (*pressure.to_list(),))
        conn.commit()
    except Exception as ex:
        print(ex)