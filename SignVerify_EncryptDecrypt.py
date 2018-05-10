# -*- coding: cp936 -*-

import rsa
print("start")

# ������Կ
(pubkey, privkey) = rsa.newkeys(1024)


# ������Կ
with open('public.pem','w+') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('private.pem','w+') as f:
    f.write(privkey.save_pkcs1().decode())


# ������Կ
with open('public.pem','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem','r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

    
# ����
message = 'hello'

# ��Կ����
crypto = rsa.encrypt(message.encode(), pubkey)

# ˽Կ����
message = rsa.decrypt(crypto, privkey).decode()
print(message)



# ˽Կǩ��
signature = rsa.sign(message.encode(), privkey, 'SHA-1')

# ��Կ��֤
rsa.verify(message.encode(), signature, pubkey)