
import hashlib


with open ('sample_wordlist.txt', 'r') as file:
    word_list = file.read().splitlines()

with open('md5rainbow_table.txt', 'w') as file:
    for word in word_list:
        print(word)
        hash = hashlib.md5(word.encode()).hexdigest()
        file.write(f"{hash}:{word}\n")
with open('sha1rainbow_table.txt', 'w') as file:
    for word in word_list:
        hash = hashlib.sha1(word.encode()).hexdigest()
        file.write(f"{hash}:{word}\n")
