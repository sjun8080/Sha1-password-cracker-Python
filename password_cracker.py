import hashlib

def crack_sha1_hash(hash, use_salts = False):
    passwords_arr = []
    read_and_add_to_arr("top-10000-passwords.txt",arr)

    if use_salts:
        top_salt_passwords = {}
        top_salts = []
        read_and_add_to_arr("known-salts.txt", top_salts)
        
        for baslt in top_salts:
            for bpassword in passwords_arr:
                prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
                appened = hashlib.sha1(bpassword +bsalt).hexdigest()
                top_salt_passwords[prepended] = bpassword.decode("utf-8")
                top_salt_passwords[appened] = bpassword.decode("utf-8")
        if hash in top_salt_passwords:
            return top_salt_passwords[hash]
    passwords_dict = {}
    for p in passwords_arr:
        hash_line = hashlib.sha1(p).hexdigest()
        passwords_dict[hash_line] = p.decode(utf-8)
    
    if hash in passwords_dict:
        return passwords_dict[hash]

    return "PASSWORDS NOT IN DATABASE"

        

    print(passwords_arr) #Prints the arr list to the console, showing all the passwords read from the file in their raw binary format.
    return "PASSWORD NOT IN DATABASE" #Regardless of the input, the function always returns "PASSWORD NOT IN DATABASE". This is likely a placeholder and not the final logic. 

   


def read_and_add_to_arr(file_name,arr):
      with open("top-10000-passwords.txt", "rb") as f:
        line = f.readline().strip() #Reads one line from the file and removes any leading or trailing whitespace (e.g., \n).
        while line: #If line is not empty, 
            arr.append(line) #it appends the password to the arr list.
            line = f.readline().strip() #Continues reading until the file is fully read (when line becomes empty).
    
