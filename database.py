import sqlite3

DB_NAME = "tasks.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": r[0], "title": r[1], "completed": bool(r[2])}
        for r in rows
    ]


def add_task(title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()


def update_task(task_id, completed):
    if not isinstance(completed, bool):
        raise ValueError("completed must be boolean")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET completed=? WHERE id=?",
        (int(completed), task_id)
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
