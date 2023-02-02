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


2. 
