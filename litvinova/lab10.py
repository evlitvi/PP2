import psycopg2
import csv

conn = psycopg2.connect(
    dbname="PhoneBook",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

#inserting user info from csv 
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue
            cur.execute(
                "INSERT INTO Users (user_name, user_phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()

#inserting user info from console
def insert_from_console():
    name = input("Enter user name: ")
    phone = input("Enter user phone: ")
    cur.execute(
        "INSERT INTO Users (user_name, user_phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()

#updating user info
def update_user():
    id = input("Enter user id: ")

    cur.execute("SELECT * FROM Users WHERE user_id = %s", (id,))
    if not cur.fetchone():
        print(f"No user found with id {id}.")
        return
    
    name = input("Enter new user name (or click 'Enter' to skip): ")
    phone = input("Enter new user phone (or click 'Enter' to skip): ")
    if name:
        cur.execute("UPDATE Users SET user_name = %s WHERE user_id = %s", (name, id))
        print(f"User with id {id} was updated.")
    if phone:
        cur.execute("UPDATE Users SET user_phone = %s WHERE user_id = %s", (phone, id))
        print(f"User with id {id} was updated.")
    conn.commit()

#searching user by filter
def search_user():
    print("Enter filter or click 'Enter' to skip")
    name_filter = input("Enter name or part: ").strip()
    phone_filter = input("Enter phone or part: ").strip()
    query = "SELECT * FROM Users WHERE TRUE"
    params = []

    if name_filter:
        query += " AND user_name ILIKE %s"
        params.append(f"%{name_filter}%")
    if phone_filter:
        query += " AND user_phone ILIKE %s"
        params.append(f"%{phone_filter}%")

    cur.execute(query, params)
    rows = cur.fetchall()

    if rows:
        print("\nResults:")
        for row in rows:
            print(f"user_id: {row[0]}, user_name: {row[1]}, user_phone: {row[2]}")
    else:
        print("Null")

#deleting users by filter
def delete_user():
    print("Delete user by: \n1. id \n2. name \n3. phone: ")
    choice = int(input())

    if choice==1:
        id = input("Enter id: ")
        cur.execute("SELECT * FROM Users WHERE user_id = %s", (id,))
        if cur.fetchone():
            cur.execute("DELETE FROM Users WHERE user_id = %s", (id,))
            conn.commit()
            print(f"User with id {id} was deleted.")
        else:
            print(f"No user found with id {id}.")

    elif choice==2:
        name = input("Enter name: ")
        cur.execute("SELECT * FROM Users WHERE user_name = %s", (name,))
        if cur.fetchone():
            cur.execute("DELETE FROM Users WHERE user_name = %s", (name,))
            conn.commit()
            print(f"User with name {name} was deleted.")
        else:
            print(f"No user found with name {name}.")

    elif choice==3:
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM Users WHERE user_phone = %s", (phone,))
        if cur.fetchone():
            cur.execute("DELETE FROM Users WHERE user_phone = %s", (phone,))
            conn.commit()
            print(f"User with phone {phone} was deleted.")
        else:
            print(f"No user found with phone {phone}.")
    else:
        print("Wrong choice. Please try again")



insert_from_csv("contacts.csv")
insert_from_console()
update_user()
search_user()
delete_user()