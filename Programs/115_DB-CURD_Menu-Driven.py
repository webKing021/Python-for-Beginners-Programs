import mysql.connector
from mysql.connector import Error

ch = 9
while(ch != 8):
    print("::::::MENU::::::")
    print("1. Show Databases")
    print("2. Create Database")
    print("3. Create table")
    print("4. Insert Data")
    print("5. Update Data")
    print("6. Delete Data")
    print("7. Show Data")
    print("8. Exit")
    
    ch = int(input("Enter your choice: "))

    if (ch == 1):
        def show_databases():
            try:
                conn = mysql.connector.connect(
                    host = "127.0.0.1",
                    port = 3306,
                    user = "root",
                    password = "",
                    database = "mysql"
                )

                if conn.is_connected():
                    print("Connected to MySQL Database")

                    cursor = conn.cursor()
                    query = "show databases"
                    cursor.execute(query)
                    data = cursor.fetchall()

                    print("List of Databases:")
                    for i in data:
                        print(i[0])

                    cursor.close()
                    conn.commit()
                    conn.close()

            except Error as e:
                print("Error while connecting to MySQL", e)

        show_databases()

        if (ch == 2):
            def create_database():
                try:
                    conn = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = "root",
                        password = "",
                        database = "mysql"
                    )

                    if conn.is_connected():
                        print("Connected to MySQL Database")

                        cursor = conn.cursor()
                        query = "CREATE DATABASE employee"
                        cursor.execute(query)
                        print("Database created successfully")

                        conn.commit()
                        conn.close()

                except Error as e:
                    print("Error while connecting to MySQL", e)

            create_database()

        if (ch == 3):
            def create_table():
                try:
                    conn = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = "root",
                        password = "",
                        database = "mysql"
                    )

                    if conn.is_connected():
                        print("Connected to MySQL Database")

                        cursor = conn.cursor()
                        query = "CREATE TABLE employee (id INT PRIMARY KEY, name VARCHAR(50), age INT(2), salary INT(3))"
                        cursor.execute(query)
                        print("Table created successfully")

                        conn.commit()
                        conn.close()

                except Error as e:
                    print("Error while connecting to MySQL", e)

            create_table()
            
        if (ch == 4):
            def insert_data(id, name, age, salary):
                try:
                    conn = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = "root",
                        password = "",
                        database = "mysql"
                    )

                    if conn.is_connected():
                        print("Connected to MySQL Database")

                        cursor = conn.cursor()
                        query = "INSERT INTO employee (id, name, age, salary) VALUES (%s, %s, %s, %s)"
                        values = (id, name, age, salary)
                        cursor.execute(query, values)
                        print("Data inserted successfully")

                        conn.commit()
                        conn.close()

                except Error as e:
                    print("Error while connecting to MySQL", e)
            
            insert_data(1, "Krutarth", 21, 5000)

        if (ch == 5):
            def update_data(id, name, age, salary):
                try:
                    conn = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = "root",
                        password = "",
                        database = "mysql"
                    )

                    if conn.is_connected():
                        print("Connected to MySQL Database")

                        cursor = conn.cursor()
                        query = "UPDATE employee SET name = %s, age = %s, salary = %s WHERE id = %s"
                        values = (name, age, salary, id)
                        cursor.execute(query, values)
                        print("Data updated successfully")

                        conn.commit()
                        conn.close()

                except Error as e:
                    print("Error while connecting to MySQL", e)

            update_data(1, "Krutarth", 21, 5000)

        if (ch == 6):
            def delete_data(id):
                try:
                    conn = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = "root",
                        password = "",
                        database = "mysql"
                    )

                    if conn.is_connected():
                        print("Connected to MySQL Database")

                        cursor = conn.cursor()
                        query = "DELETE FROM employee WHERE id = %s"
                        values = (id,)
                        cursor.execute(query, values)
                        print("Data deleted successfully")

                        conn.commit()
                        conn.close()

                except Error as e:
                    print("Error while connecting to MySQL", e)

            delete_data(1)

        if (ch == 7):
            def show_data():
                try:
                    conn = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = "root",
                        password = "",
                        database = "mysql"
                    )

                    if conn.is_connected():
                        print("Connected to MySQL Database")

                        cursor = conn.cursor()
                        query = "SELECT * FROM employee"
                        cursor.execute(query)
                        data = cursor.fetchall()

                        print("List of Employees:")
                        for i in data:
                            print(i)

                        cursor.close()
                        conn.commit()
                        conn.close()

                except Error as e:
                    print("Error while connecting to MySQL", e)

            show_data()

        if (ch == 8):
            exit()

        else:
            print("Invalid choice")