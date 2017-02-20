import os
import binascii

def filereadhex(filepath,offset=0,end='',length=0):
    with open(filepath,'rb') as file:
        file.seek(offset,0)

        if end:
            data = file.read()
            return binascii.hexlify(data[:data.find(end)])

        if length:
            return binascii.hexlify(f.read(length))

        return binascii.hexlify(f.read())

def get_C2(filepath):
    return binascii.unhexlify(filereadhex(filepath=filepath,offset=0x4CA4,end='\x00'))

def main():
    print "Backdoor.Win32.Zegost.AK DecryptConf Result:"
    path = 'sample'
    for item in [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        print "%s C2 is %s" % (item,get_C2(item))

if __name__ == '__main__':
    main()
