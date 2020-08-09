#/usr/bin/python

import sys
import hashlib
import base58

if (len(sys.argv) != 4):
	print('usage : python skin.py {encrypt,decrypt} blob key')
	sys.exit('incorrect usage')

alphabet='rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'

letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL'

command=sys.argv[1]

blob=sys.argv[2]




key=sys.argv[3].encode();

salt=b'dontbesalty91726'

print('command : ', command)
print('blob : ', blob)
print('key', key)

dk = hashlib.pbkdf2_hmac('sha256', key, salt, 100000, dklen=21)

print(len(dk))


decoded = base58.b58decode(blob, alphabet=base58.RIPPLE_ALPHABET)

print(len(decoded))

xored = bytes(a ^ b for (a, b) in zip(decoded, dk))

encoded = base58.b58encode(xored, alphabet=base58.RIPPLE_ALPHABET)

print(encoded.decode())