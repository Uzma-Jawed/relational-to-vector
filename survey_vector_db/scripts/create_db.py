import sqlite3

# 1️⃣ Database connect (file creation)
conn = sqlite3.connect("data/survey.db")
cursor = conn.cursor()

# 2️⃣ Questions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    question_type TEXT,
    max_score INTEGER
)
""")

# 3️⃣ Answers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    answer_text TEXT,
    binary_value INTEGER,
    score INTEGER,
    FOREIGN KEY (question_id) REFERENCES questions(id)
)
""")

# 4️⃣ Save & close
conn.commit()
conn.close()

print("✅ Relational database & tables created")