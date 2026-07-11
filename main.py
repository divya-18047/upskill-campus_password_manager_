import sqlite3

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

website = input("Website: ")
username = input("Username: ")
password = input("Password: ")

cursor.execute(
    "INSERT INTO passwords(website, username, password) VALUES (?, ?, ?)",
    (website, username, password)
)

conn.commit()
conn.close()

print("Password Saved Successfully!")