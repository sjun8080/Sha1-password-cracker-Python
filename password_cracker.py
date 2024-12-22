import hashlib

def crack_sha1_hash(hash, use_salts = False):
    passwords_arr = []
    read_and_add_to_arr("top-10000-passwords.txt",arr)
    print(passwords_arr) #Prints the arr list to the console, showing all the passwords read from the file in their raw binary format.
    return "PASSWORD NOT IN DATABASE" #Regardless of the input, the function always returns "PASSWORD NOT IN DATABASE". This is likely a placeholder and not the final logic. 

def read_and_add_to_arr(file_name,arr):
      with open("top-10000-passwords.txt", "rb") as f:
        line = f.readline().strip() #Reads one line from the file and removes any leading or trailing whitespace (e.g., \n).
        while line: #If line is not empty, 
            arr.append(line) #it appends the password to the arr list.
            line = f.readline().strip() #Continues reading until the file is fully read (when line becomes empty).
    
