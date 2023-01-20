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

> RESULT


