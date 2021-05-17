# -*- coding: utf-8 -*-
import os
import platform,socket,re,uuid,logging,multiprocessing, base64

print('platform : ' +  platform.system())
print('platform-release : ' + platform.release())
print('platform-version : ' + platform.version())
print('architecture : ' + platform.machine())
print('hostname : ' + socket.gethostname())
print('ip-address : ' + socket.gethostbyname(socket.gethostname()))
print('mac-address ' + ':'.join(re.findall('..', '%012x' % uuid.getnode())))
print('processor : ' + platform.processor())
print('logical threads : ' + str(multiprocessing.cpu_count()))
print('Press enter ...')
input()

