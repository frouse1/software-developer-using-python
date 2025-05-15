import mysql.connector
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="mysql user name")
    parser.add_argument("password", help="mysql password")
    args = parser.parse_args()
    print(f'The username and password are {args.user} {args.password}')

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=args.user,
            password=args.password,
            database="sakila",
            auth_plugin="mysql_native_password"
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * from actor")
        for row in cursor.fetchall():
            print(row)

    # except mysql.connector.Error as err:
    except argparse.ArgumentTypeError as err:
        print(f'Database error {err}')
    except Exception as e:
        print(f'Unknown Database error {e}')

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
