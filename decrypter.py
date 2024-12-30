import os
import pyaes
import sys
import glob

folder_path = './'
encrypt_file_name_flag = '.ransomwaretroll'
matching_files = glob.glob(os.path.join(folder_path, '*'+encrypt_file_name_flag+'*')) 

for file_name in matching_files:
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    key = bytes(sys.argv[1], 'utf-8')
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)
    os.remove(file_name)

    new_file = file_name.split(encrypt_file_name_flag)[0]
    new_file = open(f'{new_file}', "wb")
    new_file.write(decrypt_data)
    new_file.close()