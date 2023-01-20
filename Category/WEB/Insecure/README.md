# Insecure
> Write-up author: vreshco
## DESCRIPTION:
Aku suka cookie! Apalagi chocochip cookie!
http://ctf.tcp1p.com:16544/
## HINT:
- NONE
## STEPS:
1. First, Open the link given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213628467-2fb4291d-4770-439f-9b52-60b6a5124396.png)


2. Based on the description and the result we got, seems like we need to change the admin value at the cookie tab.
3. Since i'm in mozilla, i open inspect element -> storage -> cookies.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213628619-2f7e3b14-ce3a-4c6b-a6ec-ca982eb4e54d.png)


4. Now change the **isAdmin** value to `1`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213628694-70fb2458-a3a0-4af2-ae35-6b6579226370.png)


5. Refresh the page.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213628732-ea03e072-ed36-4ccc-aa2f-145d2dce8f98.png)


6. Now check the page source again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213628896-1a84120c-6388-48fc-bf1c-123d1d442232.png)


7. Got the flag!

## FLAG

```
TCP1P{1ns3cUr3_C00k1Es}
```
