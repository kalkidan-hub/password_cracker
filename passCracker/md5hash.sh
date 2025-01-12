#!/bin/bash

words=("xc" "ab" "qwerty" "123456" "password" "johndash" "unknown" "un_crackable")

output_file="hashes.txt"

> "$output_file"

for word in "${words[@]}"; do 
	echo -n "$word" | md5sum | awk '{print $1}' >> "$output_file" 
done
