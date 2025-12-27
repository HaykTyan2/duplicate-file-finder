from src.scanner import scan_folder
from src.hasher import hash_all_files
from src.finder import find_duplicates
from src.organizer import move_duplicates, delete_duplicates
from src.database import init_db, save_files
from src.actions import show_logs
from pathlib import Path

def main():
    print("=== Duplicate File Finder ===")
    folder = input("Enter folder path to scan: ").strip()

    # 1. Scan folder
    files = scan_folder(folder)
    if not files:
        return

    # 2. Initialize DB
    init_db()
    
    # 3. Save file metadata
    save_files(files)

    # 4. Hash files
    hash_map = hash_all_files(files)

    # 5. Find duplicates
    duplicates = find_duplicates(hash_map)

    if not duplicates:
        print("No duplicates found!")
        return

    print("\nDuplicates found:")
    for h, paths in duplicates.items():
        print(f"\nHash: {h}")
        for p in paths:
            print(f"  - {p}")

    print("\nActions:")
    print("1. Move duplicates to 'Duplicates' folder")
    print("2. Delete duplicates")
    print("3. View action logs")
    print("4. Exit")

    choice = input("> ").strip()

    if choice == "1":
        move_duplicates(duplicates, Path(folder) / "Duplicates")
    elif choice == "2":
        delete_duplicates(duplicates)
    elif choice == "3":
        show_logs()
    else:
        print("Goodbye.")

if __name__ == "__main__":
    main()
