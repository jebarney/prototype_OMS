import sqlite3

# New user
username = 't2s'
password = 't2s'

# Query the database
with sqlite3.connect("store.db") as db:
    cur = db.cursor()

# Change user
update_user = "UPDATE employee SET emp_id = ?, password = ?"
cur.execute(update_user, [username, password])
db.commit()

# Print results
view_user = cur.execute("SELECT * FROM employee")
results = view_user.fetchall()
print(results)