import sqlite3
from pathlib import Path
import datetime

DB_PATH = Path("file_organizer.db")

def init_db():
  # connect to the database (creates it if it doesn't exist)
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS files (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          path TEXT UNIQUE,
          name TEXT,
          extension TEXT,
          size INTEGER,
          modified TEXT
      )
  """)

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS actions (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          timestamp TEXT,
          action TEXT
      )
  """)

  conn.commit()
  conn.close()


def save_files(files_found):
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()
  
  for file_path in files_found:
    stat = file_path.stat()
    cursor.execute("""
      INSERT OR IGNORE INTO files (path, name, extension, size, modified) VALUES (?, ?, ?, ?, ?)""",
    (
      str(file_path),
      file_path.name,
      file_path.suffix.lower(),
      stat.st_size,
      datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
    ))
  conn.commit()
  conn.close()

def insert_log(action: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO actions (timestamp, action) VALUES (datetime('now', 'localtime'), ?)",
        (action,)
    )
    conn.commit()
    conn.close()


def fetch_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, action FROM actions ORDER BY id DESC")
    logs = cursor.fetchall()
    conn.close()
    return logs
