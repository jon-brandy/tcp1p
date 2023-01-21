# Web Fetcher
> Write-up author: vreshco
## DESCRIPTION:
Kali ini aku buat web fetcher pakai fungsi fetch, coba kalian lihat websiteku ini:
http://ctf.tcp1p.com:47138

## HINT:
1. https://github.com/denoland/deno/tree/main/ext/fetch
2. https://fetch.spec.whatwg.org/

## STEPS:
1. First, unzip the `.zip` file given, then jump to the extracted directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213870463-20677e50-d1d1-45ec-88fe-ff29efccd8fe.png)


2. Well let's open the link given first.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213870676-60242f01-9637-40c0-a342-060a12a3d6c9.png)


3. Based from the hint given and the source code we got, we know this chall is related to **local file inclusion** but with fetch.
4. To test that let's use -> `file://`. For example let's input -> `file:///etc/passwd`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213870756-f4e18f5b-5e60-4ebf-94bc-d4b96f1dcbdf.png)


5. Well reading the **Dockerfile** got a clue that the flag shall be inside the environment variable.

> Dockerfile

![image](https://user-images.githubusercontent.com/70703371/213870944-8911d1ec-a3da-4b6a-aac1-32f9472e2a89.png)


6. I did a small outsource about this and found [this](https://sec-art.net/2021/10/27/exploiting-local-file-inclusion-lfi-vulnerability-with-proc-self-environ-method-lfi-attacks/):

![image](https://user-images.githubusercontent.com/70703371/213871090-5f2707ff-069e-4785-b244-1c4c07b3a9cd.png)


7. Let's use that!

```
file:///proc/self/environ
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213871135-8da7e178-cbe5-41f7-8d04-d8db56c1c666.png)


8. Got the flag!

## FLAG

```
TCP1P{local_file_inclusion_with_fetch}
```

## LEARNING REFERENCES:

```
https://sec-art.net/2021/10/27/exploiting-local-file-inclusion-lfi-vulnerability-with-proc-self-environ-method-lfi-attacks/
```



