import sqlite3
DATABASE_NAME = "patient.db"

AVG_PRESSURE = """
    SELECT
        pr.date,
        pr.time,
        pr.SYS, 
        pr.DST,
        pr.PULSE
    FROM pressure pr
    WHERE pr.person_id = ?
"""

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(AVG_PRESSURE, (71121302531,))
        records = cur.fetchall()
        for record in records:
            print(record)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

