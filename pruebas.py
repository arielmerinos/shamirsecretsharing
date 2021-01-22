from hashlib import sha256
key = str(30924103179126723853473526558182844840865767751359376108391005568002681592828)
number = sha256(key.encode('utf8')).digest()
print(number)
K = int(number.hexdigest(), 16) 
print(K)