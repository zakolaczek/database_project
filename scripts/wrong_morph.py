import sqlite3,os

def is_in_range(number, ranger):
    r1 = float(ranger[0])
    r2 = float(ranger[1])
    return number >= r1 and number <= r2
def checker(values, perfect):
    values = values[3:]
    i = 0
    for value in values:
        if not is_in_range(value, perfect[i]):
            return True #prints that score is not good
        i += 1
    return False #everything is good


DATABASE_NAME = "patient.db"

AVG_PRESSURE = """
    SELECT
        p.name,
        p.surname,
        p.phone,
        AVG(m.WBC),
        AVG(m.RBC),
        AVG(m.HMG),
        AVG(m.HMK),
        AVG(m.PLT),
        AVG(m.TOT),
        AVG(m.HDL),
        AVG(m.LDL),
        AVG(m.GLK)
    FROM
        person p,
        morphology m
    WHERE p.pesel = m.person_id
    GROUP BY p.pesel
"""

if __name__ == "__main__":
    with open(os.path.join("assets", "morfologia-parametry-dane.csv"), "r") as file:
        data = file.readlines()
        data = data[2:]
        data = [x.split()[1:4] for x in data]
    values = []
    for elem in data:
        values.append((elem[1], elem[2]))  
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(AVG_PRESSURE)
        records = cur.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

    for record in records:
        if checker(record, values):
            print(record[:3])