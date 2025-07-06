import sqlite3 as sql

def main():
    conn = sql.connect("lesson10.db")
    conn.execute("INSERT INTO student VALUES ('Ced', 'Drake')")
    cursor = conn.cursor()
    conn.commit()
    print("executed successfully!")

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    for row in rows:
        print("First Name: " + row[0])
        print("Last Name: " + row[1])
if __name__ == '__main__':
    main()
