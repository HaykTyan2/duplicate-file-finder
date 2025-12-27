## duplicate-file-finder

A Python-based tool that scans a user-selected folder, identifies duplicate files using file hashing, and provides options to organize or remove duplicates safely.

This project was built as a learning exercise to understand filesystem traversal, hashing, basic databases, and modular Python project structure.

--------------------------------------------------

## What this project does

The program scans a folder on your system and identifies duplicate files based on their contents, not just their filenames.

It allows the user to:

- Recursively scan a folder for files
- Detect duplicate files using hash comparison
- View detected duplicates grouped by hash
- Move duplicate files into a separate folder
- Permanently delete duplicate files
- View a log of file actions taken

--------------------------------------------------

## How it works (high level)

1. The user provides a folder path to scan.
2. The folder is recursively scanned for files.
3. File metadata is stored in a local SQLite database.
4. Each file is hashed using a checksum algorithm.
5. Files with matching hashes are identified as duplicates.
6. The user chooses an action:
   - Move duplicates to a separate folder
   - Delete duplicates
   - View previous action logs
7. All file operations are logged for reference.

--------------------------------------------------

## Project structure
```
duplicate-file-finder/
├── src/
│   ├── scanner.py     # Scans folders recursively
│   ├── hasher.py      # Computes file hashes
│   ├── finder.py      # Identifies duplicate files
│   ├── organizer.py  # Moves or deletes duplicate files
│   ├── database.py   # Handles SQLite storage
│   ├── actions.py    # Logs file actions
│
├── main.py            # Entry point and user interaction
├── file_organizer.db  # SQLite database (generated at runtime)
├── .gitignore
├── README.md
```

--------------------------------------------------

## File explanations

main.py

This is the main entry point of the program.

It is responsible for:
- Collecting user input
- Coordinating scanning, hashing, and duplicate detection
- Displaying results
- Triggering file actions based on user choice

--------------------------------------------------

## src/scanner.py

Handles folder traversal.

This file:
- Expands user paths (such as ~)
- Recursively scans directories
- Skips invalid, hidden, or unreadable files
- Returns a list of valid file paths

--------------------------------------------------

## src/hasher.py

Handles file hashing.

This file:
- Reads files in chunks to support large files
- Computes hash checksums (MD5 by default)
- Groups files by hash value

--------------------------------------------------

## src/finder.py

Identifies duplicate files.

This file:
- Accepts a hash-to-files mapping
- Filters out hashes that only appear once
- Returns confirmed duplicate groups

--------------------------------------------------

## src/organizer.py

Handles file actions.

This file:
- Moves duplicate files to a dedicated folder
- Deletes duplicate files if requested
- Logs all file operations

--------------------------------------------------

## src/database.py

Handles persistent storage.

This file:
- Initializes a local SQLite database
- Stores file metadata
- Stores action logs for reference

--------------------------------------------------

## src/actions.py

Handles logging and history.

This file:
- Records file move and delete actions
- Displays past actions to the user

--------------------------------------------------

## Installation / Usage

Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/duplicate-file-finder.git
cd duplicate-file-finder
```
Run the program:
```
python main.py
```
--------------------------------------------------

## Notes and limitations

- This tool uses file hashing to detect duplicates, not filenames.
- Hashing large files may take time depending on system performance.
- Deleted files are permanently removed.
- The project is designed for educational purposes.
- No files are modified unless the user explicitly chooses an action.

--------------------------------------------------

## License

This project is provided for educational use.
