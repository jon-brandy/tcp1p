# Operators
> Write-up author: vrescho
## DESCRIPTION:
Buktikan kalo kamu jago dalam reversing.
## HINT:
- Lakukan analisa menggunakan IDA Pro/Ghidra terlebih dahulu. Pahamilah cara kerja setiap baris kode hasil decompilation dan buatlah "solusi"-nya.
## STEPS:
1. First, unzip the `.zip` file given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/218099624-8762ae27-6359-4aa1-95cd-9132c41e6835.png)


![image](https://user-images.githubusercontent.com/70703371/218099654-c6772df0-02e6-4207-9431-a766a9710cdf.png)


2. Since it's a binary file, let's run it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/218099746-7a528209-a097-4ea3-b352-f3c2ee0d5e18.png)


3. Let's add strings as input.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/218099803-2aa0e1b7-ca3d-49b7-b918-a5a4f09c255e.png)


4. Now let's check the `.txt` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/218100020-4033e642-31a6-4b31-aab2-67be96870fb5.png)


5. Hmm.. Let's decompile the binary.

