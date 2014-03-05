#!/usr/bin/env python
import os, sys       # do not use any other imports/libraries
# specify here how much time your solution required
# I spent 12 hours, type conversion was bit difficult for me


def bytestring_to_int(s):
    i = 0
    for k in range(len(s)):
        i = i | ord(s[k])
        i = i <<8

    i = i >>8
    return i


def int_to_bytestring(N):
    str = bin(N)
    str = "0" + str[2:]
    message = ""
    while str != "":
        i = chr(int(str[:8], 2))
        message = message + i
        str = str[8:]

    return message


def encrypt(pfile, kfile, cfile):
    # your implementation here
    fo = open(pfile, "r")
    a = os.path.getsize(pfile)
    c = fo.read(a).strip()
    x = bytestring_to_int(c)
    fo.close()

    ## For key generation ##
    #random key generation and assigning it to B
    b = os.urandom(a)
    y = bytestring_to_int(b)

    foo = open(kfile, "w")
    foo.write(str(y));

    # Close opend file
    foo.close()

    ### Writing the xored output in Cfile
    xored = int(x) ^ int(y)
    fooo = open(cfile, "w")
    fooo.write(str(xored));
    # Close opend file
    fooo.close()
    
    pass
    

def decrypt(cfile, kfile, pfile):
    # your implementation here
    #Opening cipherText File and assigning to variable d
    fa = open(cfile, "r")
    m = os.path.getsize(cfile)
    d = fa.read(m).strip()
    
    #Opening KeyFile and assigning to variable d
    faa = open(kfile, "r")
    t = os.path.getsize(kfile)
    e = faa.read(t).strip()

    unexored = int(d) ^ int(e)
    decrypted = int_to_bytestring(unexored)
    
    faaa = open(pfile, "w")
    faaa.write(str(decrypted));
    # Close opend file
    faaa.close()
    pass

def usage():
    print "Usage:"
    print "encrypt <plaintext file> <output key file> <ciphertext output file>"
    print "decrypt <ciphertext file> <key file> <plaintext output file>"
    sys.exit(1)

if len(sys.argv) != 5:
    usage()
elif sys.argv[1] == 'encrypt':
    encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt':
    decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    usage()
