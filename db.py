import sqlite3


class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_table(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                score INTEGER
            )
            """)
        conn.close()

    def get_score(self, user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            result = conn.execute(
                "SELECT score FROM users WHERE user_id = ?",
                (user_id,)
            ).fetchone()
        conn.close()

        if result:
            return result[0]
        return 0

    def add_point(self, user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("""
            INSERT INTO users (user_id, score)
            VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET score = score + 1
            """, (user_id,))
        conn.close()