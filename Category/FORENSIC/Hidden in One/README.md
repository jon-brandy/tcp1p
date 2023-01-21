# Hidden in One
> Write-up author: jon-brandy
## DESCRIPTION:
Temanku baru saja menemukan cara baru untuk menyembunyikan sebuah rahasia dan dia memberiku salah satu contohnya. 
Bisakah kamu membantuku membongkar rahasia dia?
## HINT:
- NONE
## STEPS:
1. First, unzip the `.zip` file given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/212634723-e25f2944-8d80-464e-9aa6-44ddf1e51172.png)


2. Check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/212634806-4a81fb4d-5395-4f4e-8498-58bfdf507c8b.png)


3. Since it's an ascii file, hence strings it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/212634921-6b24c875-8e54-432e-b818-77f76eafe5d6.png)


4. Let's cat with `-A` flag.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/212635241-d0b28cdc-38d4-4748-9e0e-5330479eca54.png)


5. Well i tried to use binwalk to the flag.txt file but got nothing.
6. Let's use it to the zip file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213871548-79b005c1-2d64-4707-98ac-e319c18a3120.png)


7. Notice there's a png file, now let's run **foremost** to the file.
8. Jump to the output directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213871599-5db5be78-b656-410e-8f91-3660336655cd.png)


9. Jump to the png directory and see the png file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/213871609-aee5e48a-7ed3-493a-98f1-d8bb4714b965.png)


10. Got the flag!

## FLAG

```
TCP1P{H1dd3N_1n_Pl41n_S1gHt}
```


