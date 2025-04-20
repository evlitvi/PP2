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

#searching by pattern
def search_user_by_pattern():
    string = input("Enter patern to search: ")
    pattern = f"%{string}%"
    query = "SELECT * FROM Users WHERE user_name ILIKE %s OR user_phone ILIKE %s"
    cur.execute(query, (pattern, pattern))
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

#searching by pattern procedure
# CREATE OR REPLACE FUNCTION search_users_by_pattern(p_pattern TEXT)
# RETURNS TABLE (
#     user_id INT,
#     user_name VARCHAR,
#     user_phone VARCHAR
# )
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     RETURN QUERY
#     SELECT *
#     FROM Users
#     WHERE user_name ILIKE '%' || p_pattern || '%'
#        OR user_phone ILIKE '%' || p_pattern || '%';
# END;
# $$;
def search_users_by_pattern_sql():
    pattern = input("Enter patern to search: ")
    cur.execute("SELECT * FROM search_users_by_pattern(%s);", (pattern,))
    results = cur.fetchall()

    if results:
        print("\nResults:")
        for row in results:
            print(row)
    else:
        print("Null")

#insert or update user procedure
# CREATE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     IF EXISTS (SELECT 1 FROM Users WHERE user_name = p_name) THEN
#         UPDATE Users SET user_phone = p_phone WHERE user_name = p_name;
#     ELSE
#         INSERT INTO Users (user_name, user_phone) VALUES (p_name, p_phone);
#     END IF;
# END;
# $$;
def insert_or_update_user_procedure(name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()

#delete by name or phone procedure
# CREATE OR REPLACE PROCEDURE delete_user_by_name(p_user_name VARCHAR)
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     DELETE FROM Users WHERE user_name = p_user_name;
# END;
# $$;

# CREATE PROCEDURE delete_user_by_phone(p_user_phone VARCHAR(12))
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     DELETE FROM Users WHERE user_phone = p_user_phone;
# END;
# $$;
def delete_procedure():
    print("Delete user by: \n1. Name \n2. Phone")
    choice = int(input())
    if choice == 1:
        name = input("Enter user name: ")
        cur.execute("SELECT * FROM Users WHERE user_name = %s", (name,))
        if cur.fetchone():
            cur.execute("CALL delete_user_by_name(%s);", (name,))
        else:
            print("User does not exist")
    elif choice == 2:
        phone = input("Enter user phone: ")
        cur.execute("SELECT * FROM Users WHERE user_phone = %s", (phone,))
        if cur.fetchone():
            cur.execute("CALL delete_user_by_phone(%s);", (phone,))
        else:
            print("User does not exist")
    else:
        print("Wrong choice. Please, try again")


# insert_from_csv("contacts.csv")
# insert_from_console()
# update_user()
# search_user()
# delete_user()
insert_or_update_user_procedure("Yevgeniya", "+77475623342")

cur.close()
conn.close()