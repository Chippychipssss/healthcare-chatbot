import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Check if the user already exists before inserting
cursor.execute("SELECT * FROM users WHERE id = ?", ('user4',))
existing_user = cursor.fetchone()

if not existing_user:
    new_user = ('user4', 'Alice Doe', 'alicedoe@example.com', 'mypassword')
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", new_user)
    conn.commit()
    print("\nNew user added successfully!")
else:
    print("\nUser already exists, skipping insertion.")

# Fetch and display all users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("\nUsers in Database:")
for user in users:
    print(user)

# Close connection
conn.close()
