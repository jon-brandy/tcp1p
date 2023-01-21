# Magic
> Write-up author: vreshco
## DESCRIPTION:
Apakah kamu tau sifat aneh pada suatu operator di PHP?
## HINT:
- NONE
## STEPS:
1. First, open the link given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213866585-5dfef9da-e9f5-4804-a0dc-127c81256fc4.png)


2. Hmm.. Let's open the `.php` file we got then.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213866714-574a4759-73d2-44f9-b411-1dbda29a674e.png)


3. Based on the php script we need to change the `secret` parameter value which has the same md5 value as `0e462097431906509019562988736854`.

![image](https://user-images.githubusercontent.com/70703371/213866825-059e32a2-30c5-4d0d-ab70-bd4964661ff9.png)


4. So i did a small outsource about this hash -> `0e462097431906509019562988736854` and found [this](https://stackoverflow.com/questions/22140204/why-md5240610708-is-equal-to-md5qnkcdzo) documentation.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213866924-cd2350f0-6806-4d70-81da-85922a2cf197.png)


5. It seems we can utilize the `equal` operator -> `==`.

![image](https://user-images.githubusercontent.com/70703371/213866958-1fdd418a-5c81-4fef-b372-429258e983c1.png)


6. I did a small outsource again about hash vulnerability in php and found [this](https://securityaffairs.co/36732/hacking/php-hash-comparison-flaw.html).
7. Based on the article it says that:

![image](https://user-images.githubusercontent.com/70703371/213867171-9ff0c4f3-c186-4066-8736-b49be702ffc9.png)


8. Since the `==` operator in php only comparing the **value**. Then we can add text that if hashed by md5 checksum shall gave us `0e..`.
9. Well i found [this](https://offsec.almond.consulting/super-magic-hash.html) article which gave us the correct strings for our **secret** value.

![image](https://user-images.githubusercontent.com/70703371/213867328-7e5890c2-e263-4dd4-8281-a3e5eee350f5.png)


10. Change the URL to this -> `http://ctf.tcp1p.com:45659/?secret=QNKCDZO`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213867352-790195ea-b464-4a48-96c7-c02c20fb93ab.png)


11. Got the flag!

## FLAG

```
TCP1P{W31rD_PHP_B3h4v10rS} 
```

