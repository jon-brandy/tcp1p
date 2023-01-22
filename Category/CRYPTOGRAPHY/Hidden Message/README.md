# Hidden Message
> Write-up author: jon-brandy
## DESCRIPTION:
Aku dengar XOR sangat rentan, bisakah kamu membuktikannya?

[FILE](https://ctf.tcp1p.com/files/29c58504395c3827818025261fce0234/chall.zip?token=eyJ1c2VyX2lkIjo0MzQsInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjh9.Y8ULDA.zZgknwGvTNfwsLDZPLUe2N6XmYg)

## HINT:
- NONE
## STEPS:
1. First, unzip the `.zip` file.

![image](https://user-images.githubusercontent.com/70703371/213905789-75512d35-9df0-4e83-a2ea-46c6d30aebc2.png)


> INSIDE TXT FILE

![image](https://user-images.githubusercontent.com/70703371/213905797-9117fe13-70cb-4c8e-8767-449464b425c6.png)


2. Based on the description, i think the text is XORed let's decode it with `dcode.fr`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213905857-fc2bd106-57f3-4dce-8cc6-a5f13b7164cd.png)


3. Got the flag!

## FLAG

```
TCP1P{bRut3f0rc3_c4n_b3_Us3fuLL_s0m3t1m3s}
```
