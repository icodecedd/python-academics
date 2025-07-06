import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

with sql.connect("students.db") as conn:
    df = pd.read_sql('select * from stud_course', conn)
    print(df)

print()

conn = sql.connect("students.db")

bsit = 0
bscs = 0
bsis = 0

cursor = conn.cursor()
cursor.execute('select * from stud_course')
for record in cursor:
    if record[2] == 'BSIT':
        bsit += 1
    elif record[2] == 'BSCS':
        bscs += 1
    else:
        bsis += 1

male = 0
female = 0

for record in cursor:
    if record[3] == 'Male':
        male += 1
    else:
        female +=1

stud_df = pd.read_sql('select * from stud_course', conn)
colors = ['b', 'r']

plt.xlabel = 'Number of Students Per Course'
plt.ylabel = 'Course'

y = stud_df.course

plt.pie(y, colors=colors,
      startangle=90, shadow = True, explode = (0, 0, 0, 0, 0, 0, 0, 0, 0),
      radius = 1.2, autopct = '%1.1f%%')

plt.legend()

plt.title('Student Grades')

plt.show()


