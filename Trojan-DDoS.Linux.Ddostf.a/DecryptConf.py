#!/usr/bin/env Python3
# -*- coding:utf-8 -*-

import os

IP_OFFSET = 0x0
PORT_OFFSET = 0x0

def  readhex(filepath,offset,end=0,len=32,dec=True):
    f = open(filepath ,'rb')
    f.seek(offset,0)
    result = []
    i = 0
    while i < len:
        byte = f.read(1)
        
        if byte == b'\x00':
            break
        else:
            #hexstr =  "%s" % byte.encode('hex')
            #decnum = int(hexstr, 16)
            decnum = int.from_bytes(byte, byteorder='big')
            #print(decnum)
            if decnum != end:
                if dec:
                    result.append(decnum)
                else:
                    result.append(byte)
                i = i+1
            else:
                break
    f.close()
    return result

def get_port(filepath):
    result = readhex(filepath=filepath,offset=PORT_OFFSET,len=2,dec=False)
    return int.from_bytes(b''.join(result), byteorder='little')

def get_ip(filepath):
    result = readhex(filepath=filepath,offset=IP_OFFSET,end=0)
    return [chr(x) for x in result]

def get_C2(filepath):
    return "".join(get_ip(filepath)) + ":" + str(get_port(filepath))

def main():
    print("HEUR:Trojan-DDoS.Linux.Ddostf.a DecryptConf Result:")
    path = 'sample'
    #path = '/Users/felicitychou/Public/200_WORK/ddostf/'
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        filesize = os.path.getsize(item)
        global IP_OFFSET,PORT_OFFSET
        if filesize in (1058408,1048576,942080):
            IP_OFFSET = 0xC1144
            PORT_OFFSET = 0xC1244
        elif filesize == 649585:
            IP_OFFSET = 0x8c164
            PORT_OFFSET = 0x8c264
        else:
            continue
        print("%s C2 is %s" % (item,get_C2(item)))

if __name__ == '__main__':
    main()



