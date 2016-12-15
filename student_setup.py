import sqlite3
conn= sqlite3.connect("my-app.db")

cursor = conn.cursor()

student_data = [ ("Leonardo", 16), ("Donatello", 16), ("Raphael", 16), ("Michaelangelo", 16)]

for t in student_data:
	format_str = """INSERT INTO students (name, age) VALUES ("{name}", "{age}");"""

	sql_command = format_str.format(name=t[0], age = t[1])
	cursor.execute(sql_command)
	
	
conn.commit()
conn.close()