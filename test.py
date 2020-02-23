#!/usr/bin/python3

import sys
import json
import socket

server= sys.argv[1]
print('Target:', server)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

results = {}
list1 = []
list2 = []

plist = [21, 22, 23, 53, 80, 61, 139, 443, 3389, 8080] 

length = len(plist) 

for x in plist:
    if pscan(x):
        print('port',x,'is open')
        list1.append(x)
    else:
        print('port',x,'is closed')
        list2.append(x)

print('Summary open ports:', list1)
print('Summary closed ports:', list2)

results = {server: list1}

s = set(list1)

with open('portstatus.json', 'r') as f:
    data = json.load(f)
    if data.get(server) is not None: 
        t = set(data[server])
        z = t.difference(s)
        if not z:
            print('No port status changes since last scan')
        else:
            print('Port', z,'has changed status')
            tmp = data[server]
            data[server] = list1
#            with open('portstatus.json', 'w') as f:
#                json.dump(results, f)
#            f.close()
#            quit()
            
with open('portstatus.json', 'w') as f:
    json.dump(results, f)

f.close()