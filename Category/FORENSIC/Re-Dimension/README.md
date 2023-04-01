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


4. Already tried stegsolve and other tools to extract any information but didn't get anything.
5. What comes to my mind, we should tamper the CRC to change the image file resolution.
6. To solve this challenge i used this script i found online:

```py
from binascii import crc32

with open("./dimas-profile-picture-A.png", "rb") as f:
    img = f.read()

ihdr_ofset = img.find(b'IHDR')

w = 600
h = 800
crc = b"\x49\x48\x44\x52" + w.to_bytes(4, "big") + h.to_bytes(4, "big") + b"\x08\x06\x00\x00\x00"
crc = crc32(crc)

with open("./result.png", "wb") as f:
    nimg = (crc.to_bytes(4, "big")).join([img[:29], img[29+4:]])
    nimg = (w.to_bytes(4,"big")).join([nimg[:ihdr_ofset+4], nimg[ihdr_ofset+4+4:]])
    nimg = (h.to_bytes(4,"big")).join([nimg[:ihdr_ofset+8], nimg[ihdr_ofset+8+4:]])
    f.write(nimg)
```


7. I changed the **height** to 800.
8. Running this script, resulting to an image named `result.png`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229277185-618a7a2d-9b1e-4284-87f7-5d33f4db9912.png)


9. Change the chunk value again.

> Check it first using pngcheck

```console
┌──(vreshco㉿nic)-[~/Downloads/foren]
└─$ pngcheck -v result.png 
File: result.png (405070 bytes)
  chunk IHDR at offset 0x0000c, length 13
    600 x 800 image, 24-bit RGB, non-interlaced
  CRC error in chunk IHDR (computed 70028b93, expected ff601cc4)
ERRORS DETECTED in result.png

```

10. Fix that using **bless**, open the image file again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229277267-79dcaf36-2120-421b-a1ac-fb961f6d03e7.png)


11. Got the flag!

## FLAG

```
TCP1P{Where's_My_Neko?}
```
