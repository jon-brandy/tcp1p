# The Card 
> Write-up author: vreshco
## DESCRIPTION:
Seseorang memberiku id card yang isi nya sandi untuk bisa masuk pintu, 
dan dia berpesan saya memecah sandi sandi itu menjadi beberapa bagian, 
bantu aku mencari bagian-bagian tersebut agar aku bisa masuk pintu tersebut.
## HINT:
- NONE
## STEPS:
1. Given an image file.

![image](https://user-images.githubusercontent.com/70703371/228728148-c42319a0-9a13-464c-b377-b2a1bb678800.png)


3. Let's try to check the metadata.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/228728205-f132e71d-9619-422f-aaf2-da51d3b32b39.png)


4. Notice the comment value we got the last part of the flag (?) -> `Gr34TfUn`.
5. Let's try to decode the hex value below the barcode.

![image](https://user-images.githubusercontent.com/70703371/228728341-2a752957-f7d1-4705-9777-4ce9d80e4ca8.png)


> RESULT

![image](https://user-images.githubusercontent.com/70703371/228728396-b85f2672-ae5c-4cac-979f-7defe1d89c53.png)


6. Got the first part! Let's decode the QRcode now.

![image](https://user-images.githubusercontent.com/70703371/228728599-14355340-c746-4c50-957c-113d245eafc5.png)


7. Got the 2nd part, let's concate them!

## FLAG

```
TCP1P{FoR3nSic_is_Gr34TfUn}
```

