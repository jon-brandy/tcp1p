# Property
> Write-up author: vreshco
## DESCRIPTION:
Apakah menyimpan sebuah objek bisa berbahaya? mari kita ketahui dengan melakukan pentesting ke website berikut dengan metode white-box.
http://ctf.tcp1p.com:41815
## HINT:
- NONE
## STEPS:
1. First, open the link given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217833799-ee1fbffb-cad2-4b04-aa6b-9dddba44c701.png)


2. Given a registration page, let's register then.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217834208-a9093625-d497-42b6-84f8-19012362c238.png)


3. Hm.. Got nothing here, but let's catch the request using burpsuite, to see if there are any clues or something that can be our interest.

> USING BURPSUITE TO CAPTURE REQUEST WHEN REGISTER BUTTON CLICKED

![image](https://user-images.githubusercontent.com/70703371/218106181-4c642241-bb81-4478-9e20-db4062187d67.png)


3. We successfully got the request, notice there's 2 json params, which are username and password, well still can't be our interest here.
4. Let's check the source code then.

> index.ts

![image](https://user-images.githubusercontent.com/70703371/218106801-abaf48a3-c13c-4851-94e1-f7ab2f03aa5a.png)


5. Looking at the index typescript, we know that there's **routes**.
6. Now let's check the admin typescript.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/218108037-cb5420f0-cfb7-43b0-a841-71564efcb818.png)


7. Finally, there's something that could be our interest, the `isAdmin` class which means there's admin privilege.

![image](https://user-images.githubusercontent.com/70703371/218108588-a146975d-e91e-485d-acda-afc31222ba98.png)


8. Then there's a route to admin.

![image](https://user-images.githubusercontent.com/70703371/218109517-c9045c48-3aaa-4973-a9d3-8dec5ac5a5fe.png)


9. Now we can try by adding JSON param -> `isAdmin:true`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/218110022-9f3b1064-342e-4d56-8f37-a072d4b33161.png)


![image](https://user-images.githubusercontent.com/70703371/218110184-f496a698-f695-4086-a3a2-7399b503fbae.png)


10. Great, looks like there's admin page, click that!

![image](https://user-images.githubusercontent.com/70703371/218110357-967bb50d-943a-4207-9972-462ee3a94c66.png)


11. Got the flag!

## FLAG

```
TCP1P{storing_the_entire_object_is_not_good}
```
