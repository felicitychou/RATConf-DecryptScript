#!/usr/bin/env python
#-*-coding:utf8-*-

import os

def readhex(filepath,offset,end):
    f = open(filepath ,'rb')
    f.seek(offset,0)
    result = []
    while True:
        byte = f.read(1)
        if byte == '':
            break
        else:
            hexstr =  "%s" % byte.encode('hex')
            decnum = int(hexstr, 16)
            if decnum != end:
                result.append(decnum)
            else:
                break
    f.close()
    return result

def decrypt(i,num):
    if i % 2 == 0:
        return chr(num - 1)
    else:
        return chr(num + 1)

def decryptConf(filepath,offset):
    result = readhex(filepath=filepath,offset=offset,end=0)
    i = 0
    while i < len(result):
        result[i] = decrypt(i,result[i])
        i = i+1
    return result

def get_C2(filepath): 
    ip_domain = decryptConf(filepath=filepath,offset=944768)
    port = decryptConf(filepath=filepath,offset=944808)
    return "%s:%s" % ("".join(ip_domain),"".join(port))

def main():
    print "Backdoor.Linux.Mayday.f DecryptConf Result:"
    path = 'sample'
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        print "%s C2 is %s" % (item,get_C2(item))

if __name__ == '__main__':
    main()
