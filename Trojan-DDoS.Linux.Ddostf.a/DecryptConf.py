#!/usr/bin/env Python3
# -*- coding:utf-8 -*-

import os

confs = [
{'filesize':(1058408,1048576,942080),'ip_offset':0xC1144,'port_offset':0xC1244},
{'filesize':(649585,),'ip_offset':0x8c164,'port_offset':0x8c264},
{'filesize':(748716,),'ip_offset':0x9013c,'port_offset':0x9023c},
{'filesize':(722462,),'ip_offset':0x8B134,'port_offset':0x8B234},
{'filesize':(649761,),'ip_offset':0x7f104,'port_offset':0x7f204},
{'filesize':(633684,),'ip_offset':0x7c0c4,'port_offset':0x7c1c4},

]
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
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        filesize = os.path.getsize(item)
        global IP_OFFSET,PORT_OFFSET
        for c in confs:
            if filesize in c['filesize']:
                IP_OFFSET = c['ip_offset']
                PORT_OFFSET = c['port_offset']
                break
        else:
            continue
        print("%s C2 is %s" % (item,get_C2(item)))

if __name__ == '__main__':
    main()



