# baby-pwn-2
> Write-up author: vreshco
## DESCRIPTION:
Waktunya belajar ret2libc tapi libcnya mana? Mungkin bisa dicari disini: https://libc.blukat.me/

nc 167.71.212.18 60256

## HINT:
- NONE
## STEPS:
1. Since we got a binary file, let's check the file and the binary's protections.

> TYPE - 64 BIT, binary stripped.

![image](https://user-images.githubusercontent.com/70703371/216953618-f75f88e2-d9a7-40fa-b36d-1e345d565a10.png)

> PROTECTIONS - PARTIAL RELRO - NO CANARY FOUND

![image](https://user-images.githubusercontent.com/70703371/216953782-3842ee29-f790-4834-8ab4-241f813e8ec2.png)


2. 
