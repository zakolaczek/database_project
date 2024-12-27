import sqlite3, os
DATABASE_NAME = "patient.db"

INSERT_MORPHOLOGY = """
    INSERT INTO morphology VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

class Morphology:
    def __init__(self, date, time, person_id, wbc, rbc, hmg, hmk, plt, tot, hdl, ldl, glk):
        self.date = str(date)
        self.time = str(time)
        self.person_id = int(person_id)
        self.wbc = float(wbc)
        self.rbc = float(rbc)
        self.hmg = float(hmg)
        self.hmk = float(hmk)
        self.plt = float(plt)
        self.tot = float(tot)
        self.hdl = float(hdl)
        self.ldl = float(ldl)
        self.glk = float(glk)
    def to_list(self):
        return (self.date, self.time, self.person_id, self.wbc, self.rbc, self.hmg, self.hmk, self.plt, self.tot, self.hdl, self.ldl, self.glk)

with open(os.path.join("assets", "morph-group.csv"), "r") as file:
    data = file.readlines()
    data = data[1:]
morphologies = []
for elem in data:
    helper = elem.split()
    morphologies.append(Morphology(*helper))

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        for morphology in morphologies:
            cur.execute(INSERT_MORPHOLOGY, (*morphology.to_list(),))
        conn.commit()
    except Exception as ex:
        print(ex)