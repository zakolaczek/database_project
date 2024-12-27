import sqlite3
DATABASE_NAME = "patient.db"

AVG_PRESSURE = """
    SELECT
        p.name,
        p.surname,
        p.phone,
        AVG(pr.DST),
        AVG(pr.SYS)
    FROM
        person p,
        pressure pr
    WHERE p.pesel = pr.person_id
    GROUP BY p.pesel
"""

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(AVG_PRESSURE)
        records = cur.fetchall()
        for record in records:
            if record[-1] > 139 or record[-2] > 89:
                print(record[:3])
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

