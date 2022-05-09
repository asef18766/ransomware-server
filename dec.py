from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(key:bytes, iv:bytes, ct:bytes)->bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    res = unpad(
        cipher.decrypt(
            ct
        ),
        128 // 8
    )
    return res

if __name__ == "__main__":
    key = bytes.fromhex("BC078B9AB210FB05A33D136CBD3F94A40C1BED0ED29206DE3F2CA172DDDDD81A")
    iv = bytes.fromhex("CFE7895DB006737201B02D8A55BE8389")
    ct = open("IMG_20220507_122730.jpg.enc", "rb").read()

    print(f"key len:{len(key)}")
    print(f"iv len:{len(iv)}")
    res = decrypt(key, iv, ct)

    print(res[-10:])
    open("dec.jpg", "wb").write(res)
    