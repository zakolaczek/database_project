import sqlite3,os
DATABASE_NAME = "patient.db"

INSERT_PERSON = """
    INSERT INTO person VALUES (NULL, ?, ?, ?, ?)
"""

class Patient:
    def __init__(self, name, surname, pesel, phone):
        self.name = str(name)
        self.surname = str(surname)
        self.pesel = int(pesel)
        self.phone = int(phone)
    def to_list(self):
        return (self.name, self.surname, self.pesel, self.phone)   
    
patiens = []
with open(os.path.join("assets", "pacjenci-dane.csv"), "r") as file:
    data = file.readlines()

data = data[2:]
for elem in data:
    helper = elem.split()[1:]
    patiens.append(Patient(*helper))

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        for patient in patiens:
            cur.execute(INSERT_PERSON, (*patient.to_list(),))
        conn.commit()
    except Exception as ex:
        print(ex)