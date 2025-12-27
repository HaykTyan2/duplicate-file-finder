# src/hasher.py
import hashlib
from pathlib import Path

def compute_hash(file_path: Path, algo="md5", chunk_size=8192):
    """
    Compute the hash checksum of a file (MD5 by default).
    Reads the file in chunks to handle large files safely.
    """
    hash_func = hashlib.new(algo)
    
    try:
        #rb = read bytes
        #we use binary mode AKA rb because hashing needs the raw bytes, not the decoded text
        with open(file_path, "rb") as f:
            chunk = f.read(chunk_size)
            while chunk:
                #.update() doesn't store the bytes into hash_func, instead it stores some math stuff 
                #which is then turned into a random hex via hexdigest() and returned as a string
                hash_func.update(chunk)
                chunk = f.read(chunk_size)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Could not hash {file_path}: {e}")
        return None


def hash_all_files(files_found):
    """
    Given a list of Path objects, compute and return a dict of hashes.
    {hash: [file_path1, file_path2, ...]}
    """
    hash_map = {}

    for file_path in files_found:
        file_hash = compute_hash(file_path)
        if not file_hash:
            continue

        # Store files grouped by hash
        hash_map.setdefault(file_hash, []).append(file_path)
        
    return hash_map
