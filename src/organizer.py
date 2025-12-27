import shutil
from pathlib import Path
from src.actions import log_move, log_delete

def move_duplicates(duplicates, target_folder):
    target = Path(target_folder)
    target.mkdir(exist_ok=True)

    for file_hash, paths in duplicates.items():
        for dup in paths[1:]:
            destination = target / dup.name
            shutil.move(str(dup), str(destination))
            log_move(dup, destination)
            print(f"Moved: {dup} -> {destination}")

def delete_duplicates(duplicates):
    for file_hash, paths in duplicates.items():
        for dup in paths[1:]:
            #unlink() is path's way of immediately deleting a file, only used for files not folders
            dup.unlink()
            log_delete(dup)
            print(f"Deleted duplicate: {dup}")
