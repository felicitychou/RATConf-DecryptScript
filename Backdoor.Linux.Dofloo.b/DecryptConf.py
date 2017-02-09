#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os 

decrypt_list=[0x20,0x4e]

def  readhex(filepath,offset,end=0,len=32,dec=True):
    f = open(filepath ,'rb')
    f.seek(offset,0)
    result = []
    i = 0
    while i < len:
        byte = f.read(1)
        if byte == '':
            break
        else:
            hexstr =  "%s" % byte.encode('hex')
            decnum = int(hexstr, 16)
            if decnum != end:
                if dec:
                    result.append(decnum)
                else:
                    result.append(hexstr)
                i = i+1
            else:
                break

    f.close()
    return result

def get_port(filepath):
    result = readhex(filepath=filepath,offset=950500,len=2,dec=False)
    result.reverse()
    return int("".join(result), 16) + int('4e20',16)

def get_ip(filepath):
    result = readhex(filepath=filepath,offset=950496,len=4,dec=False)
    i = 0
    while i < len(result):
        if i < 2:
            result[i] = str(int(result[i],16) + decrypt_list[i])
        else:
            result[i] = str(int(result[i],16))
        i = i+1
    return result

def get_C2(filepath):
    return ".".join(get_ip(filepath)) + ":" + str(get_port(filepath))

def main():
    print "Backdoor.Linux.Dofloo.b DecryptConf Result:"
    path = 'sample'
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        print "%s C2 is %s" % (item,get_C2(item))

if __name__ == '__main__':
    main()



