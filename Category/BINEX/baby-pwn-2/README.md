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


2. Let's run the binary file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/216954016-11d26bdf-ebb0-4604-be45-437d931b7657.png)


3. Printed out an address (?)
4. Let's check the source code given.

> RESULT

```cpp
#include <iostream>
#include <fstream>
#include <cstdio>

void Setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void logo()
{
    std::ifstream file("/app/logo");
    if (file.is_open())
    {
        std::cout << file.rdbuf();
    }
    file.close();
    putchar('\n');
}

void vuln()
{
    char name[0x32];

    logo();
    puts("Hello! welcome to TCP1P!");
    puts("What are you doing?");
    printf("ups leak! %lX\n", (void *)fgets);
    printf("ups leak! %lX\n", (void *)printf);
    printf("ups leak! %lX\n", (void *)puts);
    fgets(name, 1000, stdin);
}

int main()
{
    Setup();
    vuln();
}
```

5. Notice there's an overflow when the program allows the user to input 1000 bytes, but the name variable holds 50 bytes as the buffer.
6. The binary leaks the `fgets()`, `printf()`, and `puts()` address.
7. 

