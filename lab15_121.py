
import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_record (
        Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        Subject_1 TEXT NOT NULL,
        Mark_1 INTEGER NOT NULL,
        Subject_2 TEXT NOT NULL,
        Mark_2 INTEGER NOT NULL,
        Subject_3 TEXT NOT NULL,
        Mark_3 INTEGER NOT NULL
    )
''')
conn.commit()

# Insert multiple student records
student_record = [
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'PWP', 95, 'DSC', 90, 'ICE', 93),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI', 'PWP', 85, 'DSC', 83, 'ICE', 80),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA', 'PWP', 90, 'DSC', 93, 'ICE', 89),
    (92301733046, 'SHIVAM ATULKUMAR BHATT', 'PWP', 93, 'DSC', 83, 'ICE', 89),
    (92301733058, 'DEVENDRASINH DOLATSINH JADEJA', 'PWP', 75, 'DSC', 80, 'ICE', 87)
]

cursor.executemany('''
    INSERT OR IGNORE INTO student_record
    (Enrollment, name, Subject_1, Mark_1, Subject_2, Mark_2, Subject_3, Mark_3)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', student_record)
conn.commit()

# Fetch all student records
cursor.execute('SELECT * FROM student_record')
rows = cursor.fetchall()
print("All Student Records:")
for row in rows:
    print(row)

# Fetch students with Mark_1 greater than 90
cursor.execute('SELECT name, Subject_1, Mark_1 FROM student_record WHERE Mark_1 > 90')
high_marks = cursor.fetchall()
print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Update Mark_1 for Ashutosh Kumar Singh in PWP
cursor.execute('''
    UPDATE student_record
    SET Mark_1 = 98
    WHERE name = 'ASHUTOSH KUMAR SINGH' AND Subject_1 = 'PWP'
''')
conn.commit()

# Verify the update
cursor.execute('SELECT name, Mark_1 FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")

# Delete a student record
cursor.execute('DELETE FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
conn.commit()

# Verify the deletion
cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
deleted_name = cursor.fetchone()
if deleted_name is None:
    print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")

# Calculate the average mark across all subjects for all students
cursor.execute('''
    SELECT AVG((Mark_1 + Mark_2 + Mark_3) / 3.0) FROM student_record
''')
avg_mark = cursor.fetchone()[0]
print(f"\nThe average mark of students is: {avg_mark:.2f}")

# Close the connection
conn.close()
