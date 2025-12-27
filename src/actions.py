from src.database import insert_log, fetch_logs

def log_move(src, dest):
    insert_log(f"MOVED: {src} -> {dest}")

def log_delete(path):
    insert_log(f"DELETED: {path}")

def show_logs():
    logs = fetch_logs()
    print("\n--- Action History ---")
    for ts, action in logs:
        print(f"{ts} - {action}")
    print("----------------------\n")
