from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
key = bytes.fromhex("81f3bc34a5d86d35d4a4128aac439c0d282aed66f1be97facfb1b7539e082ebb")
iv = bytes.fromhex("ee14e8fc139de1da0a86bcf0f9e0ba77ea82857a8820cd16b99a4e4dbafb829e")
print(f"key len:{len(key)}")
print(f"iv len:{len(iv)}")

cipher = AES.new(key, AES.MODE_CBC, iv)
res = list(
    unpad(
        cipher.decrypt(
            bytes.fromhex("EB2629E8587389B56772A7659971EDB061C519C45682C8A20B3869E6D068F4F9")
        ), 
        256//8
    )
)
print(res)