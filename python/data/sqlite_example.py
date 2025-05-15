import sqlite3

def main():
    try:
        mydb = sqlite3.connect("sakila_master.db")
        cursor = mydb.cursor()

        cursor.execute("SELECT * from actor")

        for row in cursor.fetchall():
            print(row)

    except sqlite3.Error as err:
        print(f'Database error {err}')

    finally:
        if mydb:
            mydb.close()

if __name__ == "__main__":
    main()
