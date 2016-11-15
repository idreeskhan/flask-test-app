import sqlite3
import logging

# This file is used in lieu of database migrations to keep the concepts simplified

logging.info('Creating SQLite db file')
conn = sqlite3.connect('my-app.db')

logging.info('Creating SQLite db')
conn.execute('''CREATE TABLE IF NOT EXISTS teachers(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  name TEXT NOT NULL,
                  age INTEGER)''')

logging.info('Creating tables and indices')
conn.execute('''CREATE TABLE IF NOT EXISTS teachers(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  name TEXT NOT NULL,
                  age INTEGER)''')
conn.execute('''CREATE TABLE IF NOT EXISTS students(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  name TEXT NOT NULL,
                  age INTEGER)''')
conn.execute('''CREATE TABLE IF NOT EXISTS courses(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  code TEXT NOT NULL,
                  department TEXT NOT NULL)''')
conn.execute('''CREATE TABLE IF NOT EXISTS student_course_mapping(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  student_id INTEGER NOT NULL,
                  course_id INTEGER NOT NULL,
                  grade REAL NOT NULL,
                  FOREIGN KEY(student_id) REFERENCES students(id),
                  FOREIGN KEY(course_id) REFERENCES courses(id))''')
conn.execute('''CREATE TABLE IF NOT EXISTS teacher_course_mapping(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  teacher_id INTEGER NOT NULL,
                  course_id INTEGER NOT NULL,
                  FOREIGN KEY(teacher_id) REFERENCES teachers(id),
                  FOREIGN KEY(course_id) REFERENCES courses(id))''')

conn.execute('''CREATE INDEX IF NOT EXISTS teachers_id_idx ON teachers(id)''')
conn.execute('''CREATE INDEX IF NOT EXISTS students_id_idx ON students(id)''')
conn.execute('''CREATE INDEX IF NOT EXISTS courses_id_idx ON courses(id)''')
conn.execute('''CREATE INDEX IF NOT EXISTS student_course_mapping_id_idx ON student_course_mapping(id)''')
conn.execute('''CREATE INDEX IF NOT EXISTS teacher_course_mapping_id_idx ON teacher_course_mapping(id)''')

conn.commit()
conn.close()





