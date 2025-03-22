import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Drop old_users table if it already exists
cursor.execute("DROP TABLE IF EXISTS old_users")

# Rename users table to old_users
cursor.execute("ALTER TABLE users RENAME TO old_users")

# Create a new users table with auto-incrementing ID
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")

# Insert only unique emails
cursor.execute("""
    INSERT INTO users (name, email, password)
    SELECT name, email, password FROM old_users
    WHERE rowid IN (SELECT MIN(rowid) FROM old_users GROUP BY email)
""")

# Drop the old_users table
cursor.execute("DROP TABLE old_users")

# Commit and close
conn.commit()
conn.close()

print("✅ Users table updated successfully! Duplicate emails removed.")
