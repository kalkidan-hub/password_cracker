# input: hash value or a file containig list of hashes
# output: password or a file containing list of passwords

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
from passlib.hash import nthash

def hash_password(password, salt, algorithm):
    # Combine the salt and password
    pass_to_be_hashed = salt + password
   
    
    # Hash the combined string using the specified algorithm
    if algorithm == 'md5':
        return hashlib.md5(pass_to_be_hashed.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(pass_to_be_hashed.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(pass_to_be_hashed.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(pass_to_be_hashed.encode()).hexdigest()
    elif algorithm == 'ntlm':
        return nthash.hash(password)
    else:
        raise ValueError("Unsupported algorithm")

def verify_password(password, hash_value, algorithm, salt=''):
    if algorithm == 'ntlm':
        return nthash.verify(password, hash_value)
    else:
        return hash_password(password, salt, algorithm) == hash_value




def crack_by_the_list(hash_list, wordlist_file, algorithm,salt_list=None):
    # for all hashes in the hash_list find the password from the wordlist using the algorithm
    
    
    # Read the word list from the file
    with open(wordlist_file, 'r') as word_file:
        word_list = [word.strip() for word in word_file]
    
    def check_password(word):
        for i, hash_value in enumerate(hash_list):
            salt = salt_list[i] if salt_list else ''
            if verify_password(word, hash_value, algorithm, salt):
                print(f"Password found for hash {hash_value}: {word}")
                return True
        return False

    with ThreadPoolExecutor() as executor:
        results = executor.map(check_password, word_list)
        if any(results):
            return

def wordlist_generator(pattern):
    # given a pattern generate possible words 
    # Generate possible words based on the pattern
    # This function yields each possible word
    char_map = {
        'd': '0123456789',
        'l': 'abcdefghijklmnopqrstuvwxyz',
        'u': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        's': '!@#$%^&*()-_=+[]{}|;:,.<>?/~`',
        'a': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    }

    def generate_combinations(pattern):
        if not pattern:
            yield ''
        else:
            first, rest = pattern[0], pattern[1:]
            if first in char_map:
                for char in char_map[first]:
                    for combination in generate_combinations(rest):
                        yield char + combination
            else:
                for combination in generate_combinations(rest):
                    yield first + combination

    return generate_combinations(pattern)

def crack_by_the_pattern(hash_list, pattern, algorithm,salt_list=None):
    def check_password(word):
        for i, hash_value in enumerate(hash_list):
            salt = salt_list[i] if salt_list else ''
            if verify_password(word, hash_value, algorithm, salt):
                print(f"Password found for hash {hash_value}: {word}")
                return True
        return False

    with ThreadPoolExecutor() as executor:
        results = executor.map(check_password, wordlist_generator(pattern))
        if any(results):
            return
       

def rainbow_table_attack(hash_list, algorithm, rainbow_table_file):
    # use the rainbow table to crack the hashes
    # Load the rainbow table into a dictionary
    with open(rainbow_table_file, 'r') as f:
        for line in f:
            stored_hash_value, password = line.strip().split(':')

            # Check each hash against the rainbow table
            for hash_value in hash_list:
                if hash_value in stored_hash_value:
                    print(f"Password found for hash {hash_value}: {password}")

def main():
    # parse the input arguments
    parser = argparse.ArgumentParser(description='Password Cracker')
    parser.add_argument('--hash-file', type=str, required=True, help='File containing list of hashes')
    parser.add_argument('--algorithm', type=str, required=True, help='Hashing algorithm to use, supported algorithms are md5, sha1, sha256, sha512, ntlm')
    parser.add_argument('--mode', type=str, required=True, choices=['list', 'pattern', 'rainbow'], help='Mode of operation. \n Use rainbow where there\'s no salt for the hash')
    parser.add_argument('--wordlist-file', type=str, help='File containing list of words')
    parser.add_argument('--pattern', type=str, help='Pattern to generate wordlist, d- digits, l- lowercase, u- uppercase, s- special characters, a- all characters')
    parser.add_argument('--salt_file', type=str, help='File containing list of corresponding salts used in hashing')
    parser.add_argument('--rainbow-table-file', type=str, help='File containing the rainbow table')

    args = parser.parse_args()
    
    with open(args.hash_file, 'r') as f:
        hash_list = f.read().splitlines()
    if args.salt_file:
        with open(args.salt, 'r') as f:
            salt_list = f.read().splitlines()
    else: 
        salt_list = None
    # print(hash_list)
    
    # call the appropriate function
    if args.mode == 'list':
        crack_by_the_list(hash_list, args.wordlist_file, args.algorithm, salt_list)
    elif args.mode == 'pattern':
        crack_by_the_pattern(hash_list, args.pattern, args.algorithm, salt_list)
    elif args.mode == 'rainbow':
        rainbow_table_attack(hash_list, args.algorithm, args.rainbow_table_file)

if __name__ == '__main__':
    main()
    