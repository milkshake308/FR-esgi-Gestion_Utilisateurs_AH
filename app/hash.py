import hashlib

def sha256_generator(str):
    m = hashlib.sha256()
    m.update(str.encode())

    return m.hexdigest()

