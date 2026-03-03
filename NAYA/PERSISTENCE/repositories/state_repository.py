class StateRepository:

    def __init__(self, db_connection):
        self.conn = db_connection
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
        """)
        self.conn.commit()

    def save_state(self, key, value):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO system_state (key, value)
            VALUES (?, ?)
        """, (key, value))
        self.conn.commit()

    def get_state(self, key):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT value FROM system_state WHERE key = ?
        """, (key,))
        result = cursor.fetchone()
        return result[0] if result else None
