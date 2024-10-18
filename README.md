Password Cracking Script 

This script is a simple demonstration of a password cracking technique known as a dictionary attack. It takes a given password and checks it against a predefined list of potential passwords (a wordlist).

How it Works

The script defines a function crack_password that takes two parameters: hash (the password to crack) and wordlist (a list of possible passwords).
The function iterates through each word in the wordlist and checks if the stripped version of the word matches the provided hash.
If a match is found, the function prints the found password and returns.
If no match is found after checking all words, the function prints "Password not found in list".
