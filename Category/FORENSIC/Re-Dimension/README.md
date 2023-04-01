# Re-Dimension
> Writeup-author: vreshco
## DESCRIPTION:
Something is missing in this image
## HINT:
- NONE
## STEPS:
1. Given a corrupted png file.

![image](https://user-images.githubusercontent.com/70703371/229272917-edfb270c-3cb2-45d4-b7ef-2a436c084639.png)


2. Let's use **pngcheck** to see which chunks are broken.

> RESULT

```console
┌──(vreshco㉿nic)-[~/Downloads]
└─$ pngcheck -v dimas-profile-picture-A.png
File: dimas-profile-picture-A.png (405070 bytes)
  chunk IHDR at offset 0x0000c, length 13
    600 x 500 image, 24-bit RGB, non-interlaced
  CRC error in chunk IHDR (computed 6e32c483, expected d45350e1)
ERRORS DETECTED in dimas-profile-picture-A.png
```

3. Let's use **bless** to overwrite the chunks for `d45350e1`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229273169-3802d51c-9202-4e24-8be3-2cb4c2e09052.png)


![image](https://user-images.githubusercontent.com/70703371/229273195-e65223bc-4ee0-4de5-8b82-645eeed8901a.png)


4. 
