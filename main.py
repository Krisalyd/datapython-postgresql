"""
This module is responsible for creating a connection with the PostgreSQL database and insert data into it.
"""
import psycopg2

# 
connection = psycopg2.connect(user="postgres",
                              password="584510",
                              host="localhost",
                              port="5432",
                              database="postgres")
cursor = connection.cursor()


def connect():
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"Connected to {record}", "\n")

connect()

def insert():
    username = input("Username: ")
    user_password = input("Password: ")
    email = input("email: ")
    try:
        insert_query = """INSERT INTO user_data (USERNAME, USER_PASSWORD, EMAIL) VALUES (%s,%s,%s)"""
        to_insert = (username, user_password, email)
        cursor.execute(insert_query, to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Data inserted into user table.")

    except(Exception, psycopg2.Error) as error:
        if connection:
            print(f"Failed to insert data into user table. {error}")


option = 0

while option != "2":
    option = input("Choose one of the options: \n "
                   "1 - Sign up \n"
                   "2 - Exit program\n")
    if option == "1":
        insert()


if __name__ == '__main__':
    connect()
