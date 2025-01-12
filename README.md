# Password Cracker

This is a password cracker application that supports various hashing algorithms and modes of operation. It can crack passwords using a wordlist, a pattern, or a rainbow table.

## Features

- Supports the following hashing algorithms: `md5`, `sha1`, `sha256`, `sha512`, `ntlm`
- Modes of operation:
  - `list`: Crack passwords using a wordlist
  - `pattern`: Generate and crack passwords using a pattern
  - `rainbow`: Crack passwords using a precomputed rainbow table
- Supports salted and unsalted hashes
- Parallel processing for faster cracking

## Requirements

- Python 3.x
- `passlib` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/passCracker.git
   cd passCracker

## Usage

### Command-Line Arguments

- `--hash-file`: File containing list of hashes (required)
- `--algorithm`: Hashing algorithm to use (required)
- `--mode`: Mode of operation (`list`, `pattern`, `rainbow`) (required)
- `--wordlist-file`: File containing list of words (required for `list` mode)
- `--pattern`: Pattern to generate wordlist (required for `pattern` mode)
- `--salt-file`: File containing list of corresponding salts used in hashing (optional)
- `--rainbow-table-file`: File containing the rainbow table (required for `rainbow` mode)
- `--prepend-salt`: Flag to prepend salt to the password (default is to append)

### Examples

#### Crack Passwords Using a Wordlist

```bash
python cracker.py --hash-file hashes.txt --algorithm sha256 --mode list --wordlist-file wordlist.txt
```
#### Crack passwords using patter
```bash
python cracker.py --hash-file hashes.txt --algorithm sha256 --mode pattern --pattern 'lllldd'
```
#### Crack passwords using rainbow-table
```bash
python cracker.py --hash-file hashes.txt --algorithm sha256 --mode rainbow --rainbow-table-file rainbow_table.txt
```
## License

This project is licensed under the MIT License.
