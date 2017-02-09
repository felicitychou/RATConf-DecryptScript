#!/usr/bin/env Python
# -*- coding:utf-8 -*-

import os

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
    result = readhex(filepath=filepath,offset=10320,len=2,dec=False)
    result.reverse()
    return int("".join(result), 16) 

def get_ip(filepath):
    result = readhex(filepath=filepath,offset=10020,end=0)
    return [chr(x) for x in result]

def get_C2(filepath):
    return "".join(get_ip(filepath)) + ":" + str(get_port(filepath))

def main():
    print "Trojan-DDoS.Linux.MrBlack.J DecryptConf Result:"
    path = 'sample'
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        print "%s C2 is %s" % (item,get_C2(item))

if __name__ == '__main__':
    main()



