# Favorite Number
> Write-up author: vreshco
## DESCRIPTION:
Bisakah kamu menebak angka favoritku?

Catatan: File dibawah merupakan executable untuk linux. 
Kami menyarankan kamu untuk menggunakan Virtual Machine atau WSL jika kamu menggunakan sistem operasi Windows.
## HINT:
- NONE
## STEPS:
1. First, download the file given, then check the file type.

> RESULT - 64 bit binary file, not stripped.

![image](https://user-images.githubusercontent.com/70703371/213906040-d5c8cc62-181a-439b-b265-6d66668442fc.png)


2. Since it's a binary file, let's make it executeable by run chmod, then run the binary.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213906081-1d818a57-a0c1-4bd0-82d2-616f5f24c5d4.png)


3. They want us to guess the correct number, then let's decompile the binary using ghidra

> RESULT - MAIN FUNCTION

![image](https://user-images.githubusercontent.com/70703371/213906152-3fc46d4b-a263-411d-825d-e5f47b5eaecc.png)


4. Based from the main function, now we know the correct fav num is 69.

![image](https://user-images.githubusercontent.com/70703371/213906185-4f1806a0-6aaa-4166-a601-e7c1591f280a.png)


5. No need to patch the binary, let's run it again and enter the input as 69.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213906209-3f0d1f17-9385-4b9c-8544-f4cee892760e.png)


6. Got the flag!

## FLAG

```
TCP1P{G00d_w4y_T0_St4rT_R3v3rs1nG}
```

