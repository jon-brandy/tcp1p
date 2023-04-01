# Crack Me
> Write-up author: vreshco
## DESCRIPTION:
seseorang memberiku file zip aku di suruh membuka file zip tersebut tetapi file zip tersebut di password bantu aku mencari password nya!!!!
## HINT:
- NONE
## STEPS:
1. Given a zip file and within it there's a flag.txt file which locked with a password.

![image](https://user-images.githubusercontent.com/70703371/229272468-9c7084ad-6433-455d-95de-ec01eb18bd45.png)


2. To solve this i used **zip2john** then **john**.
3. Let's get the password hashes to be cracked using **zip2john**.

> COMMAND

```sh
zip2john chall.zip > hash.hashes
```

4. Next let's use **john** to crack the hash file.

> COMMAND

```
john hash.hashes --show
```

> RESULT

```
┌──(vreshco㉿nic)-[~/Downloads]
└─$ john hash.hashes --show         
chall.zip/flag.txt:Front242:flag.txt:chall.zip:chall.zip

1 password hash cracked, 0 left
```

5. Got the password, it's `Front242`.
6. Let's use that.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229272766-4c34a50a-1d55-4e09-b0ab-805a2f798b15.png)


7. Got the flag!

## FLAG

```
TCP1P{cR4ck_Z1p_With_joHn_Th3_riPp3r} 
```
