from pathlib import Path

def find_duplicates(hash_map):
    """
    Given a hash_map of {hash: [file1, file2, ...]}, return only
    the entries where the list has 2 or more files.
    """
    duplicates = {}

    for file_hash, paths in hash_map.items():
        if len(paths) > 1:
            duplicates[file_hash] = paths

    return duplicates
