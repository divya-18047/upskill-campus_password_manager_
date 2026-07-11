import sqlite3

# Connect to the database
conn = sqlite3.connect("passwords.db")

# Create a cursor
cursor = conn.cursor()

# Ask the user for the website
website = input("Enter website: ")

# Search the database
cursor.execute(
    "SELECT * FROM passwords WHERE website=?",
    (website,)
)

# Get the result
result = cursor.fetchall()

# Print the result
print(result)

# Close the database
conn.close()