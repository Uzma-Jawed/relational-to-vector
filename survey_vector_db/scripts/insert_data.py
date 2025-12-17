import sqlite3

conn = sqlite3.connect("data/survey.db")
cursor = conn.cursor()

# -----------------------
# QUESTION 1 — Binary
# -----------------------
cursor.execute("""
INSERT INTO questions (question_text, question_type, max_score)
VALUES (?, ?, ?)
""", ("Do you feel motivated at work?", "binary", 1))

q1_id = cursor.lastrowid

cursor.executemany("""
INSERT INTO answers (question_id, answer_text, binary_value, score)
VALUES (?, ?, ?, ?)
""", [
    (q1_id, "Yes, I feel motivated", 1, 1),
    (q1_id, "No, I do not feel motivated", 0, 0)
])

# -----------------------
# QUESTION 2 — True/False
# -----------------------
cursor.execute("""
INSERT INTO questions (question_text, question_type, max_score)
VALUES (?, ?, ?)
""", ("My manager supports my growth.", "true_false", 1))

q2_id = cursor.lastrowid

cursor.executemany("""
INSERT INTO answers (question_id, answer_text, binary_value, score)
VALUES (?, ?, ?, ?)
""", [
    (q2_id, "True", 1, 1),
    (q2_id, "False", 0, 0)
])

# -----------------------
# QUESTION 3 — Scoring
# -----------------------
cursor.execute("""
INSERT INTO questions (question_text, question_type, max_score)
VALUES (?, ?, ?)
""", ("Rate your work-life balance", "scale", 5))

q3_id = cursor.lastrowid

for i in range(1, 6):
    cursor.execute("""
    INSERT INTO answers (question_id, answer_text, binary_value, score)
    VALUES (?, ?, ?, ?)
    """, (q3_id, f"Rating {i}", None, i))

# Save
conn.commit()
conn.close()

print("✅ Sample questions & answers inserted")