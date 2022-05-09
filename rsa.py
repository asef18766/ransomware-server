from Crypto.Util.number import long_to_bytes
def parsing(data:str)->int:
    return int.from_bytes(
        bytes.fromhex(data.replace(' ', '').replace('\n', '').replace('\r', '').replace(':', '')), 'big'
    )
d = '''00:b4:6b:35:92:4a:76:89:f5:8f:ad:a6:59:49:d8:
    e3:51:f9:00:73:af:28:cd:9f:c8:c9:87:03:49:c5:
    af:13:eb:b0:95:01:da:9c:2c:72:34:f9:e1:e6:b1:
    32:48:b4:08:c3:cc:3e:15:2c:8c:58:0a:d3:d3:5a:
    c8:52:cd:6d:11:71:46:c2:84:49:bd:a2:e5:8a:6f:
    19:4a:41:f0:a8:be:fc:25:c2:2d:68:3d:0a:87:53:
    52:21:f8:f4:7d:ac:55:d8:7a:ba:f6:68:a6:b2:6d:
    67:ce:b0:e4:e7:5d:6e:65:d1:8d:22:2c:0a:01:d0:
    25:67:5d:0c:27:43:85:5f:ca:24:a1:75:28:0c:eb:
    a1:15:3f:8a:b6:d5:c5:ba:b7:ed:3c:41:be:b7:24:
    d3:f2:6c:db:71:f1:ef:31:9c:80:7c:bd:6b:4a:ac:
    04:f1:fd:0d:87:4a:70:1e:e5:52:01:ef:90:3d:f1:
    45:23:b6:1d:10:b7:bf:d5:8a:b3:37:ad:f5:16:4f:
    47:cb:1a:4e:e4:1a:02:30:95:85:7a:f4:71:1d:ce:
    41:27:f0:73:e7:ac:a9:3e:1c:5e:87:50:c6:3d:45:
    be:0a:01:4e:1b:31:d6:2a:70:04:ed:a7:9c:7e:c2:
    f7:14:11:be:ba:e5:ab:57:47:71:e2:b7:98:99:ff:
    fd:c3:fe:5c:03:01:a5:ce:6b:ac:44:a7:9b:7d:49:
    48:2b:bf:87:9b:48:73:fb:98:68:11:ef:ac:8c:50:
    64:11:2a:c6:3b:d1:3b:fc:be:9a:73:43:68:39:ee:
    26:15:13:90:bf:f9:4a:eb:d9:f5:ac:81:22:81:d9:
    cc:a4:28:49:b5:27:17:e5:fc:02:af:0d:91:f9:57:
    93:f5:af:f6:b8:cc:3c:25:38:30:a2:88:c1:07:5f:
    35:b4:db:d5:ff:31:7b:c2:d0:97:74:6b:66:d2:ed:
    27:9c:a0:96:01:44:d0:b0:a7:ed:8a:13:ed:bd:1b:
    93:a4:cd:71:81:5a:8c:c5:8c:be:e1:d4:4c:1c:97:
    6d:d9:c9:9a:aa:ba:41:be:d2:05:05:62:d9:48:28:
    6c:2b:d8:c6:24:3b:14:a7:99:d1:6b:28:af:19:3a:
    c4:21:b6:9f:88:7a:7d:fe:5b:b9:c2:65:db:b4:03:
    65:fb:52:15:12:b9:1e:be:d9:72:1c:99:bd:9f:b7:
    5b:d8:cf:21:7c:3e:66:5a:ec:b3:e1:82:e6:f5:70:
    68:8f:0c:d0:2c:db:b0:cc:89:1c:18:88:fd:55:5b:
    ef:49:a7:1f:f9:ee:30:4b:8d:78:3f:c6:49:0e:db:
    53:b5:57:34:19:c8:d0:9f:f8:55:bb:06:36:7d:e8:
    a3:5e:01
'''
n = '''
     00:ba:f8:d1:95:32:22:79:9e:e2:a3:e3:eb:14:92:
    b0:cc:86:aa:33:2a:81:b8:34:ae:ea:13:28:a5:53:
    bf:fb:71:ea:2c:f5:aa:f3:3c:95:c0:82:aa:cc:6c:
    86:4e:76:03:ea:f8:65:b1:7a:63:2e:1c:bd:a2:fc:
    63:48:03:a0:65:6b:f8:91:20:a9:2f:4c:dc:87:31:
    24:78:73:87:0d:f4:d0:93:68:63:65:e4:4a:3e:3c:
    03:b6:98:c0:74:b7:a2:7e:2c:2f:bd:4d:6b:76:e6:
    7d:71:27:8e:5d:15:2b:a2:9a:4a:c2:37:09:cd:c7:
    be:ad:a7:ed:9f:7e:1f:d0:a6:dc:f9:77:2e:6a:5d:
    a5:e8:e1:44:53:2a:60:a3:35:6f:31:72:75:86:f5:
    f9:29:f0:f7:06:4d:ec:00:2d:48:38:fd:05:4f:ba:
    5f:23:46:5e:a5:31:8b:c6:f5:de:06:8c:4c:7b:74:
    c2:43:46:a2:46:3a:ae:dd:9e:2b:57:16:3c:30:13:
    8d:77:26:bd:71:7a:aa:73:51:fd:69:41:f3:92:cb:
    f4:2c:1d:42:42:64:01:db:6d:9b:b0:01:de:4f:e8:
    aa:04:98:90:6b:c6:8e:27:35:da:5c:16:73:82:58:
    7f:8f:14:0e:b0:62:58:44:9a:0e:df:8e:81:6a:49:
    de:47:31:37:ef:b6:03:8d:85:9f:80:2f:6d:f2:8e:
    2c:ee:e0:e5:ff:80:1e:0c:ba:78:a9:62:92:0e:e2:
    25:44:ce:41:c7:42:30:03:78:39:d5:6c:44:93:d2:
    f4:a4:24:47:1a:08:2c:69:57:3f:6f:70:4c:4a:76:
    67:39:58:fd:a5:b2:91:1e:e3:8e:34:54:9b:5b:b4:
    0f:09:8e:be:73:95:1b:6c:e4:4e:9a:5e:f4:15:4d:
    d3:b4:f9:2d:b2:90:2a:82:a1:f2:b5:1a:69:a1:74:
    e6:cf:16:e0:c0:67:f4:04:5c:b9:5b:12:20:6c:b5:
    ff:5e:17:c0:b8:a5:11:f3:5f:76:43:c3:71:75:8a:
    87:b9:d6:ca:08:bf:ca:cf:5c:ff:39:eb:7c:89:3e:
    4f:6f:92:45:b1:cd:61:3f:a4:5e:4b:d0:2a:cf:d6:
    b0:ed:3a:bd:22:01:ee:59:cd:e8:49:4a:35:e1:73:
    8f:b4:72:ff:86:0d:69:57:5b:84:5e:27:1e:cb:f6:
    3f:5f:ad:97:c4:c5:c1:b2:88:be:90:65:00:f4:7a:
    d7:07:78:6c:ce:be:2f:fb:6c:b0:89:13:e6:f1:e6:
    71:b0:d3:54:f8:88:a3:77:04:dc:e7:b2:3a:a1:d6:
    ba:62:68:2e:b9:54:6f:45:d7:84:11:92:e1:52:09:
    a8:82:41
'''
d = parsing(d)
n = parsing(n)

