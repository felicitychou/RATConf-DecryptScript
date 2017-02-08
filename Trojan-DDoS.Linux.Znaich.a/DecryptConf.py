#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

def  readhex(filepath,offset,end=0,len=32):
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
                result.append(decnum)
                i = i+1
            else:
                break
    f.close()
    return result

decrypt_ip = [32,12,32,11,2,10,18,38,23,1,10,9,6,4,21,23,23,10,1,9]
decrypt_port = [27,34,37,50,44]
prefix = [17,252,52,47]


def get_C2(filepath):
    # x86
    if os.path.getsize(filepath) == 1584675:
        return decryptConf(filepath = filepath,offset = 1171712)
    # x64
    elif os.path.getsize(filepath) == 1820918:
        return decryptConf(filepath = filepath,offset = 1332192)
    else:
        return "Cannot Decrypt Conf."

def decryptConf(filepath,offset):
    result = readhex(filepath=filepath,offset=offset,end=0,len=32)
    
    if check(result[:4]) and len(result) <= 24:
        ip_domain = "".join(get_ip(result[4:]))
        port = "".join(get_port(result[-5:]))
        if port.isdigit():
            return "%s C2 is %s:%s" % (filepath,ip_domain,port)
        else:
            return "%s ip/domain is %s and port is not num." % (filepath,ip_domain)
    else:
        return "%s sets too long ip/domain %s." % (filepath,"".join(get_ip(result[4:])))

def check(result):
    i = 0
    while i < len(result):
        if result[i] != prefix[i]:
            return False
        i = i+1
    return True

def get_ip(result):
    i = 0
    while i < len(result):
        if i < len(decrypt_ip):
            result[i] = result[i] - decrypt_ip[i]
            if chr(result[i]).isalnum() or result[i] == 46:
                result[i] = chr(result[i])
            else:
                return result[:i]
        else:
            return result[:i] + [chr(i) for i in result[i:]]
        i = i+1
    return result[:i]

def get_port(result):
    i = 0
    while i < len(result):
        result[i] = chr(result[i] + decrypt_port[i])
        i = i+1
    return result

def main():
    print "Trojan-DDoS.Linux.Znaich.a DecryptConf Result:"
    path = 'sample'
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        print get_C2(item)

if __name__ == '__main__':
    main()




