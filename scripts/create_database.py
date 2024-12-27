#import necessary libraries
import sqlite3
DATABASE_NAME = "patient.db"


PERSONAL_DATA = """
    CREATE TABLE person(
        id      INTEGER NOT NULL PRIMARY KEY,
        name    TEXT NOT NULL,
        surname TEXT NOT NULL,
        pesel   INTEGER NOT NULL UNIQUE,
        phone   INTEGER NOT NULL UNIQUE
    )
"""
MORPHOLOGY = """
    CREATE TABLE morphology(
        id INTEGER NOT NULL PRIMARY KEY,
        person_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        WBC REAL NOT NULL,
        RBC REAL NOT NULL,
        HMG REAL NOT NULL,
        HMK REAL NOT NULL,
        PLT REAL NOT NULL,
        TOT REAL NOT NULL,
        HDL REAL NOT NULL,
        LDL REAL NOT NULL,
        GLK REAL NOT NULL
    )
"""

PRESSURE = """
    CREATE TABLE pressure(
        id INTEGER NOT NULL PRIMARY KEY,
        person_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        DST REAL NOT NULL,
        SYS REAL NOT NULL,
        PULSE INTEGER NOT NULL
    )
"""

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()

        try:
            cur.execute(PERSONAL_DATA)
            conn.commit()
        except Exception as ex:
            print(ex)

        try:
            cur.execute(MORPHOLOGY)
            conn.commit()
        except Exception as ex:
            print(ex)

        try:
            cur.execute(PRESSURE)
            conn.commit()
        except Exception as ex:
            print(ex)

    except Exception as ex:
        print(ex)
    finally:
        conn.close()