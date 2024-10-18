def crack_password(hash, wordlist):
    for word in wordlist:
        # Simulate MD5 hash for demonstration (replace with actual hash function if needed)
        if word.strip() == hash:
            print("Password found: " + word)
            return
    print("Password not found in list")

hash = input("Enter the password to crack: ")
wordlist = ["password", "123456", "letmein", "admin", "welcome"]  # Example wordlist
crack_password(hash, wordlist)
