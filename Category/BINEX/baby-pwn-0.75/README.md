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


4. 
