import sqlite3

conn = sqlite3.connect("data/survey.db")
cursor = conn.cursor()

cursor.execute("""
SELECT q.question_text, a.answer_text, a.binary_value, a.score
FROM questions q
JOIN answers a ON q.id = a.question_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()