# PHP Unserialize 
> Write-up author: jon-brandy
## DESCRIPTION:
Apakah kamu tahu unserialize di php?

http://ctf.tcp1p.com:32116/

## HINT:
- NONE
## STEPS:
1. First open the link given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/214860552-6fe49e50-8480-49f4-8ef3-3d7ed0a1e99a.png)


2. Analyzing the php script, we know that we need to specify the value of 'a' parameter so we can get the flag.
3. Well i did a small outsource about `unserialize()` function in php.

![image](https://user-images.githubusercontent.com/70703371/214862485-50031694-9464-4f8b-ae06-7ffca26646c2.png)


4. So we need to make a new object where it's a flag
