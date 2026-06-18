def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE NOT NULL,
        username TEXT,
        first_name TEXT,

        class TEXT,

        level INTEGER DEFAULT 1,
        xp INTEGER DEFAULT 0,
        gold INTEGER DEFAULT 100,

        title TEXT DEFAULT 'Wanderer',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
