from pathlib import Path


def scan_folder(folder_path):
    """
    Recursively scan the given folder and return a list of all file paths.
    Skips directories, hidden files, and unreadable paths.

    Args:
        folder_path (str | Path): Base folder to scan

    Returns:
        list[Path]: List of absolute file paths
    """
    #.expanduser() expands the ~ part of the path
    #~ is equivalent to C:\Users\Levi
    #so expander here turns ~/Desktop into C:\Users\Levi\Desktop
    #resolve() turns ../folder into the absolute path it actually is C:\Users\Levi\Documents
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        print(f"Invalid folder path: {folder}")
        return []

    print(f"Scanning folder: {folder}")

    files_found = []

    try:
        # Path.rglob('*') recursively yields all files/subfolders
        for path in folder.rglob("*"):
            # Only include regular files (ignore dirs)
            if path.is_file():
                # Skip hidden files (optional)
                if not path.name.startswith("."):
                    files_found.append(path)
    except PermissionError:
        print(f"Permission denied while scanning: {folder}")
    except Exception as e:
        print(f"Error scanning folder: {e}")

    print(f"Found {len(files_found)} files in {folder}")
    return files_found


