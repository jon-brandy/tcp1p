# You See Often
> Write-up author: vreshco
## DESCRIPTION:
You know those digital clocks and calculators with those fancy numbers that look like they're made up of seven little bars or segments? 
That's a seven segment display! It's a type of electronic display device that can show numbers (and sometimes letters) using seven individual 
segments that can be turned on or off.

Each segment is assigned a specific label, usually labeled A through G, and can be turned on or off independently to create different numbers or letters. 
By combining different segments, you can create any number from 0 to 9, as well as some letters like A, B, C, and E.

So, if you ever need to display some numbers or letters in a sussy way, just remember the seven segment display! 
It's a simple yet effective way to show information in a fun and visually appealing way.

## HINT:
- NONE
## STEPS:
1. Given a `.txt` file with 7 digits binary within it.

![image](https://user-images.githubusercontent.com/70703371/227770249-4ded1b7f-27f2-42c3-a2f9-bb62e18de3e0.png)


2. Based from the description we know it's a **7-Segment Display**, let's try to use [this](https://www.dcode.fr/7-segment-display) online tool.

> Paste all the binary -> Result:

![image](https://user-images.githubusercontent.com/70703371/227770331-628c269f-7a35-454a-b884-8473270fd509.png)


3. Wrap that with `TCP1P{}`, got the flag!

## FLAG

```
TCP1P{5EGM3nt_015PLAy_Ch1PPEr}
```
