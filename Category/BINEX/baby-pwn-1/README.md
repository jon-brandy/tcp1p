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


4. Based on it, there's a vuln at the `do-while`, we can control the **local_c** values by make an infinity loop, where we will set the `local_c` values beyond 121.
5. Hence we can do bufferoverflow and control the RIP.
6. But what seems odd here, there's no `flag()` function called. Since there's PIE protections hence we can't do ret2win. We only can change the **least significant bytes**.
7. Let's try to disassemble the `vuln()` function using gdb.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/216251364-06dba21c-0de6-406b-af8a-1b429001bbfb.png)


8. Hmm.. There's no `flag()` function, let's check the `main()`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/216251462-d61b2908-43d5-47be-a09a-8c3beb7c62a5.png)


9. Found it!

![image](https://user-images.githubusercontent.com/70703371/216251567-33303243-6d63-4ad2-96c5-14cdcc7438bf.png)


10. Actually it's written already in ghidra disassembler.

![image](https://user-images.githubusercontent.com/70703371/216252008-5c22afe6-c9f8-4d70-853d-a1e2e5d69d24.png)


11. 



