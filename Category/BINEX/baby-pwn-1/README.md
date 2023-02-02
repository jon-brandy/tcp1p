# baby-pwn-1
> Write-up author: vreshco
## DESCRIPTION:
Kamu tau gak, Buffer Overflow bisa sangat berbahaya?

Koneksikan dengan service menggunakan command:

nc ctf.tcp1p.com 50283

## HINT:
- NONE
## STEPS:
1. First, download the binary file given, then check the binary type and it's protections.

> RESULT 64 bit binary file, not stripped.

![image](https://user-images.githubusercontent.com/70703371/216246376-2fdb7c1e-b719-4884-bfe8-3efbad3a77e9.png)


> RESULT - NO CANARY FOUND, PARTIAL RELRO 

![image](https://user-images.githubusercontent.com/70703371/216246535-68d7f683-9cda-4d79-8665-2e720bc670aa.png)


2. Let's decompile the binary.
3. Go Check the `vuln()` function.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/216247886-ac5675d9-311a-4885-b3f5-0367bd7f2151.png)


4. Based on it, there's a bufferoverflow at the **do-while** loop, where the loop stops if the value of `local_c` is equal to 121.
5. Notice the `local_c` size will used as the buffer for `auStack120` variable, and that var only accept 104 bytes. This is the vuln.
6. But what seems odd here, there's no `flag()` function called. Since there's PIE protections hence we can't do ret2win.
7. Let's decompile the binary using IDA then.

> RESULT



