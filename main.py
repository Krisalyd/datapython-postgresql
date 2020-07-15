"""
The main module is responsible for creating a connection with the PostgreSQL database and insert data into it.
"""
import psycopg2
import sys

# Configuring parameters for connection with the PostgreSQL server.

connection = psycopg2.connect(user="postgres",
                              password="584510",
                              host="localhost",
                              port="5432",
                              database="postgres")

# A cursor was created so i could be able to execute PostgreSQL commands through Python source code.
cursor = connection.cursor()


def connect():
    """
    connect() function is responsible for stablishing a connection with PostgreSQL server.
    """
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Get and print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"Connected to {record}", "\n")


connect()


def insert():
    """
    insert() function insert rows into the selected PostgreSQL table.
    In case of error while inserting data, this function will return an error message.
    """
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


option = 1

while option:
    print('\n Choose one of the options: \n '
          '1 - Sign up \n'
          '2 - Exit program \n')
    option = input()
    if option == "1":
        insert()
    elif option == "2":
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            sys.exit("Ending session...")
    else:
        print("Invalid option!\n")


if __name__ == '__main__':
    connect()
