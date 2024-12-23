import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load passwords
    passwords_arr = []
    read_and_add_to_arr("top-10000-passwords.txt", passwords_arr)

    # If using salts
    if use_salts:
        top_salts = []
        read_and_add_to_arr("known-salts.txt", top_salts)

        # Generate salted hashes
        salted_hashes = generate_salted_hashes(passwords_arr, top_salts)
        if hash in salted_hashes:
            return salted_hashes[hash]

    # Generate unsalted hashes
    passwords_dict = {}
    for password in passwords_arr:
        hash_line = hashlib.sha1(password).hexdigest()
        passwords_dict[hash_line] = password.decode("utf-8")

    # Check hash
    if hash in passwords_dict:
        return passwords_dict[hash]

    return "PASSWORD NOT IN DATABASE"


def generate_salted_hashes(passwords, salts):
    salted_hashes = {}
    for salt in salts:
        for password in passwords:
            prepended = hashlib.sha1(salt + password).hexdigest()
            appended = hashlib.sha1(password + salt).hexdigest()
            salted_hashes[prepended] = password.decode("utf-8")
            salted_hashes[appended] = password.decode("utf-8")
    return salted_hashes


def read_and_add_to_arr(file_name, arr):
    try:
        with open(file_name, "rb") as f:
            line = f.readline().strip()
            while line:
                arr.append(line)
                line = f.readline().strip()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