def decrypt(data:bytes)->bytes:
    ct = int.from_bytes(data, 'big')
    msg = long_to_bytes(pow(ct, d, n))
    return msg

if __name__ == "__main__":
    print(decrypt(
            bytes.fromhex("3B023B3A40521FD12F0288504B1B39EB7499C31C8452989DE9EBBB97122851DBC35F0C0A60406EC8D9A441DF3A6089714BF6E3B3DA9B061F529E80A8C587E2C1AF27739C3733A07F58842E476B88A4A9B66F35C674AC8E329DD85384F445CC43FB21130CED95590BB69C466D710A2478F57BCB9F9F02CEE8B8FB8DC51E27D3E275D3976AE01A6056E09F8B1B31769F89F651E0F9817B48773431136D61553628191099BF63928C738F1AAC25F7FDCEAA15303AF11FCAD5AA4F4DCB1288E6D84568A8D87E38238BBBB584271116B778703E4A85AA8D815A9C3996F3B395C92D2C9D5AC55047A93892F0109661942BAC31418A600603120AD6F988D15A8B5FD499E0B88430601CBB142CED99E979E154508386FB0DB583CF9099D6B30BA856015ED6174D61B5C2072673266CA3CE51BC4C54307EED0626E4EF34938ECA3F8740C0ACFB9CEFDD277FE96EEF7C3E04A0A9E1618F85BEFE17A48012881D776F92700DE0BF5ED6F3AA79576D84A0536E37F9FB2A79B6F864BC510DDB1B7AD1655745646DD80CD5779DA3696532BFCD807E1BB4CDF5157F7E8BE82077BDE03A8805A9EEC342DE0EE5EC87FAB93CA93D038B24799C350E3287DB92319BFFD971A4FD3EB7B20FA3B892B21234EFB9C2D3D6511230D2B3F6014C88AF2D49A246D8C5C41B881BB376CF51274E8ADFFB3152217BEF805F86617A6B5FE6D7252E5BA30ED46F3E")
        ))